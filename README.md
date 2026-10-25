# CareerPilot AI - Intelligent Career Guidance & Preparation Platform

> **Academic Project Report Implementation**  
> **Institution**: G H Raisoni International Skill Tech University, Pune-412207  
> **Course**: Bachelor of Computer Applications (Science) — SYBCA, Semester IV  
> **Academic Year**: 2025-26 (Evaluation Year 2026-27)  
> **Submitted By**: **Prerna Fartade** (BC1013) & **Shubham Panchal** (BC1029)  
> **Under the Guidance of**: **Prof. Vaishnavi Lokhande**

---

## 1. Project Overview & Abstract

In today's fast-changing and competitive tech world, selecting the right career path is challenging for computer science and applications students. Traditional career counseling often lacks personalization, data-driven insights, and integrated tools.

**CareerPilot AI** is developed as a unified, comprehensive student platform that integrates:
1. **Career Guidance & Roadmaps**: Analyzes student skills, identifies skill gaps, and generates step-by-step learning roadmaps (e.g. Web Developer, Java Software Engineer, Data Scientist, Cloud & DevOps).
2. **Step-by-Step Resume Builder**: A 4-step wizard with real-time live preview matching student profiles, supporting instant PDF print-ready export.
3. **Interview Preparation**: Practice aptitude and technical multiple-choice questions in **C, C++, Java, HTML, Python, and SQL** with instant evaluation, score tracking, and detailed explanations.
4. **Job Recommendation Engine**: Automatically matches user skills against real industry job openings with calculated match percentages.
5. **AI Career Advisor**: An integrated conversational counselor for answering career, salary, and placement queries.

---

## 2. Normalized Database Design (3NF)

Implements the exact 3NF relational schema documented in Pages 11–13 of the project report:

- `users` (`user_id`, `name`, `email`, `password_hash`, `role`, `created_at`)
- `skills` (`skill_id`, `skill_name`)
- `user_skills` (`user_id`, `skill_id`)
- `career_roles` (`career_id`, `career_name`, `description`, `required_skills`, `roadmap_json`)
- `user_career_preference` (`user_id`, `career_id`)
- `resumes` (`resume_id`, `user_id`, `resume_content`, `created_at`)
- `jobs` (`job_id`, `career_id`, `job_title`, `company_name`, `location`, `required_skills`, `salary_range`)
- `interview_tests` (`test_id`, `user_id`, `subject`, `score`, `total_questions`, `result`, `test_date`)
- `job_recommendations` (`recommendation_id`, `user_id`, `job_id`, `match_score`)

---

## 3. Pre-Seeded Demonstration Accounts

For viva, external examination, and live evaluation, the database comes pre-seeded with the student authors and project guide:

| Role | Name | Email | Password | Pre-loaded Data |
|---|---|---|---|---|
| **Student** | **Prerna Fartade (BC1013)** | `prerna@gmail.com` | `Prerna@123` | BCA, 9.18 CGPA, Vaccicare+ project, HTML/JS/React skills, 3 test scores |
| **Student** | **Shubham Panchal (BC1029)** | `shubham@gmail.com` | `Shubham@123` | BCA, Java/C++/Python skills, 90% Java test score |
| **Project Guide** | **Prof. Vaishnavi Lokhande** | `guide@raisoni.edu` | `Admin@123` | Admin dashboard access, student directory, test audit log |

*(1-Click Demo Login buttons are provided on the login page for instant examiner sign-in).*

---

## 4. Quick Launch Instructions (macOS Terminal)

```bash
# 1. Navigate to project directory
cd "/Users/kanishksingh/Downloads/momo ai chat bot "

# 2. Activate virtual environment
source .venv/bin/activate

# 3. Run automated test suite (11 unit/integration tests)
python run_tests.py

# 4. Start Flask server
python app.py
```
Open **`http://127.0.0.1:5000`** in your browser.

---

## 5. Deployment on Render

This repository is ready to deploy directly on [Render.com](https://render.com):
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app`
- **Plan**: Free ($0/month)
- **Environment Variables**:
  - `SECRET_KEY`: `careerpilot-production-secret-2026`
  - `FLASK_ENV`: `production`

---

## 6. Page Routes Overview

- **Home Screen (`/`)**: Hero banner, core module cards, and university project credits.
- **Career Guidance (`/guidance`)**: Timeline roadmap (Step 1 to Step 4), skill gap analyzer, and AI Counselor chat.
- **Resume Builder (`/resume`)**: 4-step wizard form, live formatted resume sheet preview, and Print Preview.
- **Interview Prep (`/interview`)**: Interactive MCQ quizzes for C, C++, Java, HTML, Python, and SQL.
- **Job Recommendations (`/jobs`)**: Skill matching against industry opportunities.
- **Student Dashboard (`/dashboard`)**: Student test history, saved resume snapshot, and job matches.
- **Admin Dashboard (`/admin`)**: Faculty control panel with enrolled students directory and test submissions.
