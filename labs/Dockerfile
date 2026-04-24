FROM python:3.12-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire labs directory into the container
COPY . .

# Expose the port that ADK Web uses
EXPOSE 8080

# Command to run the Capstone agent via ADK web on port 8080
# Note: Cloud Run requires binding to 0.0.0.0 and defaults to PORT 8080
CMD ["adk", "web", "--host", "0.0.0.0", "--port", "8080", "--allow_origins", "*", "03_capstone/04_custom_agent_challenge"]
