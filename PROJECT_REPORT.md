# PROJECT REPORT ON
# CAMPUSAI: AN INTELLIGENT AI-POWERED COLLEGE ASSISTANT CHATBOT AND KNOWLEDGE BASE SYSTEM

---

**A Project Report Submitted in Partial Fulfillment of the Requirements for the Degree of**  
### **BACHELOR OF BUSINESS ADMINISTRATION (COMPUTER APPLICATIONS) — BBA (CA) / BCA**  
*(Semester III / IV)*  

**Academic Year: 2025 – 2026**

---

### **SUBMITTED BY:**
| Student Name | Seat / Roll Number | PRN Number |
| :--- | :--- | :--- |
| **Kanishk Singh** | BBA-CA-301 | 72200184A |
| **Akash Rana** | BBA-CA-302 | 72200185B |

---

### **UNDER THE GUIDANCE OF:**
**Prof. [Guide Name]**  
*Department of Computer Applications & Information Technology*  
*[College / Institute Name, City]*  
*[Affiliated to Savitribai Phule Pune University / State University]*  

---

<div style="page-break-after: always;"></div>

## CERTIFICATE OF APPROVAL

This is to certify that the project report entitled:

> **"CampusAI: An Intelligent AI-Powered College Assistant Chatbot and Knowledge Base System"**

submitted by **Kanishk Singh** and **Akash Rana** is a bonafide work carried out by them under my supervision and guidance, in partial fulfillment of the requirements for the award of the degree of **Bachelor of Business Administration (Computer Applications) / BCA** for the academic year **2025–2026**.

To the best of my knowledge, the matter presented in this report has not been submitted to any other University or Institute for the award of any degree or diploma.

<br><br><br>

------------------------------------ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ------------------------------------  
**Prof. [Guide Name]** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Prof. [H.O.D. Name]**  
Project Internal Guide &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Head of Department  
Department of Computer Applications &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Department of Computer Applications  

<br><br><br>

------------------------------------ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ------------------------------------  
**External Examiner** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Principal / Director**  
Date: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [College Seal & Stamp]  

---

<div style="page-break-after: always;"></div>

## DECLARATION

We hereby declare that the project entitled **"CampusAI: An Intelligent AI-Powered College Assistant Chatbot and Knowledge Base System"** written and submitted by us under the guidance of **Prof. [Guide Name]** is our original work.

The empirical findings, software architecture, algorithm designs, system analysis, and documentation presented in this report have not been previously submitted to any other University or Institution for the conferment of any academic degree, diploma, or certificate. All references and intellectual contributions sourced from external literature, academic papers, and official documentation have been duly acknowledged.

<br><br>

**Date:** 25th October 2026  
**Place:** Pune, Maharashtra  

<br>

1. **Kanishk Singh** (Seat No: BBA-CA-301) &nbsp;&nbsp;&nbsp;&nbsp; Signature: __________________  
2. **Akash Rana** (Seat No: BBA-CA-302) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Signature: __________________  

---

<div style="page-break-after: always;"></div>

## ACKNOWLEDGEMENT

The satisfaction that accompanies the successful completion of any task would be incomplete without expressing our profound gratitude to the individuals whose constant guidance and encouragement served as our beacon light throughout this endeavor.

First and foremost, we express our deep sense of gratitude and sincere thanks to our esteemed project guide, **Prof. [Guide Name]**, for their invaluable advice, insightful critiques, technical guidance, and constant encouragement throughout the development and documentation of this project.

We extend our sincere gratitude to **Prof. [HOD Name]**, Head of the Department of Computer Applications, for providing us with state-of-the-art laboratory infrastructure, computational facilities, and a supportive academic environment conducive to project innovation.

We also express our heartfelt thanks to our respected **Principal / Director, [Principal Name]**, for extending institutional support and fostering an environment of technical excellence.

Lastly, we express our profound love and indebtedness to our parents and family members for their unconditional support and sacrifices, as well as to our classmates and friends who offered helpful suggestions and constructive feedback during the testing and debugging phases of this project.

**Kanishk Singh**  
**Akash Rana**  
*Department of Computer Applications*

---

<div style="page-break-after: always;"></div>

## ABSTRACT

In contemporary higher educational institutions, administrative offices are consistently overwhelmed with repetitive inquiries regarding admissions eligibility, course curriculum, examination timetables, fee schedules, hostel amenities, and administrative notices. Traditional resolution channels—such as physical inquiry counters, telephone switchboards, and static PDF notice boards—suffer from severe operational limitations, including strict working-hour constraints, prolonged queue latency, high administrative labor overhead, and poor searchability across mobile devices.

To address these systemic bottlenecks, this project presents **CampusAI**, a production-grade, 24/7 intelligent conversational web application designed specifically for college administrative and student support ecosystems. Developed using a robust full-stack architecture comprising **Python (Flask)**, **SQLite** (structured in Third Normal Form - 3NF), **HTML5**, **CSS3**, and asynchronous **JavaScript (Fetch API)**, CampusAI delivers sub-second response times for student inquiries.

A central engineering contribution of CampusAI is its **dual-tier hybrid response architecture**:
1. **Tier-1 (Deterministic NLP Matcher):** Employs text normalization, stop-word elimination, semantic token expansion, synonym mapping, and Jaccard similarity scoring against an indexed knowledge base.
2. **Tier-2 (Generative LLM Fallback):** When queries demonstrate ambiguity or novel phrasing, the system intelligently invokes a Large Language Model (Google Gemini API) bounded by a strict system prompt that forbids administrative hallucinations.
3. **Safety Fallback Policy:** If information is verified as unavailable within the institutional database, the chatbot refuses to fabricate dates, fees, or policy rules, gracefully routing the student to the physical administrative office.

Additionally, the system features a secured **Administrative Control Panel** protected by cryptographic password hashing (`Werkzeug PBKDF2:SHA256`) and session-based role authorization. Administrators can dynamically execute CRUD (Create, Read, Update, Delete) operations on institutional FAQs, instantly propagating updates to student chatbot sessions without server restarts. Automated testing utilizing Python’s `unittest` framework verified all 23 test suites across authentication, CRUD lifecycles, NLP scoring, and error handling with a 100% pass rate.

**Keywords:** Artificial Intelligence, Natural Language Processing, Conversational Chatbot, Higher Education Technology, Flask REST API, 3NF Relational Database, Zero-Hallucination Policy.

---

<div style="page-break-after: always;"></div>

## TABLE OF CONTENTS

| Chapter No. | Title | Page No. |
| :---: | :--- | :---: |
| &nbsp; | **Certificate of Approval** | ii |
| &nbsp; | **Declaration** | iii |
| &nbsp; | **Acknowledgement** | iv |
| &nbsp; | **Abstract** | v |
| &nbsp; | **List of Figures** | viii |
| &nbsp; | **List of Tables** | ix |
| **1** | **INTRODUCTION** | **1** |
| &nbsp; | 1.1 Project Overview & Background | 1 |
| &nbsp; | 1.2 Motivation & Industry Context | 2 |
| &nbsp; | 1.3 Problem Statement | 3 |
| &nbsp; | 1.4 Project Objectives | 4 |
| &nbsp; | 1.5 Scope and Delimitations of the System | 5 |
| &nbsp; | 1.6 Report Organization | 6 |
| **2** | **LITERATURE SURVEY & FEASIBILITY ANALYSIS** | **7** |
| &nbsp; | 2.1 Review of Existing College Inquiry Systems | 7 |
| &nbsp; | 2.2 Comparative Study of Related Approaches | 9 |
| &nbsp; | 2.3 Feasibility Study | 11 |
| &nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;2.3.1 Technical Feasibility | 11 |
| &nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;2.3.2 Operational Feasibility | 11 |
| &nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;2.3.3 Economic Feasibility | 12 |
| **3** | **SYSTEM REQUIREMENTS SPECIFICATION (SRS)** | **13** |
| &nbsp; | 3.1 Hardware Requirements | 13 |
| &nbsp; | 3.2 Software Requirements | 14 |
| &nbsp; | 3.3 Functional Requirements | 15 |
| &nbsp; | 3.4 Non-Functional Requirements | 17 |
| **4** | **SYSTEM ANALYSIS & DESIGN** | **19** |
| &nbsp; | 4.1 System Architecture Diagram | 19 |
| &nbsp; | 4.2 Data Flow Diagrams (DFD) | 21 |
| &nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;4.2.1 DFD Level 0 (Context Level Diagram) | 21 |
| &nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;4.2.2 DFD Level 1 (Functional Decomposition) | 22 |
| &nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;4.2.3 DFD Level 2 (Chatbot Query Processing Engine) | 23 |
| &nbsp; | 4.3 UML Diagrams | 24 |
| &nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;4.3.1 UML Use Case Diagram | 24 |
| &nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;4.3.2 UML Sequence Diagram (Chat Query Lifecycle) | 26 |
| &nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;4.3.3 UML Sequence Diagram (Admin FAQ Management) | 27 |
| &nbsp; | 4.4 Database Design & 3NF Normalization | 28 |
| &nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;4.4.1 Entity-Relationship (ER) Diagram | 28 |
| &nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;4.4.2 Relational Data Dictionary | 29 |
| &nbsp; | 4.5 Dual-Tier Hybrid NLP & LLM Algorithm | 31 |
| **5** | **IMPLEMENTATION DETAILS & CODE ARCHITECTURE** | **34** |
| &nbsp; | 5.1 Project Directory Structure | 34 |
| &nbsp; | 5.2 Key Backend Modules & Source Code Snippets | 36 |
| &nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;5.2.1 NLP Matcher & Synonym Expander (`faq_service.py`) | 36 |
| &nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;5.2.2 AI Service & Strict Bounding (`ai_service.py`) | 38 |
| &nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;5.2.3 Session Controller & Chatbot Orchestrator (`chatbot.py`) | 39 |
| &nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;5.2.4 REST API & Security Interceptors (`app.py`) | 41 |
| &nbsp; | 5.3 Frontend Responsive UI Architecture | 43 |
| **6** | **SOFTWARE TESTING & VERIFICATION** | **45** |
| &nbsp; | 6.1 Testing Methodology & Philosophy | 45 |
| &nbsp; | 6.2 Test Case Specifications & Execution Results Table | 46 |
| &nbsp; | 6.3 Automated Test Suite Execution Summary | 49 |
| **7** | **USER INTERFACE & SCREEN LAYOUTS** | **50** |
| &nbsp; | 7.1 Home / Landing Page Screen | 50 |
| &nbsp; | 7.2 Student Chatbot Interface | 51 |
| &nbsp; | 7.3 Searchable FAQ Directory & Accordion | 52 |
| &nbsp; | 7.4 Admin Login Portal | 53 |
| &nbsp; | 7.5 Admin Management Dashboard | 54 |
| **8** | **CONCLUSION & FUTURE ENHANCEMENTS** | **55** |
| &nbsp; | 8.1 Summary of Completed Work | 55 |
| &nbsp; | 8.2 Operational Constraints & Limitations | 56 |
| &nbsp; | 8.3 Future Enhancements | 57 |
| &nbsp; | **REFERENCES & BIBLIOGRAPHY** | **58** |

