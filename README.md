# 🤖 AI Resume Analyzer

<p align="center">

<img src="https://img.shields.io/badge/Python-3.x-blue.svg">
<img src="https://img.shields.io/badge/FastAPI-REST%20API-009688.svg">
<img src="https://img.shields.io/badge/NLP-Skill%20Analysis-purple.svg">
<img src="https://img.shields.io/badge/PDF-Text%20Extraction-red.svg">
<img src="https://img.shields.io/badge/Testing-Pytest-green.svg">
<img src="https://img.shields.io/badge/JSON-API%20Response-orange.svg">
<img src="https://img.shields.io/badge/Status-Completed-success.svg">
<img src="https://img.shields.io/badge/License-Educational-yellow.svg">

</p>

A Python and FastAPI-based resume analysis application that evaluates a resume against a job description, detects relevant skills, identifies missing skills, calculates an ATS-style matching score, and provides practical recommendations.

---

## 📌 Overview

The **AI Resume Analyzer** is a portfolio-focused application designed to help students and job seekers understand how well their resume matches a particular job description.

The system accepts a **PDF resume** and a **job description**, extracts text from the resume, detects technical skills, compares the resume skills with the job requirements, calculates skill and keyword scores, identifies missing skills, detects education and experience-related information, and generates recommendations.

The project uses a transparent scoring approach so that the user can understand how the final score is calculated.

> ⚠️ This project provides an **ATS-style analysis** and is not an official ATS score or a guarantee of interview selection.

---

## 🎬 Project Demo

Add your recorded project GIF as:

```text
assets/demo.gif
```

Then display it in GitHub using:

