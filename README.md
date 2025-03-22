# Flask Calculator API

A simple Flask application that provides basic calculator operations via REST API endpoints.

## Features

- Addition, subtraction, multiplication, and division operations
- Error handling for invalid inputs and division by zero
- RESTful API with JSON responses
- CI/CD pipeline using GitHub Actions

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/JenexamplePy.git
cd JenexamplePy
```

2. Install the dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python calculate.py
```

## API Endpoints

- `/add?a=number&b=number` - Adds two numbers
- `/subtract?a=number&b=number` - Subtracts b from a
- `/multiply?a=number&b=number` - Multiplies two numbers
- `/divide?a=number&b=number` - Divides a by b

## CI/CD Pipeline with GitHub Actions

This repository uses GitHub Actions to implement a Continuous Integration and Continuous Deployment pipeline.

### Workflow Overview

The workflow automates the following steps:

1. **Test**: Runs on every push and pull request to main and staging branches
   - Sets up Python environment
   - Installs dependencies
   - Runs pytest test suite

2. **Build**: Runs after successful tests
   - Prepares the application for deployment
   - Creates build artifacts

3. **Deploy to Staging**: Runs when changes are pushed to the staging branch
   - Deploys the application to a staging environment
   - Uses staging-specific configuration

4. **Deploy to Production**: Runs when a release is published
   - Deploys the application to the production environment
   - Uses production-specific configuration

### Setting Up GitHub Secrets

The workflow uses GitHub Secrets to store sensitive information. To set up the required secrets:

1. Navigate to your GitHub repository
2. Go to **Settings** > **Secrets and variables** > **Actions**
3. Add the following secrets:

| Secret Name | Description |
|-------------|-------------|
| `DEPLOY_KEY` | SSH key or API token used for deployment |
| `STAGING_SERVER` | Hostname or IP address of the staging server |
| `PRODUCTION_SERVER` | Hostname or IP address of the production server |

### Branch Strategy

- `main`: Main development branch, changes here are tested but not automatically deployed
- `staging`: Staging branch, changes here trigger deployment to the staging environment
- `tags/releases`: Creating a new release deploys to the production environment

## Running Tests

Run the test suite with:

```bash
pytest
```

## Contributing

1. Create a new branch from `main`
2. Make your changes
3. Run tests locally to ensure they pass
4. Create a pull request to the `staging` branch
5. After review and approval, your changes will be merged and deployed to staging
6. Once verified in staging, changes can be included in a release for production deployment 