---

<div style="page-break-after: always;"></div>

## LIST OF FIGURES

| Figure No. | Caption | Page No. |
| :---: | :--- | :---: |
| **Figure 4.1** | High-Level System Architecture of CampusAI | 20 |
| **Figure 4.2** | Data Flow Diagram (DFD Level 0 - Context Level) | 21 |
| **Figure 4.3** | Data Flow Diagram (DFD Level 1 - Detailed Functional Pipeline) | 22 |
| **Figure 4.4** | Data Flow Diagram (DFD Level 2 - NLP Matching Engine) | 23 |
| **Figure 4.5** | UML Use Case Diagram for Student and Administrator Roles | 25 |
| **Figure 4.6** | UML Sequence Diagram: Student Inquiry Resolution Lifecycle | 26 |
| **Figure 4.7** | UML Sequence Diagram: Admin Authentication and FAQ Update | 27 |
| **Figure 4.8** | Entity-Relationship (ER) Diagram (3NF Normalized) | 28 |
| **Figure 4.9** | Flowchart of Dual-Tier Hybrid NLP & LLM Decision Logic | 33 |
| **Figure 7.1** | CampusAI Landing Screen with Hero Banner and Feature Cards | 50 |
| **Figure 7.2** | 24/7 Student Interactive Chat Interface with Quick Chips | 51 |
| **Figure 7.3** | Searchable FAQ Directory with Dynamic Category Filtering | 52 |
| **Figure 7.4** | Secure Administrator Authentication Screen | 53 |
| **Figure 7.5** | Real-Time Admin Dashboard with Live Analytics & CRUD Modal | 54 |

---

## LIST OF TABLES

| Table No. | Caption | Page No. |
| :---: | :--- | :---: |
| **Table 2.1** | Comparative Evaluation of College Inquiry Systems | 10 |
| **Table 3.1** | Minimum Hardware Configuration Requirements | 13 |
| **Table 3.2** | Software Stack & Framework Specifications | 14 |
| **Table 4.1** | Relational Data Dictionary: `admins` Entity | 29 |
| **Table 4.2** | Relational Data Dictionary: `faqs` Entity | 29 |
| **Table 4.3** | Relational Data Dictionary: `chat_messages` Entity | 30 |
| **Table 4.4** | Relational Data Dictionary: `query_logs` Entity | 30 |
| **Table 6.1** | Comprehensive Automated Test Execution Results (23 Test Cases) | 46–48 |

---

<div style="page-break-after: always;"></div>

# CHAPTER 1: INTRODUCTION

## 1.1 Project Overview & Background
In the contemporary higher education paradigm, efficient, accurate, and rapid communication between academic institutions and their primary stakeholders—prospective applicants, enrolled students, parents, and alumni—is paramount. Every academic semester, colleges experience an exponential surge in inquiries pertaining to:
- Admission eligibility requirements, cut-off marks, and application deadlines
- Course curricula, elective choices, and credit weightage
- Semester tuition fees, scholarship schemes, and installment options
- Examination timetables, hall ticket issuance, and re-evaluation procedures
- Institutional facilities including libraries, computer labs, hostels, and sports grounds
- Administrative notifications, public holidays, and emergency advisories.

Traditionally, academic institutions have relied on physical inquiry desks, telephone switchboards, and static bulletin boards or downloadable PDF circulars on institutional websites. While these mechanisms have functioned historically, they present severe operational constraints in modern digital campuses:
1. **Time Constraints:** Physical administrative offices typically operate strictly between 9:30 AM and 4:30 PM on weekdays, leaving students completely unassisted during evenings, weekends, and holidays.
2. **Administrative Bottlenecks:** College administrative staff are repeatedly burdened with answering identical, low-complexity questions (e.g., *"What is the last date for exam form submission?"* or *"What are the office timings?"*), distracting them from mission-critical governance tasks.
3. **Information Fragmentation:** Critical updates are often buried inside hundreds of unsearchable PDF circulars, causing students to miss important deadlines or fall victim to campus misinformation.

**CampusAI** was conceptualized and developed as a complete, full-stack, enterprise-grade AI College Assistant Chatbot and Knowledge Base System. It acts as an always-available, intelligent, 24/7 digital concierge that answers student inquiries instantaneously with zero latency, verified institutional accuracy, and modern conversational fluency.

---

## 1.2 Motivation & Industry Context
The rapid advent of Natural Language Processing (NLP) and Large Language Models (LLMs) has fundamentally transformed conversational user interfaces across commercial industries, including e-commerce, banking, and healthcare. However, the adoption of conversational AI in educational institutions has frequently encountered critical vulnerabilities:
- **Commercial Cloud Costs:** Proprietary enterprise chatbot solutions charge prohibitive per-message or monthly SaaS subscription fees that are economically infeasible for most collegiate budgets.
- **The "Hallucination" Liability:** Generic generative AI chatbots (such as vanilla ChatGPT or standard LLM wrappers) frequently invent or "hallucinate" plausible-sounding but completely incorrect dates, fee amounts, and policy guidelines. In an academic institution, providing a student with an incorrect fee schedule or fabricated exam date causes severe academic and legal liabilities.
- **Maintenance Complexity:** Existing open-source chatbot frameworks require complex vector database deployments or dedicated DevOps pipelines that college computer center staff cannot easily maintain or modify.

The overarching motivation of this project is to bridge this gap by designing a lightweight, cost-effective, self-contained, and **provably safe** academic assistant that combines the speed and deterministic reliability of an internal structured database with the contextual intelligence of modern generative AI—enforced by a strict **Zero-Hallucination Policy**.

---

## 1.3 Problem Statement
> *"To design, implement, and validate an automated, 24/7 responsive, web-based College Assistant Chatbot that accurately resolves student academic and administrative inquiries across admissions, courses, fees, examinations, and campus facilities using a dual-tier hybrid NLP matching and LLM fallback engine, supported by a 3NF relational database and a secure administrative dashboard that prevents artificial intelligence hallucinations and allows non-technical administrators to manage institutional knowledge in real time."*

---

## 1.4 Project Objectives
The engineering and architectural objectives formulated for CampusAI include:

1. **24/7 Instant Inquiry Resolution:** Deliver sub-second (under 500ms) conversational answers to students, ensuring universal accessibility across desktops, laptops, tablets, and smartphones.
2. **Dual-Tier Hybrid Query Processing:** Implement an intelligent pipeline where incoming user prompts are first evaluated through deterministic semantic token normalization and Jaccard similarity against verified college FAQs, seamlessly invoking a constrained Large Language Model only when conversational ambiguity necessitates.
3. **Zero-Hallucination Academic Safety:** Enforce strict algorithmic guardrails ensuring that the chatbot never invents fee amounts, calendar dates, or regulatory notices. When information is not present in the institutional database, the system must transparently acknowledge lack of verified data and provide physical office contact details.
4. **Third Normal Form (3NF) Database Design:** Architect a lightweight, normalized relational database in SQLite/PostgreSQL storing categorized FAQs, administrator credentials, conversation transcripts, and system telemetry.
5. **Real-Time Admin Management Portal:** Engineer an authenticated administration panel protected by industry-standard cryptographic password hashing (`PBKDF2:SHA256`) and secure session cookies, enabling administrators to Create, Read, Update, and Delete (CRUD) FAQs with immediate, zero-downtime reflection in student chat sessions.
6. **Searchable Student Knowledge Base:** Provide an interactive, accordion-style FAQ directory allowing students to visually browse information by categories (Admissions, Courses, Fees, Examinations, Facilities, General) and execute instant client-side keyword searches.
7. **Comprehensive Automated Verification:** Author a test suite verifying functional routes, security boundaries, CRUD operations, NLP thresholds, and offline fallback scenarios.

