# CampusAI - AI College Assistant Chatbot Website

> **Academic Project**: SYBBA (Computer Applications) Semester III  
> **Topic**: AI-Powered Virtual Assistant & College Knowledge Base System  
> **Tech Stack**: Python (Flask), SQLite, SQLAlchemy, HTML5, CSS3, Modern JavaScript, Google Gemini AI (Optional)

---

## 1. Project Overview

**CampusAI** is a modern, responsive web application designed to help prospective and enrolled college students find instant, verified answers to their questions 24 hours a day, 7 days a week.

Students frequently need quick details regarding:
- **Admissions & Eligibility**: Criteria for BBA, BCA / SYBBA (CA), B.Com, cutoff lists, required documents.
- **Courses & Semesters**: Detailed subject curriculums, syllabuses, practical labs, and graduation requirements.
- **College Fees & Payment**: Annual tuition breakdowns, installment options, payment methods, and merit scholarships.
- **Examinations & Timetables**: Mid-term and end-semester dates, hall ticket downloads, and grading rules.
- **Campus Facilities**: Central digital library hours, computer labs, hostels, cafeteria, sports complex, and Wi-Fi.
- **Office Timings & Contact Details**: Administrative hours, contact emails, emergency helplines, and department desks.

### 🛡️ Zero Hallucinations Policy
CampusAI is strictly grounded in official college records stored in an SQLite database. If a question is outside the verified knowledge base (or if an AI provider fails), the system **never invents** fees, dates, or regulations. Instead, it politely informs the student and provides direct contact information for the **College Administration Office**.

---

## 2. Architecture & Technology Stack

| Component | Technology | Description |
|-----------|------------|-------------|
| **Frontend** | HTML5, CSS3, Vanilla JavaScript | Responsive startup-grade UI, CSS custom properties, glassmorphism, animated typing indicator, accessible semantic HTML. |
| **Backend** | Python 3.10+, Flask 3.x | Lightweight, clean REST API endpoints, session security, CSRF protection, and rate limiting. |
| **Database** | SQLite + SQLAlchemy ORM | Local, zero-configuration relational database storing FAQs, admin accounts, and student chat logs. |
| **AI Integration** | Google Gemini API (`google-genai` SDK) | Grounded LLM service layer using `gemini-3.8-flash` with system prompt grounding. |
| **NLP & Fallback** | Python Similarity Matcher | Multi-signal token overlap, domain synonym expansion, and Levenshtein similarity. Operates 100% offline without any API key. |

---

## 3. Project Directory Structure

```
ai-college-assistant/
├── app.py                   # Application factory, page routes, and REST API endpoints
├── config.py                # Environment and configuration settings
├── models.py                # SQLAlchemy models (FAQ, Admin, ChatMessage, QueryLog)
├── seed_data.py             # Database initialization and 20 demo college FAQs
├── create_admin.py          # Secure CLI tool to create administrator accounts
├── run_tests.py             # Automated test suite runner (23 unit & integration tests)
├── requirements.txt         # Python package dependencies
├── .env.example             # Example environment variable template
├── .env                     # Local environment configuration
├── .gitignore               # Git ignore rules for virtualenv, database, and cache
├── services/
│   ├── __init__.py
│   ├── chatbot.py           # Conversational orchestrator, greeting detection & logging
│   ├── faq_service.py       # Normalized text preprocessing, synonyms & similarity scoring
│   └── ai_service.py        # Google Gemini AI integration with strict grounding
├── templates/
│   ├── base.html            # Shared header, navbar, footer, and toast notification container
│   ├── index.html           # Modern landing page with interactive preview & popular questions
│   ├── chat.html            # Full-featured student chat interface with dynamic chips & sidebar
│   ├── faqs.html            # Searchable FAQ accordion directory with category filtering
│   ├── admin_login.html     # Secure administrator login with demo credential quick-fill
│   └── admin_dashboard.html # Admin panel for FAQ CRUD operations and student query analytics
├── static/
│   ├── css/
│   │   └── style.css        # Premium custom CSS styling (Navy & Indigo theme)
│   └── js/
│       ├── main.js          # Shared UI helpers (toasts, mobile menu, copy-to-clipboard)
│       └── chat.js          # Chatbot controller (session management, auto-scroll, chips)
└── tests/
    ├── __init__.py
    ├── test_app.py          # Page status and health check tests
    ├── test_faqs.py         # FAQ listing, category filter, and search tests
    ├── test_chatbot.py      # Known questions, unknown fallback, and AI failure tests
    └── test_admin.py        # Authentication, session protection, and FAQ CRUD tests
```

