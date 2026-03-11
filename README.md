# flask-cicd-pipeline
Production-grade CI/CD  pipeline using Jenkins, Docker &amp; GitHub
# 🚀 Flask CI/CD Pipeline

![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=flat&logo=jenkins&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)

Production-grade CI/CD pipeline for Flask application 
using Jenkins, Docker & GitHub Webhooks.

## 🏗️ Architecture
```
GitHub Push → Webhook → Jenkins Pipeline
                              ↓
                    ┌─────────────────┐
                    │   Stages:       │
                    │ 1. Checkout     │
                    │ 2. Run Tests    │
                    │ 3. Docker Build │
                    │ 4. Docker Push  │
                    │ 5. Deploy       │
                    │ 6. Health Check │
                    └────────┬────────┘
                             ↓
                    Slack + Email Notify
```

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python Flask | Web Application |
| Docker | Containerization |
| Jenkins | CI/CD Automation |
| GitHub | Source Control |
| Docker Hub | Image Registry |
| Slack | Team Notification |
| Email | Build Notification |

## ⚙️ Pipeline Stages

| Stage | Description |
|-------|-------------|
| 🔔 Notify Start | Slack notification on build start |
| 📥 Checkout | Pull code from GitHub |
| 🧪 Run Tests | Unit tests with pytest |
| 🐳 Build Image | Create Docker image |
| ☁️ Push to Hub | Upload to Docker Hub |
| 🚀 Deploy | Run container |
| ❤️ Health Check | Verify app is running |

## 🚀 Quick Start
```bash
# Pull from Docker Hub
docker pull naeem3295/flask-cicd-pipeline:latest

# Run the app
docker run -d -p 5050:5000 naeem3295/flask-cicd-pipeline:latest

# Test endpoints
curl http://localhost:5050/
curl http://localhost:5050/health
curl http://localhost:5050/api/info
```

## 📡 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | App information |
| `/health` | GET | Health check |
| `/api/info` | GET | Pipeline info |

## 🔧 Jenkins Setup

1. Install Jenkins with Docker
2. Add GitHub Webhook
3. Configure Docker Hub credentials
4. Configure Slack notification
5. Run pipeline

## 👨‍💻 Developer

**MD ABU NAEEM**  
DevOps Engineer