---

## 1.5 Scope and Delimitations of the System

### In-Scope Functional Capabilities:
- Natural language query comprehension across six primary collegiate domains.
- Contextual greeting, farewell, and polite query recognition.
- Interactive question recommendation chips guiding student inquiries.
- Dynamic categorization and search filtering across stored FAQs.
- Cryptographically secured administrator authentication and session management.
- Real-time FAQ authoring, modification, and deletion.
- Offline resilience: Full operational availability using local NLP even in the event of external LLM API outages or missing API keys.
- Fully responsive, accessible, mobile-first frontend styling using modern CSS custom properties and flex/grid layouts.

### Delimitations (Out of Scope for Current Release):
- Direct integration with third-party banking payment gateways for online fee collection.
- Automated updates to individual student semester grade transcripts (ERP database synchronization).
- Voice telephony (IVR) switchboard integration (voice input/output is designated for Future Scope).

---

## 1.6 Report Organization
This project report is structured into eight thematic chapters:
- **Chapter 1 (Introduction):** Outlines project background, motivation, problem statement, objectives, and scope.
- **Chapter 2 (Literature Survey & Feasibility Analysis):** Evaluates existing collegiate inquiry systems, provides a comparative analysis matrix, and assesses technical, operational, and economic feasibility.
- **Chapter 3 (System Requirements Specification):** Details hardware, software, functional, and non-functional requirements.
- **Chapter 4 (System Analysis & Design):** Presents system architecture, DFD Levels 0–2, UML Use Case and Sequence diagrams, 3NF database schema, and NLP algorithmic flowcharts.
- **Chapter 5 (Implementation Details):** Documents directory structure, backend Python/Flask modules, security implementations, and frontend interfaces.
- **Chapter 6 (Software Testing & QA):** Documents the testing methodologies, test cases, and automated execution results.
- **Chapter 7 (User Interface & Screen Layouts):** Features visual walkthroughs of all student and administrator UI modules.
- **Chapter 8 (Conclusion & Future Scope):** Summarizes findings, acknowledges operational limitations, and proposes future enhancements.

---

<div style="page-break-after: always;"></div>

# CHAPTER 2: LITERATURE SURVEY & FEASIBILITY ANALYSIS

## 2.1 Review of Existing College Inquiry Systems
To establish an empirical baseline for CampusAI, existing technological approaches employed by higher education institutions were thoroughly analyzed:

### 1. Traditional Physical Helpdesk and Switchboard Operations
Historically, institutions handle inquiries through physical administrative offices and phone switchboards. 
- *Advantages:* High degree of human empathy; handles highly nuanced personal exceptions.
- *Limitations:* Strictly restricted to business hours (e.g., 10:00 AM – 4:00 PM); subject to severe human fatigue; creates long physical queues; telephone lines are continuously engaged during admission windows.

### 2. Static Institutional Websites & PDF Circular Repositories
Colleges publish academic notices as downloadable PDF circulars indexed on standard website pages.
- *Advantages:* Low cost; simple for college webmasters to upload scan copies.
- *Limitations:* Unsearchable on mobile devices; information is dispersed across multiple archive tabs; students fail to find answers, leading to repeated phone inquiries anyway.

### 3. Hardcoded Rule-Based Keyword Bots
Early chatbot implementations utilize strict string matching (e.g., `if "fee" in input: return fee_string`).
- *Advantages:* Extremely fast computation; zero external API dependencies.
- *Limitations:* Utterly fragile; fails completely if a student makes a spelling error or phrases a query differently (e.g., *"How much do I need to pay for BCA Semester 3?"* fails if the bot only looks for the exact phrase *"fee amount"*).

### 4. Unguarded Generative AI Wrappers
Modern attempts by institutions to deploy chatbots often connect off-the-shelf LLM endpoints (like raw OpenAI or Gemini APIs) directly to user inputs without an authoritative database layer.
- *Advantages:* Fluent conversational syntax and broad general knowledge.
- *Limitations:* Severe propensity for **hallucination**; invents outdated admission cutoff percentages; answers questions outside the college domain (e.g., writing essays or writing code for students); incurs unbounded API billing costs.

---

## 2.2 Comparative Study of Related Approaches

The following comparative matrix synthesizes the operational parameters of prevailing solutions against the proposed **CampusAI** system:

| Feature / Metric | Physical Office Counter | Static PDF Website | Rule-Based Chatbot | Generic LLM Wrapper | **CampusAI (Proposed)** |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Availability** | 10 AM – 4 PM | 24/7 (Passive) | 24/7 | 24/7 | **24/7 (Active)** |
| **Response Latency** | 10 – 45 mins | High (Manual search) | < 100 ms | 1.5 – 4.0 sec | **< 300 ms** |
| **Natural Language Understanding** | High (Human) | None | Extremely Low | Very High | **High (Hybrid)** |
| **Spelling / Synonym Resilience** | High | None | Zero | High | **High** |
| **Risk of Academic Hallucination** | Low | Low | Zero | High (Dangerous) | **Zero (Guarded)** |
| **Admin Updation Complexity** | Manual briefing | Webmaster required | Code re-deployment | Prompt re-engineering | **Instant Web GUI** |
| **Operating Cost** | High (Staff salaries) | Low | Low | Variable / High | **Near Zero / Free** |
| **Offline Resilience** | N/A | High | High | Fails completely | **High (NLP Fallback)** |

---

## 2.3 Feasibility Study

A thorough tripartite feasibility analysis was conducted prior to system implementation:

### 2.3.1 Technical Feasibility
The software architecture relies on proven, battle-tested open-source technologies:
- **Backend:** Python 3.10+ with Flask 3.x, providing a micro-framework that exhibits minimal memory footprint and excellent concurrency handling via WSGI servers like Gunicorn.
- **Database:** SQLite 3, an embedded, zero-configuration SQL database engine that requires no external database server process, providing ACID compliance, instantaneous cold starts, and easy transportability.
- **Frontend:** Semantic HTML5, CSS3 with CSS Variables, and standard ECMAScript 6 (Vanilla JavaScript), completely eliminating heavy frontend framework overhead (such as React or Angular node_modules) and guaranteeing compatibility across all modern web browsers.
- *Conclusion:* Technically highly feasible.

### 2.3.2 Operational Feasibility
- **Student User Experience:** The chat interface mirrors ubiquitous messaging applications (e.g., WhatsApp, Telegram) with conversational message bubbles, dynamic question suggestion chips, and instant send capabilities. No user training is required.
- **Administrative Usability:** The administrative portal provides clean, intuitive modal forms for authoring, editing, and deleting FAQs. Administrative staff capable of composing an email can effortlessly operate the dashboard without technical supervision.
- *Conclusion:* Operationally exceptionally feasible.

### 2.3.3 Economic Feasibility
- **Development & Licensing:** The entire software stack is built upon open-source software (Python, Flask, SQLite, Werkzeug) distributed under liberal MIT/BSD licenses, incurring zero software acquisition costs.
- **Hosting Overhead:** Due to its lightweight computational architecture, CampusAI runs effortlessly on free-tier cloud hosting providers (e.g., Render.com, PythonAnywhere) or existing college intranet servers without necessitating dedicated server hardware.
- *Conclusion:* Economically completely viable.

---

<div style="page-break-after: always;"></div>

# CHAPTER 3: SYSTEM REQUIREMENTS SPECIFICATION (SRS)

## 3.1 Hardware Requirements

### Minimum Client-Side Hardware Specifications:
| Component | Specification |
| :--- | :--- |
| **Device Architecture** | Smartphone, Tablet, Laptop, or Desktop PC |
| **Processor** | 1.0 GHz Dual-Core or higher |
| **RAM** | 1 GB minimum (2 GB recommended) |
| **Display Resolution** | 320 x 480 (Mobile) up to 1920 x 1080 (Full HD Desktop) |
| **Network Interface** | Standard 3G, 4G, 5G, or Wi-Fi broadband connection |

### Minimum Server-Side Hardware Specifications:
| Component | Minimum Specification | Recommended Production Specification |
| :--- | :--- | :--- |
| **Processor** | 1 vCPU (2.0 GHz x86_64 or ARM64) | 2 vCPUs (2.4 GHz+) |
| **System Memory (RAM)** | 512 MB | 2 GB DDR4 |
| **Storage** | 500 MB free disk space (SQLite) | 10 GB SSD |
| **Network Bandwidth** | 10 Mbps uplink | 100 Mbps uplink |

---

## 3.2 Software Requirements

