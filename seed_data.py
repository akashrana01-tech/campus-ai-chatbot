import sys
from datetime import datetime
from config import Config
from models import db, FAQ, Admin
from flask import Flask

DEMO_FAQS = [
    # Category: Admissions
    {
        "category": "Admissions",
        "question": "What are the eligibility criteria for undergraduate courses (BBA / BCA / B.Com)?",
        "answer": "[DEMO RECORD] Candidates must have passed Higher Secondary Certificate (10+2) or equivalent examination from a recognized board with a minimum of 50% aggregate marks (45% for reserved categories). For BCA / SYBBA (CA), Mathematics or Statistics at 10+2 level is preferred.",
    },
    {
        "category": "Admissions",
        "question": "How can I apply for admission to the college?",
        "answer": "[DEMO RECORD] Step 1: Visit the online admission portal on the college website.\nStep 2: Register with your active email address and phone number.\nStep 3: Fill in academic details and upload self-attested documents (Mark sheets, ID proof, passport photo).\nStep 4: Pay the non-refundable registration fee of $25 / Rs. 500 online.\nStep 5: Download the acknowledgment receipt and wait for the merit list announcement.",
    },
    {
        "category": "Admissions",
        "question": "What documents are required during the admission process?",
        "answer": "[DEMO RECORD] You must submit original and photocopies of: 1) 10th and 12th Grade Mark sheets, 2) School/College Leaving Certificate (Transfer Certificate), 3) Migration Certificate (if transferring from other boards/universities), 4) Government-issued Photo ID (Aadhar/Passport), 5) Caste/Category Certificate (if applicable), and 6) 4 recent passport-size photographs.",
    },
    {
        "category": "Admissions",
        "question": "When is the last date to apply for new admissions?",
        "answer": "[DEMO RECORD] For the upcoming academic semester, online admission applications close on July 31st. Late applications with a nominal late fee may be permitted until August 10th subject to seat availability. Please verify the current notification on the college notice board.",
    },

    # Category: Courses
    {
        "category": "Courses",
        "question": "What courses and programs does the college offer?",
        "answer": "[DEMO RECORD] Our college offers undergraduate degrees in:\n- Bachelor of Business Administration (BBA)\n- Bachelor of Computer Applications (BCA / SYBBA Computer Applications)\n- Bachelor of Science in Computer Science (B.Sc CS)\n- Bachelor of Commerce (B.Com)\n- Master of Science in Information Technology (M.Sc IT)\nAll programs feature modern semester curriculums, practical lab hours, and internship projects.",
    },
    {
        "category": "Courses",
        "question": "What is the curriculum and syllabus for SYBBA (CA) Semester III?",
        "answer": "[DEMO RECORD] The SYBBA (Computer Applications) Semester III curriculum includes:\n1. Relational Database Management Systems (RDBMS & SQL)\n2. Data Structures using C/C++\n3. Core Java & Object-Oriented Programming\n4. Principles of Management & Accounting\n5. Practical Lab on RDBMS & Java\n6. Minor Software Development Mini-Project.",
    },
    {
        "category": "Courses",
        "question": "Does the college offer internship and campus placement support?",
        "answer": "[DEMO RECORD] Yes, our dedicated Training & Placement Cell (TPC) conducts career readiness workshops, resume building sessions, and on-campus recruitment drives starting in Semester V. Leading IT and financial consulting firms participate annually with average salary packages of $45,000 / Rs. 4.5 LPA.",
    },

    # Category: Fees
    {
        "category": "Fees",
        "question": "What are the college fees for undergraduate courses?",
        "answer": "[DEMO RECORD] The approximate annual tuition fees are:\n- BBA: $1,200 (Rs. 45,000 / year)\n- BCA / SYBBA (CA): $1,500 (Rs. 55,000 / year)\n- B.Sc Computer Science: $1,400 (Rs. 50,000 / year)\n- B.Com: $800 (Rs. 30,000 / year)\nLaboratory and library deposits are one-time and refundable upon course completion.",
    },
    {
        "category": "Fees",
        "question": "Can college fees be paid in installments?",
        "answer": "[DEMO RECORD] Yes. Tuition fees can be paid in two equal installments: 50% at the time of admission/semester commencement, and the remaining 50% before the mid-term examinations. Students must submit an installment request form at the Accounts Section (Room 104).",
    },
    {
        "category": "Fees",
        "question": "What payment methods are accepted for fee payments?",
        "answer": "[DEMO RECORD] Fees can be paid through:\n1. Online Net Banking, Credit/Debit Cards, or UPI via the student portal\n2. Demand Draft (DD) drawn in favor of 'CampusAI College Educational Trust'\n3. Bank Challan at the campus branch of National Bank\n*Cash payments exceeding $100 / Rs. 5000 are not accepted at the cashier counter.*",
    },
    {
        "category": "Fees",
        "question": "Are there any merit scholarships or financial aid schemes?",
        "answer": "[DEMO RECORD] Yes, the college awards 25% to 50% tuition waivers to students securing above 90% in their qualifying exams. In addition, government social welfare scholarships (EBC, SC/ST, and minority scholarships) are fully facilitated through the college Scholarship Cell.",
    },

    # Category: Examinations
    {
        "category": "Examinations",
        "question": "When are the semester examinations conducted?",
        "answer": "[DEMO RECORD] Odd semester examinations (Semesters I, III, V) are typically conducted in November–December. Even semester examinations (Semesters II, IV, VI) are held in April–May. Exact datesheets are published on the website 30 days prior to commencement.",
    },
    {
        "category": "Examinations",
        "question": "How can students download their examination hall ticket?",
        "answer": "[DEMO RECORD] Hall tickets become available 7 days before examination commencement. Log in to the Student Portal > Exams Tab > Download Hall Ticket. Make sure to print a physical copy and verify your subject codes and photograph.",
    },
    {
        "category": "Examinations",
        "question": "What is the passing criteria and attendance requirement for exams?",
        "answer": "[DEMO RECORD] A student must secure a minimum of 40% marks in both internal assessments and university end-semester examinations independently. Furthermore, a minimum of 75% attendance across lectures and practical laboratories is mandatory to be eligible to appear for final exams.",
    },

    # Category: Facilities
    {
        "category": "Facilities",
        "question": "What facilities are available on the college campus?",
        "answer": "[DEMO RECORD] The campus features:\n- Central Air-Conditioned Digital Library with over 50,000 books and IEEE/ACM digital access\n- High-performance Computer Labs with Gigabit fiber connectivity\n- On-campus Boys and Girls Hostels with 24/7 security\n- Multipurpose Sports Complex, Gymnasium, and Indoor Badminton Court\n- Hygienic cafeteria serving breakfast, lunch, and refreshments\n- Campus-wide secure high-speed Wi-Fi.",
    },
    {
        "category": "Facilities",
        "question": "What are the library timings and membership rules?",
        "answer": "[DEMO RECORD] The Central Library is open Monday through Saturday from 8:00 AM to 8:00 PM. During examination periods, the reading hall remains open until 11:00 PM. Each undergraduate student may borrow up to 3 books for a period of 14 days using their Student RFID card.",
    },
    {
        "category": "Facilities",
        "question": "Is there hostel accommodation available for outstation students?",
        "answer": "[DEMO RECORD] Yes, separate secure hostels for male and female students are located inside the campus perimeter. Facilities include double and triple-sharing furnished rooms, Wi-Fi, laundry service, study lounges, and nutritious meal plans. Hostel allotment is on a first-come, first-served basis upon admission confirmation.",
    },

    # Category: General
    {
        "category": "General",
        "question": "What are the college office timings and working days?",
        "answer": "[DEMO RECORD] Academic classes run Monday through Friday from 8:30 AM to 3:30 PM. Administrative offices (Student Section, Accounts, and Principal's Office) operate Monday through Friday from 8:30 AM to 5:00 PM, and Saturday from 9:00 AM to 1:00 PM. All offices remain closed on Sundays and gazetted public holidays.",
    },
    {
        "category": "General",
        "question": "How can I contact the college administration?",
        "answer": "[DEMO RECORD] You can contact the college via:\n- General Enquiries: admin@campusai.edu\n- Admissions Helpdesk: admissions@campusai.edu\n- Phone Helpline: +1-800-555-CAMPUS / (555) 019-2834\n- Campus Address: 100 University Avenue, Academic Hills, NY 10001\n- Admissions Helpdesk: Ground Floor, Administrative Block.",
    },
    {
        "category": "General",
        "question": "Where can I find the official college holiday list and academic calendar?",
        "answer": "[DEMO RECORD] The annual Academic Calendar and gazetted holiday list are published in the 'Notices & Circulars' section on the college website and displayed on the student notice board in the main lobby. Major vacation periods include the Diwali/Autumn break (2 weeks) and Summer recess (June).",
    },
]


def seed_database(app: Flask):
    """Initializes tables and seeds demo FAQs and the default administrator account."""
    with app.app_context():
        db.create_all()

        # Seed or update Admin
        existing_admin = Admin.query.filter_by(username="admin").first()
        if not existing_admin:
            admin = Admin(
                username="admin",
                email="admin@campusai.edu",
            )
            admin.set_password("Admin@123")
            db.session.add(admin)
            print("[✓] Seeded default administrator account: admin / Admin@123")
        else:
            print("[*] Admin user already exists.")

        # Seed FAQs if empty
        current_faq_count = FAQ.query.count()
        if current_faq_count == 0:
            for item in DEMO_FAQS:
                faq = FAQ(
                    category=item["category"],
                    question=item["question"],
                    answer=item["answer"],
                )
                db.session.add(faq)
            db.session.commit()
            print(f"[✓] Seeded {len(DEMO_FAQS)} demo FAQs across all categories.")
        else:
            print(f"[*] Database already contains {current_faq_count} FAQs. Skipping duplicate seeding.")


if __name__ == "__main__":
    from app import create_app
    app = create_app()
    seed_database(app)
    print("[✓] Database initialization and seeding complete.")
