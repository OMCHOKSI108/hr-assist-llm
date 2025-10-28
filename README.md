# TalentScout AI — Professional Hiring Assistant

TalentScout AI is an enterprise-grade HR assistant powered by Large Language Models (LLMs) designed to streamline candidate screening, interview preparation, and talent acquisition processes. Built with modern AI capabilities and professional-grade security standards.

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Quick Start](#quick-start)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Reference](#api-reference)
- [Frontend Interface](#frontend-interface)
- [Deployment](#deployment)
- [Screenshots](#screenshots)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

## Overview

TalentScout AI transforms traditional HR recruitment workflows by providing intelligent automation for:
- Candidate resume analysis and scoring
- Interview question generation
- Skills assessment and gap analysis
- Automated candidate ranking
- Interview feedback processing

The system integrates seamlessly with existing HR tools and provides both API access for enterprise integration and a user-friendly web interface for direct use.

## Key Features

- **Intelligent Candidate Screening**: Automated resume parsing and candidate evaluation
- **Interview Preparation**: AI-generated interview questions tailored to job requirements
- **Skills Analysis**: Comprehensive skill gap identification and recommendations
- **Multi-format Support**: Handles PDF, DOCX, and text resume formats
- **RESTful API**: Complete API for integration with existing HR systems
- **Web Interface**: Intuitive Streamlit-based frontend for direct use
- **Docker Deployment**: Containerized deployment for easy scaling
- **Security First**: Enterprise-grade security with configurable authentication
- **Extensible Architecture**: Modular design for easy customization

## Quick Start

### Prerequisites

- Docker and Docker Compose
- Git
- At least 4GB RAM available
- Internet connection for LLM API access

### One-Command Deployment

```powershell
# Clone the repository
git clone https://github.com/OMCHOKSI108/hr-assist-llm.git
cd hr-assist-llm

# Start the complete system
docker-compose up -d --build
```

### Access the Application

- **Web Interface**: http://localhost:8501
- **API Documentation**: http://localhost:8000/docs
- **Direct API Access**: http://localhost:8000

### First Use

1. Open the web interface at http://localhost:8501
2. Configure your API keys in the settings panel
3. Upload a candidate resume to test the system
4. Generate interview questions for a job posting

## Installation

### Option 1: Docker Deployment (Recommended)

```powershell
# Clone repository
git clone https://github.com/OMCHOKSI108/hr-assist-llm.git
cd hr-assist-llm

# Build and start services
docker-compose up -d --build

# View logs
docker-compose logs -f
```

### Option 2: Local Development Setup

```powershell
# Clone repository
git clone https://github.com/OMCHOKSI108/hr-assist-llm.git
cd hr-assist-llm

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Copy configuration
cp config.py.example config.py

# Edit configuration with your API keys
notepad config.py  # or your preferred editor

# Start the API server
python -m backend.api

# In another terminal, start the frontend
streamlit run frontend/app.py
```

### Option 3: Using PyProject.toml

```powershell
# Install using modern Python packaging
pip install -e .
```

## Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
# LLM API Configuration
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here

# Application Settings
APP_ENV=production
DEBUG=false
HOST=0.0.0.0
PORT=8000

# Security
SECRET_KEY=your_secret_key_here
JWT_SECRET_KEY=your_jwt_secret_key_here

# Database (if using persistent storage)
DATABASE_URL=sqlite:///hr_assist.db

# File Upload Settings
MAX_FILE_SIZE=10485760  # 10MB
ALLOWED_EXTENSIONS=pdf,docx,txt
```

### Configuration File

Edit `config.py` to customize:

```python
# API Keys
OPENAI_API_KEY = "your-key-here"
ANTHROPIC_API_KEY = "your-key-here"

# Model Settings
DEFAULT_MODEL = "gpt-4"
TEMPERATURE = 0.7
MAX_TOKENS = 2000

# Security Settings
ENABLE_AUTH = True
SESSION_TIMEOUT = 3600

# Feature Flags
ENABLE_RESUME_ANALYSIS = True
ENABLE_INTERVIEW_GEN = True
ENABLE_SKILLS_ANALYSIS = True
```

## Usage

### Web Interface

1. **Access the Application**
   - Open http://localhost:8501 in your browser
   - The interface will load with navigation sidebar

2. **Upload Candidate Resume**
   - Navigate to "Resume Analysis" section
   - Drag and drop or click to upload PDF/DOCX/TXT files
   - Wait for AI processing (typically 10-30 seconds)

3. **Generate Interview Questions**
   - Go to "Interview Preparation" section
   - Enter job description and requirements
   - Specify question types (technical, behavioral, situational)
   - Generate customized question set

4. **Skills Assessment**
   - Use "Skills Analysis" to identify candidate skill gaps
   - Compare against job requirements
   - Get recommendations for training/development

### API Usage

#### Resume Analysis

```python
import requests

# Analyze a resume
response = requests.post(
    "http://localhost:8000/api/analyze-resume",
    files={"file": open("resume.pdf", "rb")},
    data={"job_description": "Software Engineer position"}
)

result = response.json()
print(f"Candidate Score: {result['score']}")
print(f"Key Skills: {result['skills']}")
```

#### Interview Questions

```python
# Generate interview questions
response = requests.post(
    "http://localhost:8000/api/generate-questions",
    json={
        "job_title": "Senior Python Developer",
        "experience_level": "senior",
        "question_types": ["technical", "behavioral"],
        "count": 10
    }
)

questions = response.json()
for q in questions["questions"]:
    print(f"Question: {q['question']}")
    print(f"Type: {q['type']}")
```

#### Skills Analysis

```python
# Analyze skills gap
response = requests.post(
    "http://localhost:8000/api/analyze-skills",
    json={
        "candidate_skills": ["Python", "Django", "PostgreSQL"],
        "required_skills": ["Python", "Django", "React", "AWS"],
        "experience_years": 5
    }
)

analysis = response.json()
print(f"Match Percentage: {analysis['match_percentage']}%")
print(f"Gaps: {analysis['gaps']}")
```

## API Reference

### Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/analyze-resume` | Analyze candidate resume |
| POST | `/api/generate-questions` | Generate interview questions |
| POST | `/api/analyze-skills` | Perform skills gap analysis |
| GET | `/api/health` | Health check endpoint |
| GET | `/docs` | Interactive API documentation |

### Authentication

For enterprise deployments, enable authentication by setting `ENABLE_AUTH=true` in configuration.

```python
# Login
response = requests.post("/api/auth/login", json={
    "username": "hr_manager",
    "password": "secure_password"
})

token = response.json()["access_token"]

# Use token in subsequent requests
headers = {"Authorization": f"Bearer {token}"}
response = requests.get("/api/protected-endpoint", headers=headers)
```

## Frontend Interface

The web interface provides:

- **Dashboard**: Overview of recent analyses and statistics
- **Resume Upload**: Drag-and-drop interface for candidate documents
- **Results Display**: Formatted analysis results with scoring
- **Question Generator**: Interactive form for interview preparation
- **Settings Panel**: Configuration management interface
- **Export Options**: Download results as PDF or JSON

### Navigation

- **Home**: Dashboard and recent activity
- **Analyze**: Resume analysis tools
- **Questions**: Interview question generation
- **Skills**: Skills assessment tools
- **Settings**: Application configuration
- **API Docs**: Interactive API documentation

## Deployment

### Production Deployment

```powershell
# Build production images
docker-compose -f docker-compose.prod.yml up -d --build

# Or use the provided deployment script
./run.sh production
```

### Cloud Deployment Options

#### Azure Container Apps

```powershell
# Deploy to Azure Container Apps
az containerapp up \
  --name talentscout-ai-hr-assist \
  --source . \
  --resource-group your-resource-group \
  --environment your-environment
```

#### AWS ECS

```powershell
# Build and push to ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin your-account.dkr.ecr.us-east-1.amazonaws.com

docker build -t talentscout-ai-hr-assist .
docker tag talentscout-ai-hr-assist:latest your-account.dkr.ecr.us-east-1.amazonaws.com/talentscout-ai-hr-assist:latest
docker push your-account.dkr.ecr.us-east-1.amazonaws.com/talentscout-ai-hr-assist:latest

# Deploy to ECS (configure task definition and service)
```

#### Google Cloud Run

```powershell
# Build and deploy to Cloud Run
gcloud builds submit --tag gcr.io/your-project/talentscout-ai-hr-assist
gcloud run deploy talentscout-ai-hr-assist \
  --image gcr.io/your-project/talentscout-ai-hr-assist \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

### Scaling Considerations

- **Horizontal Scaling**: Use load balancer with multiple container instances
- **Database**: Consider PostgreSQL for production data persistence
- **Caching**: Implement Redis for API response caching
- **Monitoring**: Set up application performance monitoring

## Screenshots

### Frontend Interface
![Frontend Interface](docs/images/frontend.png)
*Professional TalentScout AI interface showing the chat system, theme toggle, and interview progress tracking*

### Backend API
![Backend API](docs/images/backend.png)
*FastAPI backend service running and providing API endpoints for the HR assistant*

### Main Dashboard
![Main Dashboard](assets/images/dashboard.png)
*Main dashboard showing recent analyses and system status*

### Resume Analysis
![Resume Analysis](assets/images/resume_analysis.png)
*Resume upload and analysis interface*

### Interview Questions
![Interview Questions](assets/images/interview_questions.png)
*Generated interview questions interface*

### Skills Assessment
![Skills Assessment](assets/images/skills_assessment.png)
*Skills gap analysis results*

### API Documentation
![API Documentation](assets/images/api_docs.png)
*Interactive API documentation interface*

## Development

### Project Structure

```
hr-assist-llm/
├── main.py               # Main application entry point
├── backend/              # Backend API and services
│   ├── api.py           # FastAPI application
│   ├── config.py        # Configuration management
│   ├── models.py        # Data models and schemas
│   └── __init__.py
├── frontend/             # Frontend interface
│   ├── app.py           # Main Streamlit application
│   ├── components/      # Reusable UI components
│   │   ├── api_service.py
│   │   ├── chat_interface.py
│   │   ├── theme_manager.py
│   │   └── __init__.py
│   ├── assets/          # Static assets
│   │   └── chat_ui.html
│   └── styles/          # CSS stylesheets
├── docs/                # Documentation files
│   ├── images/          # Screenshots and graphics
│   ├── api.md           # API documentation
│   └── screenshots.md   # Visual documentation
├── project/             # Project configuration
│   └── requirements.txt # Python dependencies
├── scripts/             # Deployment scripts
│   └── run.sh          # Docker startup script
├── docker-compose.yml   # Docker services
├── Dockerfile          # Container definition
├── mkdocs.yml          # Documentation configuration
└── .github/            # GitHub Actions workflows
    └── workflows/
```

### Development Setup

```powershell
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest

# Run linting
flake8
black .

# Start development servers
python -m backend.api & streamlit run frontend/app.py
```

### Testing

```powershell
# Run all tests
pytest

# Run with coverage
pytest --cov=. --cov-report=html

# Run specific test file
pytest tests/test_api.py

# Run integration tests
pytest tests/integration/
```

### Code Quality

- **Linting**: flake8 for style checking
- **Formatting**: black for code formatting
- **Type Checking**: mypy for static type analysis
- **Testing**: pytest with coverage reporting

## Contributing

We welcome contributions to TalentScout AI! Please follow these guidelines:

### Development Process

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Make your changes and add tests
4. Ensure all tests pass: `pytest`
5. Format code: `black .`
6. Commit changes: `git commit -m "Add your feature"`
7. Push to branch: `git push origin feature/your-feature-name`
8. Create a Pull Request

### Code Standards

- Follow PEP 8 style guidelines
- Use type hints for function parameters and return values
- Write comprehensive docstrings
- Add unit tests for new features
- Update documentation for API changes

### Reporting Issues

- Use GitHub Issues to report bugs
- Include detailed reproduction steps
- Attach relevant screenshots or logs
- Specify your environment (OS, Python version, etc.)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

- **Documentation**: https://omchoksi108.github.io/hr-assist-llm/
- **Issues**: https://github.com/OMCHOKSI108/hr-assist-llm/issues
- **Discussions**: https://github.com/OMCHOKSI108/hr-assist-llm/discussions

## Changelog

### Version 1.0.0
- Initial release with core HR assistant functionality
- Resume analysis and scoring
- Interview question generation
- Skills gap analysis
- Web interface and REST API
- Docker containerization
- Comprehensive documentation

---

Built with modern AI capabilities for enterprise HR excellence.