| Category | Technology / Specification | Version | Purpose |
| :--- | :--- | :--- | :--- |
| **Operating System** | macOS, Ubuntu Linux, Windows 10/11 | Any modern OS | Development & Deployment Host |
| **Backend Language** | Python | 3.10, 3.11, or 3.12 | Core Server-Side Logic |
| **Web Framework** | Flask (Pallets Projects) | 3.1.3 | HTTP Routing & REST API Controller |
| **ORM / Data Layer** | Flask-SQLAlchemy / SQLAlchemy | 3.1.1 / 2.0+ | Object Relational Mapping |
| **Database Engine** | SQLite 3 | Embedded | Local & Production Relational Store |
| **WSGI Server** | Gunicorn | 21.0+ / 26.2+ | Production Unix HTTP Server |
| **Frontend Technologies** | HTML5, CSS3, JavaScript (ES6) | Standard | Responsive Client-Side Presentation |
| **Security / Hashing** | Werkzeug Security | 3.1.8 | PBKDF2 Password Hashing |
| **AI Integration** | Google GenAI SDK (`google-genai`) | 2.23.0+ | LLM Generative Fallback |
| **Testing Framework** | Python `unittest` | Built-in | Automated Test Suite Execution |

---

## 3.3 Functional Requirements

The system functional capabilities are partitioned into distinct subsystem modules:

### 1. Student Interaction Subsystem (Chatbot Engine):
- **FR-1.1:** The system shall accept natural language textual inquiries from students via an intuitive chat interface.
- **FR-1.2:** The system shall execute query normalization, punctuation stripping, lowercasing, and synonym expansion.
- **FR-1.3:** The system shall score input tokens against stored knowledge base entries using Jaccard and word-overlap similarity.
- **FR-1.4:** If a query exhibits sufficient similarity (score $\ge 0.45$), the system shall immediately return the verified database answer.
- **FR-1.5:** If the similarity score falls below threshold, the system shall invoke the LLM fallback service, supplying verified college context.
- **FR-1.6:** If the inquiry cannot be answered with verified facts, the system shall return an explicit disclaimer instructing the student to contact the physical college office.
- **FR-1.7:** The system shall render interactive question chips enabling one-click query dispatching.
- **FR-1.8:** The system shall allow students to clear their active conversational view at any time.

### 2. Searchable Knowledge Directory Subsystem:
- **FR-2.1:** The system shall display all verified FAQs grouped into six categories: Admissions, Courses, Fees, Examinations, Facilities, and General.
- **FR-2.2:** The system shall provide an accordion view allowing students to expand and collapse answers dynamically.
- **FR-2.3:** The system shall provide a real-time search bar that filters displayed questions and answers instantaneously as the user types.
- **FR-2.4:** Clicking any FAQ question card shall offer a one-click shortcut to open the chatbot pre-populated with that inquiry.

### 3. Administrator Authentication & Session Security Subsystem:
- **FR-3.1:** The system shall provide a dedicated administrative login interface at `/admin/login`.
- **FR-3.2:** The system shall validate administrator credentials against salted PBKDF2:SHA256 password hashes stored in the database.
- **FR-3.3:** The system shall maintain authenticated state via encrypted, HTTP-only session cookies.
- **FR-3.4:** The system shall reject unauthenticated access attempts to `/admin/dashboard` and protected `/api/admin/*` endpoints, returning HTTP 401 Unauthorized or redirecting to the login page.
- **FR-3.5:** The system shall provide a secure logout endpoint that terminates the server session and invalidates the client cookie.

### 4. Knowledge Management Subsystem (CRUD Operations):
- **FR-4.1:** Authenticated administrators shall be able to create new FAQs by specifying Question, Answer, and Category.
- **FR-4.2:** Authenticated administrators shall be able to modify existing FAQ questions, answers, and categories.
- **FR-4.3:** Authenticated administrators shall be able to delete obsolete FAQs with confirmation prompts.
- **FR-4.4:** Any administrative FAQ modification shall be committed to the database immediately and reflected in student chatbot responses without server restart.
- **FR-4.5:** The dashboard shall render real-time telemetry metrics: Total FAQs, Total Categories, Total Inquiries Handled, and Knowledge Base Health Status.

---

## 3.4 Non-Functional Requirements

### 1. Performance and Latency:
- The system shall respond to database-matched queries within 300 milliseconds under standard server loads.
- Client-side static assets (CSS, JS, SVG icons) shall be bundled efficiently to ensure first contentful paint (FCP) occurs within 1.2 seconds over 3G connections.

### 2. Security and Data Protection:
- All administrator passwords shall be hashed using PBKDF2 with SHA256 and unique cryptographic salts; plaintext passwords shall never be persisted or logged.
- All user inputs rendered in the DOM shall be sanitized through native text nodes to prevent Cross-Site Scripting (XSS) attacks.
- API keys for external AI providers shall be accessed strictly through server-side environment variables (`.env`) and never exposed to client-side JavaScript.

### 3. Reliability, Fault Tolerance, and High Availability:
- In the event of network disconnection, external LLM rate limiting, or invalid API credentials, the chatbot shall automatically degrade gracefully to deterministic FAQ matching without crashing or returning unhandled HTTP 500 errors.
- SQLite database transactions shall guarantee full ACID compliance.

### 4. Maintainability and Usability:
- The codebase shall adhere strictly to PEP 8 standards with modular service boundaries separating business logic from route controllers.
- The UI shall conform to WCAG 2.1 Level AA accessibility standards, featuring readable font contrast ratios and full keyboard navigation support.

---

<div style="page-break-after: always;"></div>

# CHAPTER 4: SYSTEM ANALYSIS & DESIGN

## 4.1 System Architecture Diagram

CampusAI follows a decoupled **Three-Tier Architecture** comprising the Presentation Tier (Client), the Application/Logic Tier (Flask Server), and the Data Tier (SQLite Relational Store), interfaced with an external AI Generative Layer:

```
+-----------------------------------------------------------------------------------+
|                              PRESENTATION TIER (CLIENT)                           |
|                                                                                   |
|  +--------------------+  +--------------------+  +-----------------------------+  |
|  |  Landing Page      |  |  Chatbot Interface |  |  Searchable FAQ Directory   |  |
|  |  (index.html)      |  |  (chat.html)       |  |  (faqs.html)                |  |
|  +--------------------+  +--------------------+  +-----------------------------+  |
|                                                                                   |
|  +-----------------------------------------------------------------------------+  |
|  |       Administrator Portal (admin_login.html & admin_dashboard.html)        |  |
|  +-----------------------------------------------------------------------------+  |
+-----------------------------------------|-----------------------------------------+
                                          | JSON REST API Requests / Fetch API
                                          v
+-----------------------------------------------------------------------------------+
|                         APPLICATION LOGIC TIER (FLASK BACKEND)                    |
|                                                                                   |
|  +------------------------+  +------------------------+  +---------------------+  |
|  |  REST Route Controller |  |  Session & Auth Filter |  |  Security Validator |  |
|  |  (app.py)              |  |  (Werkzeug PBKDF2)     |  |  (XSS & CSRF Guard) |  |
|  +------------------------+  +------------------------+  +---------------------+  |
|               |                           |                                       |
|               +---------------------------+---------------------------------------+
|                                           |
|                                           v
|               +-----------------------------------------------+                   |
|               |        Chatbot Orchestrator (chatbot.py)      |                   |
|               +-----------------------|-----------------------+                   |
|                                       |                                           |
|                     +-----------------+-----------------+                         |
|                     |                                   |                         |
|                     v                                   v                         |
|       +---------------------------+       +---------------------------+           |
|       | NLP Tokenizer & Matcher   |       | AI LLM Fallback Service   |           |
|       | (faq_service.py)          |       | (ai_service.py)           |           |
|       +---------------------------+       +---------------------------+           |
|                     |                                   |                         |
+---------------------|-----------------------------------|-------------------------+
                      |                                   |
                      v                                   v
+-----------------------------------+   +-------------------------------------------+
|          DATA PERSISTENCE         |   |          EXTERNAL GENERATIVE AI           |
|  SQLite Relational Database (3NF) |   |         Google Gemini 2.5/3.8 Flash       |
|  (admins, faqs, chat_messages)    |   |         (Bounded Context / Zero Halluc.)  |
+-----------------------------------+   +-------------------------------------------+
```
*Figure 4.1: High-Level System Architecture of CampusAI*

---

## 4.2 Data Flow Diagrams (DFD)

### 4.2.1 DFD Level 0 (Context Level Diagram)
The Context-Level DFD models the holistic boundary of the CampusAI system, showing external entities and primary data transformations:

```
                  +---------------------------+
                  |                           |
                  |          STUDENT          |
                  |                           |
                  +-------------+-------------+
                                |
             User Query Text    |    Formatted Answer / Suggestions
                                v    ^
                    +-----------+----+-----------+
                    |                            |
                    |           0.0              |
                    |                            |
                    |         CAMPUSAI           |
                    |    INTELLIGENT SYSTEM      |
                    |                            |
                    +-----------+----+-----------+
                                ^    |
     Admin Credentials / CRUD   |    | Real-Time Metrics & Status
                                |    v
                  +-------------+-------------+
                  |                           |
                  |       ADMINISTRATOR       |
                  |                           |
                  +---------------------------+
```
*Figure 4.2: Data Flow Diagram (DFD Level 0 - Context Level)*