---

## 4. Setup and Installation (macOS Terminal)

Follow these exact steps to run the project on macOS:

### Step 1: Open Terminal and Navigate to Project
```bash
cd "/Users/kanishksingh/Downloads/momo ai chat bot "
```

### Step 2: Initialize Virtual Environment
```bash
python3 -m venv --system-site-packages .venv
source .venv/bin/activate
```

### Step 3: Install Required Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables
Copy `.env.example` to `.env` (already done by default):
```bash
cp .env.example .env
```

*(Optional)* If you have a Google Gemini API key, add it inside `.env`:
```ini
GEMINI_API_KEY=your_actual_gemini_api_key_here
GEMINI_MODEL=gemini-3.8-flash
```
> **Note**: If `GEMINI_API_KEY` is left blank, the application automatically runs in **100% offline Knowledge Base mode**, using internal NLP and database matching with zero degradation of functionality.

### Step 5: Initialize and Seed the Database
Populate the SQLite database with the default administrator and 20 verified demo college FAQs:
```bash
python seed_data.py
```
*Output:*
```
[✓] Seeded default administrator account: admin / Admin@123
[✓] Seeded 20 demo FAQs across all categories.
[✓] Database initialization and seeding complete.
```

### Step 6: Start the Flask Web Server
```bash
python app.py
```
Open your browser and navigate to: **`http://127.0.0.1:5000`**

---

## 5. Default Demonstration Credentials

For ease of testing and presentation, the following default administrator account is pre-configured:

