# Sans AI — HR Assist LLM

[![Docker Image](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)](https://hub.docker.com/r/omchoksi/hr-assist-llm)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/)

Professional HR assistant powered by Large Language Models (LLMs) designed to streamline candidate screening, interview preparation, and talent acquisition processes.

## 🚀 Quick Start

```bash
# Pull the image
docker pull omchoksi/hr-assist-llm:latest

# Run with environment file
docker run -d \
  --name hr-assist \
  -p 8501:8501 \
  -p 8000:8000 \
  --env-file .env \
  omchoksi/hr-assist-llm:latest
```

## 📋 Prerequisites

- Docker installed on your system
- GROQ API key (get free at [groq.com](https://groq.com))

## 🔧 Environment Variables

Create a `.env` file with the following variables:

```env
# AI Configuration
GROQ_API_KEY=your_groq_api_key_here
AI_MODEL=llama-3.1-8b-instant
MAX_TOKENS=2048
TEMPERATURE=0.7

# Database Configuration
DATABASE_URL=postgresql://user:password@host:5432/database

# Application Settings
DEBUG=false
LOG_LEVEL=INFO
SECRET_KEY=your_secure_random_key_here
```

## 🌐 Access Points

- **Web Interface**: http://localhost:8501 (Streamlit UI)
- **API Documentation**: http://localhost:8000/docs (FastAPI)
- **Health Check**: http://localhost:8000/api/health

## 🏗️ Architecture

This container includes:
- **FastAPI Backend**: RESTful API for HR operations
- **Streamlit Frontend**: Modern web interface
- **PostgreSQL Integration**: Database support
- **GROQ AI Integration**: LLM-powered features

## 📊 Features

- 🤖 **Intelligent Resume Analysis**: AI-powered candidate evaluation
- 🎯 **Interview Question Generation**: Customized questions for job roles
- 📈 **Skills Gap Analysis**: Comprehensive skill assessment
- 🎨 **Modern UI**: Professional chat interface
- 🔒 **Secure**: Enterprise-grade security standards

## 🏷️ Labels

This image includes comprehensive metadata labels following OCI standards:

- **Title**: Sans AI — HR Assist LLM
- **Description**: Professional HR assistant powered by LLMs
- **Version**: 1.0.0
- **Category**: AI/ML, Business Application, Productivity
- **License**: MIT
- **Maintainer**: OMCHOKSI108

## 📚 Documentation

- [Full Documentation](https://omchoksi108.github.io/hr-assist-llm/)
- [API Reference](https://omchoksi108.github.io/hr-assist-llm/api/)
- [Deployment Guide](https://omchoksi108.github.io/hr-assist-llm/deployment/)

## 🤝 Contributing

Contributions are welcome! Please see our [Contributing Guide](https://omchoksi108.github.io/hr-assist-llm/contributing/) for details.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/OMCHOKSI108/hr-assist-llm/blob/main/LICENSE) file for details.

## 🆘 Support

- [GitHub Issues](https://github.com/OMCHOKSI108/hr-assist-llm/issues)
- [Documentation](https://omchoksi108.github.io/hr-assist-llm/)

---

**Built with ❤️ by [OMCHOKSI108](https://github.com/OMCHOKSI108)**