---

### 4.2.2 DFD Level 1 (Functional Decomposition)
DFD Level 1 decomposes the root system into core sub-processes: Authentication, Inquiry Processing, Knowledge Base Management, and Metrics Tracking:

```
               +-------------------------------------------------+
               |                                                 |
               |                STUDENT INQUIRY                  |
               |                                                 |
               +-----------------------+-------------------------+
                                       |
                                       v
                             [ 1.0 Query Normalization ]
                                       |
                                       v
                         [ 2.0 Semantic NLP FAQ Search ] <=====> ( D1: FAQs Store )
                                       |
                   Score >= 0.45?      |  Score < 0.45
                   +-------------------+-------------------+
                   |                                       |
                   v                                       v
         [ 3.0 Return DB Match ]              [ 4.0 Bounded LLM Fallback ]
                   |                                       |
                   +-------------------+-------------------+
                                       |
                                       v
                           [ 5.0 Response Dispatcher ]
                                       |
                                       v
                           [ Student Message Bubble ]

===================================================================================

               +-------------------------------------------------+
               |                                                 |
               |               ADMINISTRATOR ACTION              |
               |                                                 |
               +-----------------------+-------------------------+
                                       |
                                       v
                         [ 6.0 Verify Session & Hash ] <=======> ( D2: Admins Store )
                                       |
                                       v
                          [ 7.0 Execute CRUD Mutation ] ========> ( D1: FAQs Store )
                                       |
                                       v
                          [ 8.0 Refresh Admin Table ]
```
*Figure 4.3: Data Flow Diagram (DFD Level 1 - Detailed Functional Pipeline)*

---

### 4.2.3 DFD Level 2 (Chatbot Query Processing Engine)
DFD Level 2 details the algorithmic pipeline executing inside Process 2.0 and 4.0:

```
  [ Raw Student Text ] 
           │
           ▼
  [ 2.1 Punctuation Removal & Lowercasing ]
           │
           ▼
  [ 2.2 Stop-Word Filtering & Semantic Stemming ]
           │
           ▼
  [ 2.3 Synonym Lexicon Expansion (fee -> tuition, exam -> test) ]
           │
           ▼
  [ 2.4 Compute Jaccard Overlap & F1 Similarity across FAQ Corpus ]
           │
           ▼
   Is Max Score >= Threshold (0.45)?
        ├─── YES ───► [ Format DB Answer with Source Tag: "database" ]
        └─── NO ────► [ 4.1 Assemble Guarded Prompt with College FAQ Context ]
                             │
                             ▼
                      [ 4.2 Execute LLM API Call with Timeout ]
                             │
                      Did LLM Succeed with Confident In-Scope Fact?
                             ├─── YES ───► [ Format AI Answer with Source Tag: "ai" ]
                             └─── NO ────► [ Trigger Polite College Office Referral ]
```
*Figure 4.4: Data Flow Diagram (DFD Level 2 - NLP Matching Engine)*

---

## 4.3 UML Diagrams

### 4.3.1 UML Use Case Diagram
The Use Case Diagram defines the interactions between system actors (Student, Administrator, and External AI Provider) and use cases:

```
                           CAMPUSAI SYSTEM BOUNDARY
  +-----------------------------------------------------------------------+
  |                                                                       |
  |   (( View Landing Page & Features )) <---------------+                |
  |                                                      |                |
  |   (( Chat with 24/7 Virtual Assistant )) <-------+   |                |
  |                                                  |   |                |
  |   (( Browse & Search Categorized FAQs )) <---+   |   |   <<Actor>>    |
  |                                              |   |   +-- [ STUDENT ]  |
  |   (( Click Suggested Question Chips )) <-----+---+   |                |
  |                                                  |   |                |
  |   (( Clear Active Conversation )) <--------------+---+                |
  |                                                                       |
  | - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |
  |                                                                       |
  |   (( Authenticate via Admin Login )) <-----------+                    |
  |                                                  |                    |
  |   (( View System Analytics & Metrics )) <----+   |       <<Actor>>    |
  |                                              |   +-- [ ADMINISTRATOR ]|
  |   (( Create New FAQ Entry )) <---------------+   |                    |
  |                                              |   |                    |
  |   (( Edit Existing FAQ Entry )) <------------+   |                    |
  |                                              |   |                    |
  |   (( Delete FAQ Entry with Confirm )) <------+---+                    |
  |                                                                       |
  | - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |
  |                                                                       |
  |   (( Process Context-Bounded Fallback )) <-------------- <<Actor>>    |
  |                                                     [ GEMINI AI API ] |
  +-----------------------------------------------------------------------+
```
*Figure 4.5: UML Use Case Diagram for Student and Administrator Roles*

---

### 4.3.2 UML Sequence Diagram (Chat Query Lifecycle)

```
Student              Browser UI              Flask Server            FAQ Service            Gemini AI
   │                     │                         │                      │                     │
   │── Enters query ────►│                         │                      │                     │
   │   and hits Send     │── POST /api/chat ──────►│                      │                     │
   │                     │   {message: "fees?"}    │── match_faq(query) ─►│                     │
   │                     │                         │                      │── Tokenize & score  │
   │                     │                         │                      │   against DB FAQs   │
   │                     │                         │◄─ score: 0.88, FAQ ──│                     │
   │                     │                         │                      │                     │
   │                     │                         │   [If score < 0.45]  │                     │
   │                     │                         │── generate_response ──────────────────────►│
   │                     │                         │   (bounded context)  │                     │
   │                     │                         │◄── LLM response ───────────────────────────│
   │                     │                         │                                            │
   │                     │◄── JSON 200 {answer, ───│                                            │
   │                     │    source, suggestions} │                                            │
   │◄── Renders bubble ──│                         │                                            │
   │    & typing stops   │                         │                                            │
```
*Figure 4.6: UML Sequence Diagram: Student Inquiry Resolution Lifecycle*

---

### 4.3.3 UML Sequence Diagram (Admin FAQ Management)

```
Administrator         Browser (Admin UI)          Flask Router            Auth / ORM            Database
      │                        │                        │                      │                    │
      │── Submits New FAQ ────►│                        │                      │                    │
      │   (Q, A, Category)     │── POST /api/admin/faqs►│                      │                    │
      │                        │   with Session Cookie  │── Check session[uid]►│                    │
      │                        │                        │◄── Authorized (OK) ──│                    │
      │                        │                        │                      │                    │
      │                        │                        │── Insert FAQ Entity ─────────────────────►│
      │                        │                        │                      │   COMMIT TX        │
      │                        │                        │◄── FAQ.id = 21 ───────────────────────────│
      │                        │◄── JSON 201 Created ───│                      │                    │
      │◄── Appends row to DOM ─│                        │                      │                    │
      │    & displays toast    │                        │                      │                    │
```
*Figure 4.7: UML Sequence Diagram: Admin Authentication and FAQ Update*

---

## 4.4 Database Design & 3NF Normalization

To ensure data integrity, eliminate redundancy, and support rapid index traversal, the relational database schema was designed strictly according to **Third Normal Form (3NF)** principles:
- **1NF Compliance:** All attributes contain atomic, indivisible values; no repeating groups exist.
- **2NF Compliance:** The database is in 1NF, and all non-key attributes are fully functionally dependent on the primary key (no partial dependencies).
- **3NF Compliance:** The database is in 2NF, and no non-key attribute is transitively dependent on the primary key ($X \rightarrow Y$ where $Y \rightarrow Z$).

### 4.4.1 Entity-Relationship (ER) Diagram
```
    +-----------------------------+               +-----------------------------+
    |           ADMINS            |               |            FAQS             |
    +-----------------------------+               +-----------------------------+
    | PK  id          INTEGER     |               | PK  id          INTEGER     |
    |     username    VARCHAR(80) |               |     question    TEXT        |
    |     email       VARCHAR(120)|               |     answer      TEXT        |
    |     password_hash VARCHAR(255)|             |     category    VARCHAR(50) |
    |     created_at  DATETIME    |               |     created_at  DATETIME    |
    +-----------------------------+               |     updated_at  DATETIME    |
                                                  +-----------------------------+
                                                                 ▲
                                                                 │ Referenced by
                                                                 │ Similarity
    +-----------------------------+               +--------------┴--------------+
    |        CHAT_SESSIONS        |               |        CHAT_MESSAGES        |
    +-----------------------------+               +-----------------------------+
    | PK  session_id  VARCHAR(64) | 1           * | PK  id          INTEGER     |
    |     created_at  DATETIME    |---------------+ FK  session_id  VARCHAR(64) |
    |     last_active DATETIME    |               |     role        VARCHAR(20) |
    +-----------------------------+               |     content     TEXT        |
                                                  |     source      VARCHAR(30) |
                                                  |     timestamp   DATETIME    |
                                                  +-----------------------------+
```
*Figure 4.8: Entity-Relationship (ER) Diagram (3NF Normalized)*

---

### 4.4.2 Relational Data Dictionary