![AI Resume Analyzer Demo](https://github.com/aakashp2008/ai-resume-analyzer/raw/main/assets/demo.gif)

### 🌐 Related External GIF

![Resume Analysis](https://media.giphy.com/media/QBd2kLB5qDmysEXre9/giphy.gif)

> The external GIF is used only as a visual reference. The actual project demonstration should be recorded from this application and stored as `assets/demo.gif`.

---

## ✨ Features

* 📄 PDF resume upload
* 📝 Job description input
* 🔍 Resume text extraction
* 🧠 Technical skill detection
* 💼 Job requirement detection
* 🎯 Resume-job skill matching
* 📊 ATS-style matching score
* 📈 Skill match score
* 🔑 Keyword analysis
* 🧩 Missing skill detection
* ✅ Matched skill detection
* 🎓 Education keyword detection
* 💼 Experience keyword detection
* 💡 Personalized recommendations
* 🌐 FastAPI REST API
* 📚 Interactive API documentation
* 🧪 Automated API testing
* ⚠️ Input validation
* 💾 Structured JSON responses
* 🏗️ Modular project architecture

---

## 🛠️ Technologies Used

* Python 3
* FastAPI
* Uvicorn
* Pydantic
* PyPDF
* Pytest
* HTTPX
* Regular Expressions
* JSON
* REST API
* File Handling
* Object-Oriented / Modular Programming Concepts

---

## 📂 Project Structure

```text
ai-resume-analyzer/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   │
│   └── services/
│       ├── __init__.py
│       ├── resume_parser.py
│       ├── skill_extractor.py
│       └── matching_engine.py
│
├── tests/
│   └── test_api.py
│
├── sample_data/
│   └── sample_job_description.txt
│
├── assets/
│   └── demo.gif
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

Make sure Python 3.x is installed.

Check your Python version:

```bash
python --version
```

or:

```bash
python3 --version
```

---

## 📥 Clone the Repository

Clone the project:

```bash
git clone https://github.com/aakashp2008/ai-resume-analyzer.git
```

Navigate into the project:

```bash
cd ai-resume-analyzer
```

---

## 🐍 Create a Virtual Environment

Create a virtual environment:

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

---

## 📦 Install Dependencies

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The application will run at:

```text
http://127.0.0.1:8000
```

---

## 🌐 API Documentation

FastAPI automatically provides interactive documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

You can use the **Swagger UI** to test the API directly from your browser.

Alternative documentation:

```text
http://127.0.0.1:8000/redoc
```

---

## 🔐 Login

This version does **not require a login system**.

The application is designed as a resume analysis API.

Future versions can include:

* 👤 User registration
* 🔐 Secure login
* 🔑 Password protection
* 👥 Multiple user profiles
* 🛡️ Role-based access
* 🔒 Authentication using JWT

---

## 🖥️ API Endpoints

### Health Check

```text
GET /health
```

Example response:

```json
{
    "status": "healthy"
}
```

### Application Information

```text
GET /
```

Example response:

```json
{
    "message": "AI Resume Analyzer API",
    "version": "2.0.0",
    "status": "running"
}
```

### Resume Analysis

```text
POST /analyze
```

The endpoint accepts:

* PDF resume
* Job description

---

## 🧪 Example Input

### Resume

Example resume content:

```text
Aakash P

B.Tech Information Technology Student

Skills:
Python
Java
SQL
Git
GitHub
Data Structures
Algorithms
HTML
CSS
JavaScript
Pandas
NumPy

Experience:
Software Development Internship

Projects:
Student Management System
Data Analysis Project

Education:
B.Tech Information Technology
Engineering College
CGPA: 8.6
```

### Job Description

```text
We are looking for a Software Developer.

Required Skills:
Python
Java
SQL
Git
JavaScript
React
Docker
REST API
Data Structures
Algorithms

Candidates should have software development
experience and knowledge of modern technologies.
```

---

## 📊 Example Output

```json
{
    "filename": "aakash_resume.pdf",
    "ats_style_score": 72.45,
    "skill_match_score": 80.0,
    "keyword_score": 54.83,
    "resume_skills": [
        "algorithms",
        "data structures",
        "git",
        "java",
        "javascript",
        "python",
        "sql"
    ],
    "required_skills": [
        "algorithms",
        "data structures",
        "docker",
        "git",
        "java",
        "javascript",
        "python",
        "react",
        "rest api",
        "sql"
    ],
    "matched_skills": [
        "algorithms",
        "data structures",
        "git",
        "java",
        "javascript",
        "python",
        "sql"
    ],
    "missing_skills": [
        "docker",
        "react",
        "rest api"
    ],
    "detected_experience": [
        "experience",
        "internship",
        "project"
    ],
    "detected_education": [
        "b.tech",
        "college",
        "engineering",
        "information technology"
    ],
    "recommendations": [
        "Consider developing the missing technical skills."
    ]
}
```

---

## 🔍 Analysis

The application performs several types of analysis.

### 1. Skill Analysis

The system detects technical skills present in the resume.

Example:

```text
Resume Skills:
Python
Java
SQL
Git
JavaScript
```

The system then compares them with the skills detected in the job description.

---

### 2. Matched Skills

Skills present in both the resume and job description are considered matched.

Example:

```text
Python
Java
SQL
Git
JavaScript
```

---

### 3. Missing Skills

Skills required by the job description but not detected in the resume are displayed.

Example:

```text
Docker
React
REST API
```

This can help users identify areas they may want to learn or demonstrate through projects.

---

### 4. Skill Match Score

The skill match score is calculated using:

```text
Skill Match Score =
Matched Required Skills
/
Total Required Skills
× 100
```

---

### 5. Keyword Analysis

The application compares important words found in the resume and job description.

This provides an additional keyword score.

---

### 6. ATS-Style Score

The project uses a transparent weighted calculation:

```text
ATS-Style Score =
70% Skill Match Score
+
30% Keyword Score
```

This is a project-defined scoring model.

It is **not an official ATS algorithm**.

---

### 7. Education Detection

The system checks for education-related terms such as:

```text
B.Tech
Bachelor
Engineering
College
University
CGPA
Information Technology
```

---

### 8. Experience Detection

The system detects experience-related terms such as:

```text
Internship
Intern
Experience
Developer
Engineer
Project
Work Experience
```

---

## 💡 Recommendations

The system provides recommendations based on the detected resume information.

Examples:

* 🎯 Develop missing technical skills.
* 📚 Improve skills required by the target role.
* 💼 Add relevant internship or project experience.
* 🎓 Clearly mention educational qualifications.
* 🔍 Align relevant resume content with the job description.
* 📈 Strengthen projects related to the target position.

> Recommendations are generated from the information detected by the application and should not be treated as guaranteed career advice.

---

## 🧠 Concepts Demonstrated

This project demonstrates:

* Python programming
* FastAPI
* REST APIs
* API endpoints
* HTTP methods
* File uploads
* PDF processing
* Text extraction
* Regular expressions
* String processing
* Sets
* Lists
* Dictionaries
* Functions
* Modular programming
* Pydantic models
* JSON responses
* Input validation
* Exception handling
* Automated testing
* Pytest
* API documentation
* Software architecture

---

## 🎯 Project Objectives

The main objectives are:

1. Build a practical Python application.
2. Process resume PDF files.
3. Extract useful resume information.
4. Detect technical skills.
5. Analyze job descriptions.
6. Compare resume skills with job requirements.
7. Identify missing skills.
8. Calculate a transparent matching score.
9. Provide actionable recommendations.
10. Build a REST API using FastAPI.
11. Practice automated API testing.
12. Develop a placement-oriented portfolio project.

---

## 📚 Learning Outcomes

Through this project, I practiced:

* Building REST APIs using FastAPI.
* Handling file uploads.
* Extracting text from PDF documents.
* Processing unstructured text.
* Using regular expressions.
* Working with Python sets.
* Designing modular applications.
* Creating Pydantic response models.
* Returning structured JSON.
* Validating user input.
* Handling API errors.
* Writing automated tests.
* Using Swagger API documentation.
* Designing service-based project architecture.
* Building a practical AI/NLP-oriented application.

---

## 🧪 Testing

Run the automated tests using:

```bash
pytest
```

Expected result:

```text
3 passed
```

The tests verify:

* API availability
* Health endpoint
* Invalid file handling

---

## ⚠️ Current Limitations

The current version has some limitations:

* 📄 Only PDF resumes are supported.
* 🧠 Skill detection uses a predefined skill dictionary.
* 🤖 It does not use a trained machine-learning model.
* 🔍 Keyword analysis is relatively simple.
* 📊 The ATS-style score is a custom scoring model.
* 🗃️ No database is currently used.
* 👤 No user authentication.
* ☁️ No cloud storage.
* 📧 No email notifications.
* 📱 No mobile application.
* 🖥️ No dedicated frontend dashboard.
* 📝 Complex resume layouts may affect PDF text extraction.

---

## 🔮 Future Enhancements

### Phase 1 — Advanced Resume Parsing

* Extract candidate name
* Extract email
* Extract phone number
* Extract education details
* Extract projects
* Extract certifications
* Extract work experience
* Extract dates
* Extract job titles

---

### Phase 2 — Advanced NLP

* Named Entity Recognition
* Natural Language Processing
* Sentence similarity
* Semantic skill matching
* Synonym detection
* Context-aware skill extraction
* Better keyword analysis

---

### Phase 3 — Machine Learning

Future versions can use machine-learning models for:

* Resume classification
* Job-role prediction
* Skill recommendation
* Semantic resume-job matching
* Resume quality prediction

---

### Phase 4 — Database

Add database support using:

* SQLite
* MySQL
* PostgreSQL

Store:

* User profiles
* Resumes
* Job descriptions
* Analysis history
* Skill results
* Recommendations

---

### Phase 5 — Web Dashboard

Create a frontend dashboard using:

* React
* TypeScript
* HTML
* CSS
* JavaScript

Dashboard features:

* 📊 Resume score
* 🎯 Skill match
* 🧩 Missing skills
* 📈 Keyword analysis
* 💼 Job recommendations
* 📚 Skill development suggestions
* 📜 Analysis history

---

### Phase 6 — Smart Job Matching

The system could recommend suitable job opportunities based on:

* Technical skills
* Education
* Projects
* Certifications
* Experience
* Preferred roles
* Career interests

---

### Phase 7 — Deployment

Deploy the application using:

* Docker
* GitHub Actions
* Cloud hosting
* Production database
* Secure environment variables

---

## 🔒 Security Note

The current project is intended for educational and portfolio use.

Important considerations:

* Do not upload sensitive personal information unnecessarily.
* Do not commit private resumes to GitHub.
* Do not store passwords in source code.
* Do not commit API keys or secrets.
* Use environment variables for sensitive configuration.
* Production deployments should use authentication and secure storage.
* Uploaded files should be validated before processing.

---

## 🌟 Why This Project?

Resume screening is an important part of modern recruitment.

Students often struggle to understand:

**"Does my resume actually match this job?"**

This project provides a practical way to analyze that question.

The system converts:

```text
Resume PDF
     +
Job Description
     ↓
Text Extraction
     ↓
Skill Detection
     ↓
Keyword Analysis
     ↓
Skill Matching
     ↓
Missing Skills
     ↓
ATS-Style Score
     ↓
Recommendations
```

It combines **Python, API development, PDF processing, text analysis, testing, and career-focused application development** in one project.

---

## 💼 Placement Relevance

This project demonstrates skills that are useful for software-development placements:

* Python
* REST API development
* FastAPI
* Backend development
* File processing
* Data processing
* NLP fundamentals
* JSON
* API testing
* Git/GitHub
* Modular architecture
* Problem solving

It also gives interview discussion points such as:

* How PDF text extraction works
* How skills are detected
* How matching is calculated
* Why sets are used
* How REST APIs work
* How API validation is implemented
* How automated testing is performed
* How the project could be improved using NLP/ML

---

## 👨‍💻 Author

### Aakash P

**B.Tech Information Technology Student**

### Skills & Interests

* Python
* Java
* C
* SQL
* Data Structures & Algorithms
* FastAPI
* REST APIs
* Artificial Intelligence
* Machine Learning
* Data Analysis
* Web Development
* Software Development

---

## 🔗 GitHub

### Repository

https://github.com/aakashp2008/ai-resume-analyzer

### GitHub Profile

https://github.com/aakashp2008

---

## ⭐ Support

If you find this project useful for learning or placement preparation, consider giving the repository a ⭐ on GitHub.

Your support encourages further development and improvement.

---

## 📄 License

This project is created for educational and learning purposes.

You are free to study, modify, and improve the code for your own learning and projects.

---

## 📌 Project Status

```text
Version: 2.0
Status: Completed
Type: Educational / Portfolio Project
Language: Python
Framework: FastAPI
```

---

### 🔗 Related Resources

* FastAPI: https://fastapi.tiangolo.com/
* PyPDF: https://pypi.org/project/pypdf/
* Pytest: https://docs.pytest.org/
* Python: https://www.python.org/
