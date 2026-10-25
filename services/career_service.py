from typing import List, Dict, Any, Tuple
from models import db, CareerRole, Job, JobRecommendation, User, Skill


DEFAULT_ROADMAPS = {
    "Web Developer": [
        {
            "step": 1,
            "title": "Step 1: Learn HTML, CSS",
            "desc": "Build static pages, semantic layouts, responsive design using Flexbox and Grid."
        },
        {
            "step": 2,
            "title": "Step 2: Learn JavaScript",
            "desc": "Master DOM manipulation, ES6+ features, async/await, Fetch API, and basic Data Structures."
        },
        {
            "step": 3,
            "title": "Step 3: Learn React",
            "desc": "Components, state management, props, hooks, routing, and modern frontend architecture."
        },
        {
            "step": 4,
            "title": "Step 4: Backend (Node.js & Express)",
            "desc": "Build secure RESTful APIs, connect to MongoDB / SQL databases, authentication, and deployment."
        }
    ],
    "Java Software Engineer": [
        {
            "step": 1,
            "title": "Step 1: Core Java & OOP Concepts",
            "desc": "Classes, inheritance, polymorphism, encapsulation, exception handling, and collections framework."
        },
        {
            "step": 2,
            "title": "Step 2: Data Structures & Algorithms",
            "desc": "Arrays, Linked Lists, Stacks, Queues, Trees, searching and sorting algorithms in Java."
        },
        {
            "step": 3,
            "title": "Step 3: Relational DB & SQL / Hibernate",
            "desc": "Database normalization, complex SQL joins, JDBC connection, and ORM with Hibernate / JPA."
        },
        {
            "step": 4,
            "title": "Step 4: Spring Boot & Microservices",
            "desc": "Spring MVC, dependency injection, REST controllers, Spring Data JPA, Docker, and Maven."
        }
    ],
    "Data Scientist": [
        {
            "step": 1,
            "title": "Step 1: Python & Mathematical Foundations",
            "desc": "Python programming, linear algebra, multivariable calculus, and applied probability & statistics."
        },
        {
            "step": 2,
            "title": "Step 2: Data Analysis & Visualization",
            "desc": "NumPy array manipulation, Pandas data cleaning, Matplotlib, Seaborn, and exploratory data analysis."
        },
        {
            "step": 3,
            "title": "Step 3: Machine Learning Algorithms",
            "desc": "Supervised & unsupervised learning with Scikit-Learn: Regression, Decision Trees, Random Forests, Clustering."
        },
        {
            "step": 4,
            "title": "Step 4: Deep Learning & MLOps",
            "desc": "Neural networks, PyTorch / TensorFlow, model evaluation metrics, and API deployment with Flask/FastAPI."
        }
    ],
    "Cloud & DevOps Engineer": [
        {
            "step": 1,
            "title": "Step 1: Linux & Shell Scripting",
            "desc": "Linux system administration, file permissions, Bash scripting, process management, and networking basics."
        },
        {
            "step": 2,
            "title": "Step 2: Containerization with Docker",
            "desc": "Dockerfiles, image optimization, multi-stage builds, container networking, and Docker Compose."
        },
        {
            "step": 3,
            "title": "Step 3: Cloud Infrastructure (AWS / GCP)",
            "desc": "Compute (EC2 / VMs), Storage (S3 / Cloud Storage), VPC networking, IAM security, and Cloud deployment."
        },
        {
            "step": 4,
            "title": "Step 4: CI/CD & Orchestration",
            "desc": "GitHub Actions, automated pipelines, Kubernetes pod management, and Infrastructure as Code (Terraform)."
        }
    ]
}


class CareerService:
    """Provides career guidance, skill gap analysis, and job recommendations."""

    @staticmethod
    def get_all_roles() -> List[CareerRole]:
        return CareerRole.query.order_by(CareerRole.career_name.asc()).all()

    @staticmethod
    def get_role_by_id(role_id: int) -> CareerRole:
        return CareerRole.query.get(role_id)

    @staticmethod
    def analyze_skill_gap(user_skills: List[str], target_role_name: str) -> Dict[str, Any]:
        """
        Analyzes skill gaps for a user against a target career role (Report Page 4 & 10).
        """
        role = CareerRole.query.filter(CareerRole.career_name.ilike(f"%{target_role_name}%")).first()
        if not role:
            # Fallback mock analysis if role not in database
            required = ["HTML", "CSS", "JavaScript", "React", "Node.js"]
            roadmap = DEFAULT_ROADMAPS.get("Web Developer", [])
            desc = "Modern Web Developer specializing in client-side and server-side web applications."
        else:
            required = role.to_dict()["required_skills"]
            roadmap = role.get_roadmap() or DEFAULT_ROADMAPS.get(role.career_name, [])
            desc = role.description

        norm_user_skills = {s.strip().lower() for s in user_skills if s.strip()}
        acquired = []
        missing = []

        for req in required:
            if req.strip().lower() in norm_user_skills:
                acquired.append(req.strip())
            else:
                missing.append(req.strip())

        total = max(len(required), 1)
        match_percentage = round((len(acquired) / total) * 100)

        # Readiness status
        if match_percentage >= 80:
            status = "Job Ready"
            status_color = "emerald"
        elif match_percentage >= 50:
            status = "Intermediate (Action Required)"
            status_color = "amber"
        else:
            status = "Beginner (Upskilling Needed)"
            status_color = "indigo"

        return {
            "career_name": role.career_name if role else target_role_name,
            "description": desc,
            "match_percentage": match_percentage,
            "status": status,
            "status_color": status_color,
            "acquired_skills": acquired,
            "missing_skills": missing,
            "roadmap": roadmap
        }

    @staticmethod
    def recommend_jobs_for_user(user: User) -> List[Dict[str, Any]]:
        """
        Calculates match scores between user's skills and active jobs (Report Page 13 & 19).
        """
        user_skills = {s.skill_name.strip().lower() for s in user.skills}
        all_jobs = Job.query.all()
        recommendations = []

        for job in all_jobs:
            job_req_skills = [s.strip().lower() for s in job.required_skills.split(",") if s.strip()]
            if not job_req_skills:
                score = 50.0
            else:
                matches = sum(1 for req in job_req_skills if req in user_skills)
                score = round((matches / len(job_req_skills)) * 100, 1)

            # Minimum threshold for recommendation
            score = max(score, 40.0) if len(user_skills) > 0 else 50.0

            recommendations.append({
                "job": job.to_dict(),
                "match_score": score,
                "matched_skills": [s for s in job.required_skills.split(",") if s.strip().lower() in user_skills],
                "missing_skills": [s for s in job.required_skills.split(",") if s.strip().lower() not in user_skills]
            })

        # Sort highest match score first
        recommendations.sort(key=lambda x: x["match_score"], reverse=True)
        return recommendations