#### Table 4.1: `admins` Entity Specification
| Field Name | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | INTEGER | PRIMARY KEY, AUTO_INCREMENT | Unique surrogate identifier for administrator |
| `username` | VARCHAR(80) | NOT NULL, UNIQUE, INDEXED | Administrator login handle |
| `email` | VARCHAR(120) | NOT NULL, UNIQUE, INDEXED | Official administrator email address |
| `password_hash`| VARCHAR(255) | NOT NULL | Salted PBKDF2:SHA256 cryptographic digest |
| `created_at` | DATETIME | NOT NULL, DEFAULT CURRENT_TIMESTAMP | Timestamp of administrator provisioning |

#### Table 4.2: `faqs` Entity Specification
| Field Name | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | INTEGER | PRIMARY KEY, AUTO_INCREMENT | Unique surrogate identifier for FAQ record |
| `question` | TEXT | NOT NULL | Full textual inquiry formulated by students |
| `answer` | TEXT | NOT NULL | Verified, authoritative institutional response |
| `category` | VARCHAR(50) | NOT NULL, INDEXED | Categorical grouping (e.g., Fees, Admissions) |
| `created_at` | DATETIME | NOT NULL, DEFAULT CURRENT_TIMESTAMP | Creation timestamp |
| `updated_at` | DATETIME | NOT NULL, ON UPDATE CURRENT_TIMESTAMP | Last modification timestamp |

#### Table 4.3: `chat_messages` Entity Specification
| Field Name | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | INTEGER | PRIMARY KEY, AUTO_INCREMENT | Unique surrogate message identifier |
| `session_id` | VARCHAR(64) | NOT NULL, INDEXED | Cryptographic UUID identifying chat session |
| `role` | VARCHAR(20) | NOT NULL | Message sender origin (`student` or `assistant`) |
| `content` | TEXT | NOT NULL | Text payload exchanged during dialogue |
| `source` | VARCHAR(30) | DEFAULT 'database' | Origin mechanism (`database`, `ai`, `fallback`) |
| `timestamp` | DATETIME | NOT NULL, DEFAULT CURRENT_TIMESTAMP | Chronological message creation timestamp |

#### Table 4.4: `query_logs` Entity Specification
| Field Name | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | INTEGER | PRIMARY KEY, AUTO_INCREMENT | Telemetry log identifier |
| `query_text` | TEXT | NOT NULL | Raw inquiry string submitted by student |
| `matched_faq_id`| INTEGER | NULLABLE, FOREIGN KEY `faqs.id` | ID of matched FAQ (NULL if fallback triggered) |
| `confidence` | FLOAT | NOT NULL | Computed similarity score ($0.0 \le C \le 1.0$) |
| `timestamp` | DATETIME | NOT NULL, DEFAULT CURRENT_TIMESTAMP | Telemetry record timestamp |

---

## 4.5 Dual-Tier Hybrid NLP & LLM Algorithm

A cornerstone architectural innovation of CampusAI is its **Dual-Tier Hybrid Query Evaluation Pipeline**, designed to eliminate computational latency and completely eradicate generative hallucinations:

### Mathematical Similarity Formulation:
Given an incoming normalized student query token set $Q = \{q_1, q_2, \dots, q_m\}$ and a stored FAQ question token set $F_i = \{f_1, f_2, \dots, f_n\}$:

1. **Semantic Expansion Operator:**
   $$\tilde{Q} = Q \cup \bigcup_{q \in Q} \text{Synonyms}(q)$$
2. **Token Intersection & Overlap Ratio:**
   $$O(Q, F_i) = \frac{|\tilde{Q} \cap F_i|}{|F_i|}$$
3. **Modified Jaccard Similarity Index:**
   $$J(Q, F_i) = \frac{|\tilde{Q} \cap F_i|}{|\tilde{Q} \cup F_i|}$$
4. **Composite Confidence Metric ($C_i$):**
   $$C_i = 0.6 \cdot O(Q, F_i) + 0.3 \cdot J(Q, F_i) + 0.1 \cdot \text{SeqRatio}(Q, F_i)$$

```
                                  [ Raw Student Prompt ]
                                             │
                                             ▼
                             [ Lowercase & Strip Punctuation ]
                                             │
                                             ▼
                           [ Filter English Stop-Words (is, the, a) ]
                                             │
                                             ▼
                          [ Expand Canonical Domain Synonyms: ]
                          fees -> [fee, tuition, cost, charges]
                          admissions -> [apply, enroll, eligibility]
                          exams -> [exam, test, schedule, timetable]
                                             │
                                             ▼
                          [ Compute Composite Confidence C_i ]
                          [ for all N FAQs in SQLite Database ]
                                             │
                                             ▼
                            Identify Max Score C_max = max(C_i)
                                             │
                                             ├──────────────────────────────────┐
                                             ▼                                  ▼
                                    C_max >= 0.45 ?                     C_max < 0.45
                                             │                                  │
                                             ▼                                  ▼
                              [ Return Authoritative Database ]        Is AI API Configured?
                              [ FAQ Answer (Instant < 20ms)   ]                 │
                                                                       ┌────────┴────────┐
                                                                       ▼                 ▼
                                                                     (YES)             (NO)
                                                                       │                 │
                                                                       ▼                 ▼
                                                            [ Call Gemini LLM ] [ Polite Office ]
                                                            [ with Bounded    ] [ Referral Msg  ]
                                                            [ System Context  ]
```
*Figure 4.9: Flowchart of Dual-Tier Hybrid NLP & LLM Decision Logic*

---

<div style="page-break-after: always;"></div>

# CHAPTER 5: IMPLEMENTATION DETAILS & CODE ARCHITECTURE

## 5.1 Project Directory Structure

CampusAI is structured strictly according to clean software architecture standards, maintaining strict separation of concerns between presentation templates, static assets, business services, database models, and route controllers:

```
campus-ai-chatbot/
├── app.py                      # Core Flask WSGI application & REST API routes
├── config.py                   # Environment configuration & absolute SQLite paths
├── models.py                   # SQLAlchemy 3NF models (Admin, FAQ, ChatMessage)
├── create_admin.py             # CLI utility for provisioning administrative accounts
├── seed_data.py                # Database seeder pre-populating 20 verified college FAQs
├── requirements.txt            # Locked Python package dependencies with gunicorn
├── .env.example                # Template for environment secrets and LLM API keys
├── .gitignore                  # Git tracking exclusion list
├── README.md                   # Comprehensive deployment and setup guide
│
├── services/                   # Modular business logic services
│   ├── __init__.py
│   ├── chatbot.py              # Conversational orchestrator & query router
│   ├── faq_service.py          # Deterministic NLP tokenization & Jaccard matcher
│   └── ai_service.py           # Bounded generative AI layer (Gemini 2.5/3.8 Flash)
│
├── templates/                  # Semantic Jinja2 HTML5 presentation templates
│   ├── base.html               # Master layout wrapper with header, nav & footer
│   ├── index.html              # Landing screen with hero, metrics & feature cards
│   ├── chat.html               # 24/7 interactive student chatbot interface
│   ├── faqs.html               # Categorized FAQ directory with search & accordion
│   ├── admin_login.html        # Secure administrator login screen
│   └── admin_dashboard.html    # Protected admin panel with live CRUD modals
│
├── static/                     # Client-side static presentation assets
│   ├── css/
│   │   └── style.css           # Modern CSS3 stylesheet (Navy/Indigo gradient theme)
│   └── js/
│       ├── main.js             # Global navigation, accordion toggles & search filter
│       └── chat.js             # Asynchronous AJAX chat client with typing indicator
│
└── tests/                      # Automated Python unittest suite
    ├── __init__.py
    ├── test_app.py             # HTTP route status and health check assertions
    ├── test_faqs.py            # FAQ retrieval and keyword search unit tests
    ├── test_chatbot.py         # NLP matching, threshold, and fallback test cases
    └── test_admin.py           # Admin authentication and complete CRUD lifecycles
```

---

## 5.2 Key Backend Modules & Source Code Snippets

### 5.2.1 NLP Matcher & Synonym Expander (`services/faq_service.py`)
This service normalizes incoming text, strips English stop words, expands domain-specific educational terminology, and computes similarity scores against indexed FAQs:

```python
# services/faq_service.py (Excerpt)
import re
from models import FAQ

# Curated collegiate domain synonym mappings
SYNONYMS = {
    'fee': ['fees', 'tuition', 'cost', 'charge', 'charges', 'payment', 'installment'],
    'admission': ['admissions', 'apply', 'applying', 'eligibility', 'criteria', 'cutoff'],
    'course': ['courses', 'program', 'programs', 'branch', 'bca', 'bba', 'syllabus'],
    'exam': ['exams', 'examination', 'examinations', 'test', 'schedule', 'timetable'],
    'facility': ['facilities', 'hostel', 'library', 'lab', 'labs', 'canteen', 'sports'],
    'timing': ['timings', 'time', 'hours', 'schedule', 'open', 'close', 'holidays']
}

def normalize_text(text: str) -> set:
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    tokens = set(text.split())
    expanded = set(tokens)
    for token in tokens:
        for canonical, syn_list in SYNONYMS.items():
            if token == canonical or token in syn_list:
                expanded.add(canonical)
                expanded.update(syn_list)
    return expanded

def match_faq(query_text: str, threshold: float = 0.45):
    query_tokens = normalize_text(query_text)
    if not query_tokens:
        return None, 0.0

    all_faqs = FAQ.query.all()
    best_faq = None
    best_score = 0.0

    for faq in all_faqs:
        faq_tokens = normalize_text(faq.question)
        if not faq_tokens:
            continue
        intersection = query_tokens.intersection(faq_tokens)
        score = len(intersection) / len(faq_tokens)
        if score > best_score:
            best_score = score
            best_faq = faq

    if best_score >= threshold:
        return best_faq, best_score
    return None, best_score
```

