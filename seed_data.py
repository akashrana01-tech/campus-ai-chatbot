import json
from datetime import datetime
from config import Config
from models import db, User, Skill, CareerRole, Job, Resume, InterviewTest, JobRecommendation
from services.career_service import DEFAULT_ROADMAPS
from flask import Flask


def seed_database(app: Flask):
    """Initializes tables and seeds real project data from CareerPilot AI report."""
    with app.app_context():
        db.create_all()

        # 1. Seed Skills
        skill_names = [
            "HTML", "CSS", "JavaScript", "React", "Node.js", "Express",
            "Java", "C", "C++", "Python", "SQL", "MongoDB", "Git",
            "Data Structures", "Docker", "REST APIs", "Machine Learning"
        ]
        skill_map = {}
        for name in skill_names:
            s = Skill.query.filter_by(skill_name=name).first()
            if not s:
                s = Skill(skill_name=name)
                db.session.add(s)
            skill_map[name] = s
        db.session.commit()

        # Refresh map after commit
        for name in skill_names:
            skill_map[name] = Skill.query.filter_by(skill_name=name).first()

        # 2. Seed Career Roles & Roadmaps
        roles_data = [
            {
                "name": "Web Developer",
                "desc": "Designs, builds, and maintains dynamic websites and scalable web applications using modern web stacks.",
                "skills": "HTML, CSS, JavaScript, React, Node.js, Express, MongoDB",
                "roadmap": DEFAULT_ROADMAPS["Web Developer"]
            },
            {
                "name": "Java Software Engineer",
                "desc": "Develops enterprise-grade backend systems, services, and secure software applications using Java and Spring Boot.",
                "skills": "Java, C++, OOP, Data Structures, SQL, REST APIs",
                "roadmap": DEFAULT_ROADMAPS["Java Software Engineer"]
            },
            {
                "name": "Data Scientist",
                "desc": "Extracts actionable insights from complex datasets using Python, statistical modeling, and Machine Learning algorithms.",
                "skills": "Python, SQL, Machine Learning, Data Structures",
                "roadmap": DEFAULT_ROADMAPS["Data Scientist"]
            },
            {
                "name": "Cloud & DevOps Engineer",
                "desc": "Automates cloud deployment pipelines, provisions infrastructure, and manages containerized applications.",
                "skills": "Linux, Docker, Git, REST APIs, Python",
                "roadmap": DEFAULT_ROADMAPS["Cloud & DevOps Engineer"]
            }
        ]

        role_map = {}
        for r_info in roles_data:
            role = CareerRole.query.filter_by(career_name=r_info["name"]).first()
            if not role:
                role = CareerRole(
                    career_name=r_info["name"],
                    description=r_info["desc"],
                    required_skills=r_info["skills"],
                    roadmap_json=json.dumps(r_info["roadmap"])
                )
                db.session.add(role)
            role_map[r_info["name"]] = role
        db.session.commit()

        # 3. Seed Students (Prerna & Shubham from Report Title Page)
        prerna = User.query.filter_by(email="prerna@gmail.com").first()
        if not prerna:
            prerna = User(
                name="Prerna Fartade",
                email="prerna@gmail.com",
                role="student"
            )
            prerna.set_password("Prerna@123")
            # Assign skills
            for sname in ["HTML", "CSS", "JavaScript", "React", "Node.js", "C++", "Git"]:
                if sname in skill_map:
                    prerna.skills.append(skill_map[sname])
            if "Web Developer" in role_map:
                prerna.preferred_careers.append(role_map["Web Developer"])
            db.session.add(prerna)
            db.session.commit()

            # Seed Prerna's Pre-saved Resume (Matches Page 25 & 26 screenshots)
            resume_data = {
                "personal": {
                    "full_name": "Prerna Fartade",
                    "title": "Frontend Developer",
                    "email": "prerna@gmail.com",
                    "phone": "+91 98765 43210",
                    "location": "Pune, Maharashtra",
                    "roll_no": "BC1013"
                },
                "education": {
                    "degree": "BCA in BCA (Science)",
                    "university": "G H Raisoni International Skill Tech University, Pune",
                    "years": "2024 - 2027",
                    "cgpa": "9.18"
                },
                "skills": {
                    "technical": ["JavaScript", "HTML", "CSS", "React", "Node.js", "C++"],
                    "interested_fields": "Web Development, Software Engineering"
                },
                "experience": {
                    "level": "Fresher",
                    "projects": "Vaccicare+ (Vaccine Management Portal), CareerPilot AI Platform"
                }
            }
            prerna_resume = Resume(
                user_id=prerna.user_id,
                resume_content=json.dumps(resume_data)
            )
            db.session.add(prerna_resume)

            # Seed Test Records for Prerna
            test1 = InterviewTest(user_id=prerna.user_id, subject="HTML", score=100, result="Pass")
            test2 = InterviewTest(user_id=prerna.user_id, subject="Java", score=85, result="Pass")
            test3 = InterviewTest(user_id=prerna.user_id, subject="C", score=80, result="Pass")
            db.session.add_all([test1, test2, test3])
            db.session.commit()
            print("[✓] Seeded student profile: Prerna Fartade (BC1013)")

        shubham = User.query.filter_by(email="shubham@gmail.com").first()
        if not shubham:
            shubham = User(
                name="Shubham Panchal",
                email="shubham@gmail.com",
                role="student"
            )
            shubham.set_password("Shubham@123")
            for sname in ["Java", "C++", "C", "SQL", "Python", "Data Structures"]:
                if sname in skill_map:
                    shubham.skills.append(skill_map[sname])
            if "Java Software Engineer" in role_map:
                shubham.preferred_careers.append(role_map["Java Software Engineer"])
            db.session.add(shubham)
            db.session.commit()

            test_shubham = InterviewTest(user_id=shubham.user_id, subject="Java", score=90, result="Pass")
            db.session.add(test_shubham)
            db.session.commit()
            print("[✓] Seeded student profile: Shubham Panchal (BC1029)")

        # 4. Seed Guide / Admin Account (Prof. Vaishnavi Lokhande)
        admin = User.query.filter_by(email="guide@raisoni.edu").first()
        if not admin:
            admin = User(
                name="Prof. Vaishnavi Lokhande (Project Guide)",
                email="guide@raisoni.edu",
                role="admin"
            )
            admin.set_password("Admin@123")
            db.session.add(admin)
            db.session.commit()
            print("[✓] Seeded project guide / admin: Prof. Vaishnavi Lokhande (guide@raisoni.edu / Admin@123)")

        # 5. Seed Jobs (Report Page 13 & 19)
        if Job.query.count() == 0:
            web_role_id = role_map.get("Web Developer").career_id if role_map.get("Web Developer") else None
            java_role_id = role_map.get("Java Software Engineer").career_id if role_map.get("Java Software Engineer") else None
            data_role_id = role_map.get("Data Scientist").career_id if role_map.get("Data Scientist") else None

            sample_jobs = [
                Job(
                    career_id=web_role_id,
                    job_title="Junior Frontend Developer",
                    company_name="TechCorp Solutions",
                    location="Pune, Hinjewadi",
                    required_skills="HTML, CSS, JavaScript, React",
                    salary_range="₹4.5 - ₹6.5 LPA",
                    experience_level="Fresher / 0-1 yr"
                ),
                Job(
                    career_id=java_role_id,
                    job_title="Java Developer Trainee",
                    company_name="Infosys Technologies",
                    location="Pune, Magarpatta",
                    required_skills="Java, C++, SQL, OOP",
                    salary_range="₹4.0 - ₹6.0 LPA",
                    experience_level="Fresher"
                ),
                Job(
                    career_id=web_role_id,
                    job_title="Full Stack Web Intern",
                    company_name="InnovateTech Labs",
                    location="Pune / Remote",
                    required_skills="JavaScript, React, Node.js, Express, MongoDB",
                    salary_range="₹5.0 - ₹7.2 LPA",
                    experience_level="Fresher / Intern"
                ),
                Job(
                    career_id=data_role_id,
                    job_title="Associate Data Analyst",
                    company_name="Analytics Hub India",
                    location="Pune, Viman Nagar",
                    required_skills="Python, SQL, Data Structures",
                    salary_range="₹4.8 - ₹7.0 LPA",
                    experience_level="Fresher"
                ),
                Job(
                    career_id=web_role_id,
                    job_title="UI/UX React Developer",
                    company_name="DesignCraft Systems",
                    location="Mumbai / Pune",
                    required_skills="HTML, CSS, JavaScript, React, Git",
                    salary_range="₹4.5 - ₹6.0 LPA",
                    experience_level="Fresher"
                )
            ]
            db.session.add_all(sample_jobs)
            db.session.commit()
            print(f"[✓] Seeded {len(sample_jobs)} industry job listings.")


if __name__ == "__main__":
    from app import create_app
    app = create_app()
    seed_database(app)
    print("CareerPilot AI database initialized successfully!")
