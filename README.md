<div align="center">

# 🚀 AI Cloud Cost Detective

### Intelligent Cloud Cost Optimization Dashboard using React + FastAPI + AWS

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi)
![React](https://img.shields.io/badge/React-Frontend-61DAFB?style=for-the-badge&logo=react)
![Vite](https://img.shields.io/badge/Vite-Build-646CFF?style=for-the-badge&logo=vite)
![AWS](https://img.shields.io/badge/AWS-Cloud-FF9900?style=for-the-badge&logo=amazonaws)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker)
![Terraform](https://img.shields.io/badge/Terraform-IaC-844FBA?style=for-the-badge&logo=terraform)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</div>

---

# 📖 Project Description

**AI Cloud Cost Detective** is a cloud cost optimization dashboard that helps identify underutilized cloud resources and estimate potential monthly savings.

It combines a **React frontend** with a **FastAPI backend** to present cloud resources in a clean dashboard and is designed to be extended for AWS, Azure, and GCP integrations.

---

# ✨ Features

- 🔍 Scan cloud resources
- 💰 Estimate monthly savings
- 📊 Interactive dashboard
- ⚡ FastAPI REST APIs
- ⚛️ React + Vite frontend
- ☁️ AWS-ready architecture
- 🐳 Docker support
- 🌍 Terraform ready
- 📈 Easy to extend with AI recommendations

---

# ☁️ AWS Architecture

```text
                 AWS Cloud

              +----------------+
              | EC2 Instances  |
              +----------------+
                     |
              +----------------+
              | S3 Buckets     |
              +----------------+
                     |
              +----------------+
              | CloudWatch     |
              +----------------+
                     |
              FastAPI Backend
                     |
             REST API (/scan-resources)
                     |
              React Dashboard
```

---

# ⚛️ Tech Stack

| Technology | Purpose |
|------------|----------|
| React | Frontend |
| Vite | Build Tool |
| FastAPI | Backend API |
| Python | Backend |
| Docker | Containerization |
| Terraform | Infrastructure as Code |
| AWS | Cloud Platform |

---

# 📸 Screenshots

## Dashboard

> Add your dashboard screenshot here

```
images/dashboard.png
```

## API Documentation

> Add Swagger screenshot

```
images/swagger.png
```

## Architecture Diagram

> Add architecture diagram

```
images/architecture.png
```

---

# 📂 Project Structure

```text
AI-Cloud-Cost-Detective
│
├── backend
│   ├── main.py
│   ├── requirements.txt
│
├── frontend
│   ├── src
│   ├── public
│   ├── package.json
│
├── README.md
└── .gitignore
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/sampreeth-15/AI-Cloud-Cost-Detective.git

cd AI-Cloud-Cost-Detective
```

---

## Backend

```bash
cd backend

pip install -r requirements.txt

python -m uvicorn main:app --reload
```

Backend runs on

```
http://127.0.0.1:8000
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend runs on

```
http://localhost:5173
```

---

# 🔗 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | / | Home |
| GET | /health | Health Check |
| GET | /scan-resources | Scan Cloud Resources |

---

# 🐳 Docker

Build

```bash
docker build -t ai-cloud-cost-detective .
```

Run

```bash
docker run -p 8000:8000 ai-cloud-cost-detective
```

---

# 🌍 Terraform

Future support

- AWS EC2
- VPC
- IAM
- S3
- RDS
- EKS
- ECS

---

# 🔮 Future Roadmap

- ✅ AWS Integration
- ✅ Azure Integration
- ✅ GCP Integration
- ✅ AI Cost Recommendations
- ✅ Authentication
- ✅ Database Support
- ✅ Charts & Analytics
- ✅ PDF Reports
- ✅ Email Notifications
- ✅ Kubernetes Deployment

---

# 👨‍💻 Author

**Sampreeth B S**

Cloud & DevOps Engineer

GitHub:

https://github.com/sampreeth-15

LinkedIn:

(Add your LinkedIn profile here)

---

# ⭐ Support

If you like this project, please ⭐ the repository.

---

<div align="center">

Made with ❤️ using React, FastAPI & AWS

</div>
