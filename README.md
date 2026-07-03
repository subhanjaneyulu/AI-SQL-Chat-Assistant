# AI SQL Chat Assistant

> An AI-powered SQL chatbot that enables users to interact with relational databases using natural language instead of writing SQL queries.

Built with **LangChain**, **Groq LLM**, **MySQL**, **SQLAlchemy**, and **Streamlit**, this application converts plain English questions into SQL queries, executes them on a live database, and returns accurate, human-friendly responses.

---

## Project Overview

Writing SQL queries can be difficult for non-technical users.

This project solves that problem by allowing users to communicate with a database using natural language.

Instead of writing SQL like:

```sql
SELECT * FROM students WHERE branch='AI';
```

Users can simply ask:

> **"Show all AI branch students."**

The AI Agent understands the request, generates the SQL query automatically, retrieves the required data, and provides an easy-to-understand response.

---

# Demo

### User Question

> I am the principal of the college. Give me a complete report about the students including total students, branch-wise distribution, gender-wise distribution, city-wise distribution, highest CGPA, lowest CGPA, average CGPA, top 5 students, and your observations.

### AI Response

->Total Students

->Branch-wise Distribution

->Gender-wise Distribution

->City-wise Distribution

->Highest & Lowest CGPA

->Average CGPA

->Top 5 Students

->AI Generated Insights

The application automatically generates SQL queries, executes them on MySQL, and summarizes the results into a professional report.

---

#Features

- Natural Language to SQL Conversion
- AI-Powered SQL Agent
- Supports MySQL Database
- SQLite Support
- Live Database Querying
- Human-Friendly AI Responses
- SQL Query Validation
- Interactive Chat Interface
- Streamlit UI
- Groq LLM Integration
- LangChain SQL Agent
- Supports Complex Analytical Questions

---

# Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| LangChain | AI Agent Framework |
| Groq | Large Language Model |
| SQLAlchemy | Database Connection |
| MySQL | Relational Database |
| SQLite | Local Database Support |
| Streamlit | User Interface |

---

# Architecture

```
                User

                  │

                  ▼

          Natural Language

                  │

                  ▼

        LangChain SQL Agent

                  │

                  ▼

          Groq Large Language Model

                  │

                  ▼

      SQL Query Generation & Validation

                  │

                  ▼

             SQLAlchemy

                  │

                  ▼

          MySQL / SQLite Database

                  │

                  ▼

            Query Execution

                  │

                  ▼

         AI Generated Response
```

---

#  Project Structure

```
AI-SQL-Chat-Assistant/

│── myapp.py

│── student.db

│── requirements.txt

│── README.md

└── .gitignore
```

---

# Installation


Create Virtual Environment

```bash
python -m venv .venv
```

Activate Environment

Windows

```bash
.venv\Scripts\activate
```

Install Dependencies using uv package

```bash
uv add -r requirements.txt
```

Run the Application

```bash
streamlit run myapp.py
```

---

# Configuration

Provide the following credentials inside the application.

```
Host      : localhost

Username  : root

Password  : ********

Database  : studentdb
```

Also add your Groq API Key.

---

# Example Questions

```
Show all students.

Count total students.

Who has the highest CGPA?

Show students from Hyderabad.

List AI branch students.

Find the average CGPA.

Show top 5 students.

Generate a complete college report.

Which branch performs the best?

Compare AI and CSE students.
```

---

# Learning Outcomes

Through this project I learned:

- Building AI Agents using LangChain

- Connecting LLMs with SQL Databases

- Natural Language to SQL Generation

- SQLAlchemy Integration

- Prompt Engineering

- MySQL Database Connectivity

- Streamlit Application Development

- LLM Tool Calling

- AI Agent Workflow

---

# Future Improvements

- Authentication

- Query History

- Export Report as PDF

- SQL Query Visualization

- Interactive Charts

- Multi Database Support

- React Frontend

- FastAPI Backend

- Docker Deployment

- LangGraph Integration

- Cloud Deployment

---

---

# Why This Project?

This project demonstrates how Large Language Models can interact with structured relational databases to answer business questions using natural language.

It showcases practical skills in:

- Generative AI

- LangChain

- SQL Agents

- Database Integration

- Prompt Engineering

- Backend Development

These are commonly required skills for **Generative AI Engineer**, **LLM Engineer**, and **AI Application Developer** roles.

---

# Author

**Subhanjaneyulu Kallagandla**

Generative AI Developer

---

# ⭐ If you found this project useful

Please consider giving this repository a ⭐.