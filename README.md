# DevOps CI/CD Pipeline with GitHub Actions, Docker, GHCR and AWS EC2

A complete CI/CD project that automatically tests a Python Flask application, builds a Docker image, pushes it to GitHub Container Registry (GHCR), and deploys it to an AWS EC2 instance using a self-hosted GitHub Actions runner.

## Project Architecture

Developer
   |
   | git push
   v
GitHub Repository
   |
   v
GitHub Actions
   |
   +--> Install Python dependencies
   |
   +--> Check Python syntax
   |
   +--> Run pytest automated tests
   |
   +--> Build Docker image
   |
   +--> Push Docker image to GHCR
   |
   v
GitHub Container Registry
   |
   v
AWS EC2 Self-Hosted Runner
   |
   +--> Pull latest Docker image
   |
   +--> Stop old container
   |
   +--> Remove old container
   |
   +--> Start new container
   |
   v
Flask Application
Port 5000

## Technologies Used

- Python
- Flask
- pytest
- Docker
- GitHub Actions
- GitHub Container Registry
- AWS EC2
- Linux
- Git
- GitHub
- CI/CD
- Self-hosted GitHub Actions Runner

## CI Pipeline

The CI stage runs automatically on every push to the main branch.

The pipeline performs:

1. Checkout source code
2. Set up Python 3.13
3. Install dependencies
4. Check Python syntax
5. Run automated pytest tests
6. Build Docker image
7. Log in to GHCR
8. Push Docker image to GHCR

## Automated Testing

The project uses pytest to validate the Flask health endpoint.

Example test:

```python
def test_health_endpoint():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "healthy"
    assert data["service"] == "flask-backend"