| Role | Username / Email | Password | Access URL |
|------|-------------------|----------|------------|
| **Administrator** | `admin` (or `admin@campusai.edu`) | `Admin@123` | [http://127.0.0.1:5000/admin/login](http://127.0.0.1:5000/admin/login) |

*You can also use the convenient "Auto-fill Demo Credentials" button on the login screen.*

### Creating Additional Admin Accounts
You can securely create custom administrator accounts using the included CLI tool:
```bash
python create_admin.py --username staff1 --email staff1@campusai.edu --password SecurePassword@123
```

---

## 6. Running the Automated Test Suite

The project includes a comprehensive automated test suite verifying all 23 key requirements:

```bash
python run_tests.py
```

Or run via pytest:
```bash
pytest -v
```

### Test Coverage Highlights:
- **Landing Page & Route Tests**: Tests status codes (200), header rendering, and `/api/health`.
- **FAQ Retrieval & Search Tests**: Tests full listing, category filtering (`?category=Fees`), and keyword search (`?q=admission`).
- **Admin Authentication Tests**: Successful login, wrong password rejection (401), and unauthorized route redirection.
- **Admin CRUD Operations**: Tests creating a new FAQ, editing questions/answers, and deleting with immediate database persistence.
- **Chatbot Known Question Matching**: Verifies correct FAQ retrieval for fees, admissions, and exam timetables.
- **Chatbot Unknown Fallback**: Verifies polite fallback without hallucinating on out-of-scope queries (e.g. "Can I land a rocket on campus?").
- **AI Resilience Test**: Verifies that when the AI service experiences connection timeouts, the chatbot seamlessly falls back to local FAQ matching without user disruption.

---

## 7. Key Features Walkthrough

### A. Landing Page (`/`)
- Professional hero banner with gradient accents and live statistics.
- Interactive chatbot preview card allowing users to try sample questions.
- Feature grid explaining 24/7 availability, verified answers, and privacy.
- Popular questions cards with 1-click links to the chatbot.
- College contact details in the footer.

### B. Student Chatbot (`/chat`)
- Real-time conversational interface with welcome banner and message bubbles.
- Dynamic suggestion chips that update according to query topics.
- Side drawer with quick access to common categories (Admissions, Fees, Exams, Facilities).
- Animated typing indicator while processing.
- "Copy Answer" button on every assistant message.
- URL parameter support: accessing `/chat?q=What+are+the+fees` automatically runs the query!

### C. Searchable FAQ Directory (`/faqs`)
- Real-time instant search bar with live character-by-character filtering.
- Category filter pills with count badges (All, Admissions, Courses, Fees, Examinations, Facilities, General).
- Expandable accordions with verified stamps and category badges.
- Direct "Ask in Chatbot" button next to every FAQ.
- Friendly empty state when no matching question is found.

### D. Admin Dashboard (`/admin/dashboard`)
- KPI summary cards (Total FAQs, Total Categories, Total Queries Logged, AI Mode).
- Full FAQ Management Table with live search and category dropdown filters.
- Add FAQ Modal, Edit FAQ Modal, and Delete Confirmation Modal.
- Live Real-Time Student Query Log tracking all incoming questions and their resolution source.
- Immediate reflection: Any FAQ created, edited, or deleted in the admin dashboard is immediately updated in the student chatbot.

---

## 8. REST API Reference

| Endpoint | Method | Authentication | Description |
|----------|--------|----------------|-------------|
| `/api/health` | GET | Public | Health status check and FAQ count. |
| `/api/faqs` | GET | Public | Returns list of FAQs with optional `?category=` filter. |
| `/api/faqs/search` | GET | Public | Search FAQs by keyword `?q=` and optional `?category=`. |
| `/api/chat` | POST | Public (Rate-limited) | Receives `{"message": "...", "session_id": "..."}`, returns response, source, and suggestions. |
| `/api/admin/login` | POST | Public (Rate-limited) | Authenticates administrator with username/email and password. |
| `/api/admin/logout` | POST | Admin Session | Ends active admin session. |
| `/api/admin/stats` | GET | Admin Session | Returns counts, category stats, and query logs. |
| `/api/admin/faqs` | POST | Admin Session + CSRF | Creates a new FAQ entry. |
| `/api/admin/faqs/<id>` | PUT | Admin Session + CSRF | Updates an existing FAQ entry. |
| `/api/admin/faqs/<id>` | DELETE | Admin Session + CSRF | Permanently deletes an FAQ entry. |

---

## 9. Security & Best Practices

1. **Password Security**: Passwords are never stored in plaintext; hashed using `werkzeug.security.generate_password_hash` with secure PBKDF2 salt.
2. **CSRF Protection**: State-changing requests (`POST`, `PUT`, `DELETE`) require a valid session CSRF token sent via `X-CSRFToken` header.
3. **Session Hardening**: Cookies configured with `HttpOnly=True` and `SameSite=Lax`.
4. **Rate Limiting**: Built-in memory sliding window limiter prevents abuse of login attempts and chat queries.
5. **XSS Prevention**: Safe text node rendering in JavaScript (`textContent`) and HTML escaping in Jinja templates prevent script injection.
6. **No API Key Leaks**: All AI communications occur strictly on the Python backend; frontend never has access to secret keys.

---

## 10. Troubleshooting

- **Database file locked or unable to open**:
  Ensure the `instance/` folder exists in your project root (`mkdir -p instance`). The application automatically creates this on boot.
- **Port 5000 already in use (macOS AirPlay)**:
  On macOS Monterey or newer, AirPlay Receiver uses port 5000. You can disable AirPlay Receiver in *System Settings > General > AirDrop & AirPlay*, or run Flask on port 5001:
  ```bash
  python -c "from app import app; app.run(port=5001, debug=True)"
  ```
- **Virtual Environment Activation**:
  If commands fail with `ModuleNotFoundError: flask`, ensure your virtual environment is active:
  ```bash
  source .venv/bin/activate
  ```

---

*Developed for the SYBBA (Computer Applications) Semester III Project Demonstration.*
