# Customer Accounts Microservice

## Project Name: DevOps Capstone Project - Customer Accounts Service

## 📌 Project Overview
This project implements a Customer Accounts microservice with full DevOps practices including:
- RESTful API development
- Automated testing with nosetests
- CI/CD pipeline with GitHub Actions
- Security headers with Talisman and CORS
- Containerization with Docker
- Deployment to Kubernetes
- Tekton CD pipeline

## 🚀 Technologies Used
- **Python/Flask** - REST API
- **nosetests** - Unit testing
- **flake8** - Linting
- **GitHub Actions** - CI/CD
- **Docker** - Containerization
- **Kubernetes** - Orchestration
- **Tekton** - CD Pipeline

## 📁 Repository Structure
.
├── .github/workflows/
│ └── ci-build.yaml # CI workflow
├── service/
│ ├── init.py # App with Talisman/CORS
│ ├── models.py # Data models
│ └── routes.py # API routes
├── tests/
│ └── test_routes.py # Unit tests
├── .tekton/
│ └── pipeline.yaml # CD pipeline
├── Dockerfile # Container definition
├── setup.cfg # Testing config
├── user-story.md # User stories
└── README.md

text

## 🔄 API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/accounts` | List all accounts |
| GET | `/accounts/<id>` | Read one account |
| POST | `/accounts` | Create an account |
| PUT | `/accounts/<id>` | Update an account |
| DELETE | `/accounts/<id>` | Delete an account |

## ✅ CI/CD Status
- CI Pipeline: ✅ Passing
- CD Pipeline: ✅ Passing
- Security Headers: ✅ Configured
- Docker: ✅ Built
- Kubernetes: ✅ Deployed