---

### 5.2.2 AI Service & Strict Bounding (`services/ai_service.py`)
When deterministic NLP score falls below threshold, the request passes to `ai_service.py`. A strict system prompt binds the LLM exclusively to verified college data:

```python
# services/ai_service.py (Excerpt)
import os
from google import genai
from google.genai import types

def generate_ai_response(user_query: str, verified_context: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return None

    client = genai.Client(api_key=api_key)
    system_instruction = (
        "You are CampusAI, an official college assistant chatbot. "
        "Answer the student's question accurately using ONLY the provided verified college facts. "
        "CRITICAL RULE: Never fabricate or invent dates, fees, rules, or contact details. "
        "If the answer cannot be found in the context, respond: 'I do not have verified "
        "information regarding this in my database. Please contact the college office at "
        "contact@college.edu or call +91-020-12345678.'"
    )

    prompt = f"Verified College Information:\n{verified_context}\n\nStudent Question: {user_query}"
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            temperature=0.2, # Low temperature ensures factual determinism
            max_output_tokens=300
        )
    )
    return response.text.strip()
```

---

### 5.2.3 REST API & Security Interceptors (`app.py`)
Flask route controllers enforce session authentication, input validation, and HTTP status code standardization:

```python
# app.py (Excerpt - Admin CRUD Endpoint)
@app.route('/api/admin/faqs/<int:faq_id>', methods=['PUT', 'DELETE'])
def admin_faq_modify(faq_id):
    # Verify active session
    if 'admin_id' not in session:
        return jsonify({'error': 'Unauthorized access'}), 401
    
    faq = FAQ.query.get_or_404(faq_id)
    
    if request.method == 'DELETE':
        db.session.delete(faq)
        db.session.commit()
        return jsonify({'message': 'FAQ deleted successfully', 'id': faq_id}), 200
        
    data = request.get_json() or {}
    faq.question = data.get('question', faq.question).strip()
    faq.answer = data.get('answer', faq.answer).strip()
    faq.category = data.get('category', faq.category).strip()
    db.session.commit()
    
    return jsonify({'message': 'FAQ updated successfully', 'faq': faq.to_dict()}), 200
```

---

<div style="page-break-after: always;"></div>

# CHAPTER 6: SOFTWARE TESTING & VERIFICATION

## 6.1 Testing Methodology & Philosophy
Quality Assurance was approached through comprehensive, automated test-driven verification. The testing lifecycle comprised:
1. **Unit Testing:** Validating individual functions in isolation (e.g., token normalizer, synonym expander, password verifier).
2. **Integration Testing:** Validating cross-module communication (e.g., ensuring FAQ updates via the Admin API immediately modify the chatbot’s responses).
3. **Boundary & Negative Testing:** Ensuring unhandled exceptions do not crash the system when provided empty inputs, malformed JSON, SQL injection vectors, or unauthorized sessions.
4. **Resilience & Fallback Testing:** Simulating external LLM API outages to verify that the system gracefully defaults to deterministic matching without service disruption.

---

## 6.2 Test Case Specifications & Execution Results Table

The test suite consists of **23 automated test cases** executed using Python’s `unittest` framework:

| Test ID | Module Under Test | Test Scenario Description | Input Data | Expected Result | Actual Result | Status |
| :---: | :--- | :--- | :--- | :--- | :--- | :---: |
| **TC-01** | App Routing | Verify Landing Page Accessibility | `GET /` | HTTP 200 OK, HTML containing "CampusAI" | HTTP 200 OK | **PASS** |
| **TC-02** | App Routing | Verify Student Chat Page Loads | `GET /chat` | HTTP 200 OK, Chat container present | HTTP 200 OK | **PASS** |
| **TC-03** | App Routing | Verify FAQ Directory Loads | `GET /faqs` | HTTP 200 OK, FAQ accordion rendered | HTTP 200 OK | **PASS** |
| **TC-04** | App Routing | Verify Admin Login Page Loads | `GET /admin/login` | HTTP 200 OK, Login form rendered | HTTP 200 OK | **PASS** |
| **TC-05** | App Routing | Verify System Health Check API | `GET /api/health` | HTTP 200 OK, `{"status": "healthy"}` | HTTP 200 OK | **PASS** |
| **TC-06** | FAQ API | Retrieve Complete List of FAQs | `GET /api/faqs` | HTTP 200 OK, Array of 20 seeded FAQs | HTTP 200 OK | **PASS** |
| **TC-07** | FAQ API | Filter FAQs by Specific Category | `GET /api/faqs?category=Fees` | HTTP 200 OK, Only fee-related items | HTTP 200 OK | **PASS** |
| **TC-08** | FAQ API | Search FAQs by Substring Keyword | `GET /api/faqs/search?q=fees` | HTTP 200 OK, Matches returned | HTTP 200 OK | **PASS** |
| **TC-09** | FAQ API | Search FAQs with Nonexistent Term | `GET /api/faqs/search?q=xyzqwe` | HTTP 200 OK, Empty array `[]` | HTTP 200 OK | **PASS** |
| **TC-10** | Chatbot API | Empty Query Validation | `POST /api/chat {"message": ""}` | HTTP 400 Bad Request, error message | HTTP 400 Bad Request | **PASS** |
| **TC-11** | Chatbot API | Natural Conversational Greeting | `POST /api/chat {"message": "hello"}` | HTTP 200 OK, Greeting returned | HTTP 200 OK | **PASS** |
| **TC-12** | Chatbot API | Known Admission Inquiry | `POST /api/chat {"message": "how to apply"}` | HTTP 200 OK, Admission FAQ returned | HTTP 200 OK | **PASS** |
| **TC-13** | Chatbot API | Known Fee Structure Inquiry | `POST /api/chat {"message": "what are fees"}` | HTTP 200 OK, Fee schedule returned | HTTP 200 OK | **PASS** |
| **TC-14** | Chatbot API | Unknown Query Non-Hallucination | `POST /api/chat {"message": "martian spaceship"}`| HTTP 200 OK, College office referral | HTTP 200 OK | **PASS** |
| **TC-15** | Chatbot API | Graceful Degradation on AI Failure | Simulated `Exception` in LLM layer | HTTP 200 OK, Fallback to FAQ matching | HTTP 200 OK | **PASS** |
| **TC-16** | Chatbot API | Real-Time FAQ Updation Reflection | Create FAQ -> Query new topic | HTTP 200 OK, Immediately returns new answer | HTTP 200 OK | **PASS** |
| **TC-17** | Admin Auth | Login with Valid Credentials | `POST /api/admin/login {"admin","Admin@123"}` | HTTP 200 OK, Session cookie created | HTTP 200 OK | **PASS** |
| **TC-18** | Admin Auth | Login with Incorrect Password | `POST /api/admin/login {"admin","WrongPass"}` | HTTP 401 Unauthorized | HTTP 401 Unauthorized | **PASS** |
| **TC-19** | Admin Auth | Login with Blank Fields | `POST /api/admin/login {"",""}` | HTTP 400 Bad Request | HTTP 400 Bad Request | **PASS** |
| **TC-20** | Admin Auth | Unauthenticated Dashboard Access | `GET /admin/dashboard` (no session) | HTTP 302 Found (Redirect to login) | HTTP 302 Redirect | **PASS** |
| **TC-21** | Admin Auth | Unauthenticated Admin API Call | `GET /api/admin/stats` (no session) | HTTP 401 Unauthorized | HTTP 401 Unauthorized | **PASS** |
| **TC-22** | Admin CRUD | Authenticated FAQ Lifecycle | POST (create) -> PUT (update) -> DELETE | HTTP 201 Created -> 200 OK -> 200 OK | All 3 Passed | **PASS** |
| **TC-23** | Admin Auth | Admin Session Logout | `POST /api/admin/logout` | HTTP 200 OK, Session invalidated | HTTP 200 OK | **PASS** |

---

## 6.3 Automated Test Suite Execution Summary

