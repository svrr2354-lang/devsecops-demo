# Secure Pipeline Demo

A Flask-based web application demonstrating secure coding practices, specifically focusing on SQL injection prevention through parameterized queries. This project includes containerization with Docker and Kubernetes deployment configurations.

## 🎯 Overview

This project serves as an educational demo showcasing a secure login system that uses parameterized SQL queries to prevent SQL injection attacks. The application includes both the secure implementation and security testing tools.

## ✨ Features

- **Secure Login System**: Implements parameterized queries to prevent SQL injection
- **Flask Web Application**: Lightweight Python web framework
- **SQLite Database**: Embedded database with user management
- **Docker Support**: Containerized application for easy deployment
- **Kubernetes Ready**: Includes deployment and service manifests
- **Security Testing**: Includes exploit script to test SQL injection prevention

## 📋 Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- Docker (for containerization)
- Kubernetes (optional, for Kubernetes deployment)

## 🚀 Installation

### Local Development Setup

1. **Clone the repository** (or navigate to the project directory)

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Initialize the database** (automatically created on first run):
   ```bash
   python app.py
   ```

4. **Access the application**:
   - Open your browser and navigate to `http://localhost:5000`

## 🐳 Docker Deployment

1. **Build the Docker image**:
   ```bash
   docker build -t vulnerable-bank:v2 .
   ```

2. **Run the container**:
   ```bash
   docker run -p 5000:5000 vulnerable-bank:v2
   ```

3. **Access the application**:
   - Open your browser and navigate to `http://localhost:5000`

## ☸️ Kubernetes Deployment

1. **Load the Docker image** into your Kubernetes cluster (if using local image):
   ```bash
   kind load docker-image vulnerable-bank:v2
   ```

2. **Deploy the application**:
   ```bash
   kubectl apply -f deployment.yaml
   kubectl apply -f service.yaml
   ```

3. **Get the service URL**:
   ```bash
   kubectl get services
   ```

## 🔒 Security Features

### Parameterized Queries

The application uses parameterized SQL queries to prevent SQL injection attacks:

```python
query = "SELECT * FROM users WHERE username = ? AND password = ?"
cursor.execute(query, (username, password))
```

This approach ensures that user input is treated as data, not executable SQL code, effectively preventing SQL injection vulnerabilities.

## 🧪 Testing

The project includes an `exploit.py` script to test SQL injection prevention:

1. **Start the application** (locally or in Docker)

2. **Run the security test**:
   ```bash
   python exploit.py
   ```

The script attempts a SQL injection attack and verifies that the application correctly rejects the malicious input.

## 📁 Project Structure

```
secure-pipeline-demo/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── Dockerfile         # Docker container configuration
├── deployment.yaml    # Kubernetes deployment manifest
├── service.yaml       # Kubernetes service manifest
├── exploit.py         # Security testing script
├── demo.db           # SQLite database (created at runtime)
└── README.md         # This file
```

## 🔑 Default Credentials

The application initializes with a default admin user:
- **Username**: `admin`
- **Password**: `adminpass`

⚠️ **Note**: These are demo credentials. Change them in production environments.

## 🌐 Endpoints

- `GET /` - Home page with login link
- `GET /login` - Login page
- `POST /login` - Submit login credentials

## 🛠️ Technologies Used

- **Flask**: Web framework
- **SQLite**: Database
- **Docker**: Containerization
- **Kubernetes**: Container orchestration

## 📝 License

This project is for educational and demonstration purposes.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## ⚠️ Disclaimer

This project is designed for educational purposes to demonstrate secure coding practices. Always follow security best practices in production environments.

