# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Standard Docker labels
LABEL org.opencontainers.image.title="Sans AI — HR Assist LLM" \
      org.opencontainers.image.description="Professional HR assistant powered by Large Language Models (LLMs) designed to streamline candidate screening, interview preparation, and talent acquisition processes" \
      org.opencontainers.image.version="1.0.0" \
      org.opencontainers.image.authors="OMCHOKSI108 <omchoksi108@example.com>" \
      org.opencontainers.image.vendor="Sans AI" \
      org.opencontainers.image.url="https://github.com/OMCHOKSI108/hr-assist-llm" \
      org.opencontainers.image.source="https://github.com/OMCHOKSI108/hr-assist-llm" \
      org.opencontainers.image.licenses="MIT" \
      org.opencontainers.image.category="AI/ML,Business Application,Productivity" \
      org.opencontainers.image.documentation="https://omchoksi108.github.io/hr-assist-llm/" \
      org.opencontainers.image.keywords="hr-assistant,llm,ai,talent-scout,recruitment,interview-preparation,resume-analysis" \
      maintainer="OMCHOKSI108" \
      architecture="x86_64" \
      os="linux" \
      language="python" \
      framework="fastapi,streamlit"

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY project/requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . .

# Make run.sh executable
RUN chmod +x scripts/run.sh

# Make ports available
EXPOSE 8501 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
  CMD curl -fsS http://localhost:8000/api/health || exit 1

# Define environment variable
ENV STREAMLIT_SERVER.PORT 8501

# Run the application
CMD ["scripts/run.sh"]