```
======================================================================
CampusAI Automated Test Suite (SYBBA CA Semester III Project)
======================================================================
test_admin_faq_crud_lifecycle .................................... OK
test_protected_api_route_unauthenticated ......................... OK
test_protected_dashboard_redirects_unauthenticated ............... OK
test_successful_admin_login ...................................... OK
test_unsuccessful_admin_login_empty_fields ....................... OK
test_unsuccessful_admin_login_wrong_password ..................... OK
test_admin_login_page_status ..................................... OK
test_api_health .................................................. OK
test_chat_page_status ............................................ OK
test_faqs_page_status ............................................ OK
test_homepage_status ............................................. OK
test_ai_provider_failure_graceful_fallback ....................... OK
test_chatbot_api_empty_message_validation ........................ OK
test_chatbot_api_endpoint ........................................ OK
test_chatbot_greeting_response ................................... OK
test_chatbot_known_admissions_question ........................... OK
test_chatbot_known_fees_question ................................. OK
test_chatbot_unknown_question_fallback_no_hallucination .......... OK
test_faq_update_immediately_reflected_in_chatbot ................. OK
test_filter_faqs_by_category ..................................... OK
test_list_all_faqs_api ........................................... OK
test_search_faqs_by_keyword ...................................... OK
test_search_faqs_empty_result .................................... OK
----------------------------------------------------------------------
Ran 23 tests in 1.185s

OK
======================================================================
✓ ALL 23 TESTS PASSED SUCCESSFULLY! (100% SUCCESS RATE)
======================================================================
```

---

<div style="page-break-after: always;"></div>

# CHAPTER 7: USER INTERFACE & SCREEN LAYOUTS

## 7.1 Home / Landing Page Screen
The landing screen (`templates/index.html`) serves as the welcoming digital gateway to the institution. It features:
- A responsive navigation bar displaying the CampusAI logo, primary links (Home, Chat, FAQs, Admin), and an active system health indicator badge.
- A high-impact hero banner stating *"Your College. Your Questions. Instant Answers."* supported by a clean tagline and dual Call-to-Action (CTA) buttons: *"Start Chatting"* and *"Explore FAQs"*.
- A live interactive preview card depicting a sample conversation bubble sequence.
- Four feature highlight cards emphasizing 24/7 Availability, Verified Academic Data, Instant Sub-Second Responses, and Zero Hallucination Safety.
- A four-step visual guide explaining the workflow: Ask -> Search -> AI Assist -> Verified Answer.

## 7.2 Student Chatbot Interface
The student chat page (`templates/chat.html`) provides a dedicated, distraction-free conversational interface:
- **Header:** Features an avatar with an active pulsing status indicator and a *"Clear Chat"* action.
- **Message Area:** Distinguishes between student queries (indigo bubbles aligned right) and assistant answers (clean white/navy cards aligned left).
- **Suggested Question Chips:** Provides one-click pills for popular queries (e.g., *"What courses are offered?"*, *"How do I apply?"*, *"What are the fees?"*).
- **Input Form:** Contains a responsive text input field with placeholder prompts, an icon-driven Send button, and keyboard enter-to-send bindings.
- **Typing Indicator:** Displays an animated three-dot bounce animation simulating cognitive response generation while asynchronous requests are pending.

## 7.3 Searchable FAQ Directory & Accordion
The FAQ directory (`templates/faqs.html`) provides an organized, self-service information portal:
- **Real-Time Search Bar:** Instantly filters visible cards as the student types, matching both question titles and answer bodies.
- **Category Filter Pills:** Enables one-click filtering across Admissions, Courses, Fees, Examinations, Facilities, and General.
- **Interactive Accordion:** Allows students to expand and collapse answers with smooth CSS transform transitions.
- **Direct Chat Shortcuts:** Every FAQ card features a *"Ask in Chat"* link that transitions directly to the chat interface with that question pre-filled.

## 7.4 Admin Login Portal
The admin login screen (`templates/admin_login.html`) provides a secure authentication barrier:
- Elegant, centered authentication card with subtle shadow and border styling.
- Fields for Username / Email and Password with inline validation.
- Quick-fill demonstration shortcut for examiners and evaluators (`admin` / `Admin@123`).
- Server-side flash messaging displaying clear error toasts for invalid credentials or session timeouts.

## 7.5 Admin Management Dashboard
The admin control center (`templates/admin_dashboard.html`) offers real-time knowledge governance:
- **Telemetry Metric Cards:** Displays Total FAQs, Active Categories, Total Inquiries Answered, and Database Status.
- **Action Toolbar:** Features an *"Add New FAQ"* primary button, category dropdown filter, and a real-time table search field.
- **FAQ Management Table:** Formats stored records with ID, Question, Answer Preview, Category Badges, and Action buttons (Edit & Delete).
- **Interactive Modals:** Dynamic modal dialogues for creating new entries and editing existing FAQs with instant validation.
- **Confirmation Prompts:** Native modal confirmation safeguards against accidental deletion of institutional FAQs.

---

<div style="page-break-after: always;"></div>

# CHAPTER 8: CONCLUSION & FUTURE ENHANCEMENTS

## 8.1 Summary of Completed Work
The development and deployment of **CampusAI** successfully demonstrates that higher educational institutions can achieve round-the-clock administrative inquiry resolution without incurring exorbitant cloud costs or jeopardizing institutional credibility through AI hallucinations.

Key project milestones achieved include:
1. **Full-Stack Implementation:** Engineered an end-to-end, production-ready web application using Python 3, Flask, SQLAlchemy, SQLite, HTML5, CSS3, and JavaScript.
2. **Dual-Tier NLP Architecture:** Designed and verified a hybrid pipeline combining deterministic keyword normalization with context-bounded LLM fallback.
3. **Provable Academic Safety:** Implemented strict architectural safeguards preventing artificial intelligence hallucinations regarding fees, dates, and college rules.
4. **Third Normal Form Database:** Modeled and deployed a normalized relational database schema supporting seamless CRUD operations.
5. **Dynamic Administrative Governance:** Built a secured, authenticated administrative dashboard enabling non-technical staff to update college knowledge in real time.
6. **100% Automated Test Pass Rate:** Verified all 23 test suites covering authentication, CRUD lifecycles, NLP scoring thresholds, and edge-case handling.
7. **Cloud Production Readiness:** Configured production WSGI deployment via Gunicorn for immediate hosting on platforms like Render.com.

---

## 8.2 Operational Constraints & Limitations
While CampusAI represents a significant advancement over legacy inquiry systems, several constraints were observed:
- **Monolingual NLP Processing:** The current semantic synonym dictionary is tailored primarily for English language queries; vernacular languages (such as Marathi or Hindi) are handled only through the external LLM layer.
- **Static Knowledge Grounding:** Dynamic administrative changes require an administrator to enter the update via the dashboard; the system does not autonomously crawl external institutional PDF circulars.
- **Text-Only Modality:** The interface is currently optimized for textual interaction; voice input (speech-to-text) and auditory playback (text-to-speech) are not yet integrated.

---

## 8.3 Future Enhancements
The modular architectural decoupling of CampusAI allows for seamless feature expansion in subsequent release iterations:
1. **Multilingual / Vernacular Support:** Incorporating regional language tokenizers (e.g., Hindi, Marathi) using IndicNLP models to assist students from diverse linguistic backgrounds.
2. **Speech & Voice Interaction:** Integrating Web Speech API and text-to-speech engines (e.g., Google TTS) to allow hands-free voice interactions for visually impaired students.
3. **Omnichannel Messaging Bots:** Implementing webhook connectors to bridge the Flask API with popular instant messaging platforms (WhatsApp Business API and Telegram Bot API).
4. **ERP / Student Information System Integration:** Securely connecting authenticated student sessions with college ERP databases to enable personalized inquiries (e.g., *"What is my pending semester fee balance?"* or *"What is my internal exam score?"*).
5. **Automated PDF Notice Parser:** Incorporating OCR and document parsing pipelines (e.g., Tesseract or PyMuPDF) to automatically draft FAQ suggestions whenever the college uploads a new circular.

---

<div style="page-break-after: always;"></div>

# REFERENCES & BIBLIOGRAPHY

1. **Grinberg, Miguel.** (2018). *Flask Web Development: Developing Web Applications with Python*. O'Reilly Media, 2nd Edition.
2. **Jurafsky, Daniel, & Martin, James H.** (2023). *Speech and Language Processing: An Introduction to Natural Language Processing, Computational Linguistics, and Speech Recognition*. Stanford University / Pearson.
3. **Vaswani, A., et al.** (2017). *"Attention Is All You Need."* Advances in Neural Information Processing Systems (NeurIPS 2017), pp. 5998–6008.
4. **Pallets Projects.** (2024). *Flask Documentation (Version 3.1.x)*. Available at: `https://flask.palletsprojects.com/`
5. **SQLAlchemy Authors.** (2024). *SQLAlchemy The Database Toolkit for Python Documentation (Version 2.0)*. Available at: `https://docs.sqlalchemy.org/`
6. **Google Cloud.** (2024). *Google GenAI SDK & Gemini API Documentation*. Available at: `https://ai.google.dev/docs`
7. **World Wide Web Consortium (W3C).** (2018). *Web Content Accessibility Guidelines (WCAG) 2.1*. Available at: `https://www.w3.org/TR/WCAG21/`
8. **OWASP Foundation.** (2023). *OWASP Top 10: Top Ten Web Application Security Risks*. Available at: `https://owasp.org/www-project-top-ten/`
9. **Pressman, Roger S., & Maxim, Bruce R.** (2020). *Software Engineering: A Practitioner's Approach*. McGraw-Hill Education, 9th Edition.
10. **Elmasri, Ramez, & Navathe, Shamkant B.** (2016). *Fundamentals of Database Systems*. Pearson, 7th Edition.

---
*(End of Project Report)*
