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

This repository implements a comprehensive CI/CD (Continuous Integration/Continuous Deployment) pipeline using GitHub Actions, with distinct stages for testing, building, and deploying the application to both staging and production environments.

### Workflow Overview

The CI/CD pipeline consists of the following sequential stages:

1. **Testing Stage**:
   - Triggered on every push to any branch and pull requests to main/staging
   - Sets up Python environment
   - Installs all dependencies from requirements.txt
   - Runs the test suite using pytest
   - Fails fast if any tests fail, preventing further pipeline execution

2. **Build Stage**:
   - Only proceeds if all tests pass
   - Prepares the application for deployment
   - Creates build artifacts (application files and dependencies)
   - Stores artifacts for deployment stages

3. **Staging Deployment**:
   - Only triggers when changes are pushed to the staging branch
   - Uses GitHub environment protection rules for staging
   - Downloads the build artifacts
   - Deploys the application to the staging server
   - Provides a deployment URL for testing

4. **Production Deployment**:
   - Only triggers when a new release is published
   - Uses GitHub environment protection rules for production
   - Downloads the same build artifacts (ensuring what was tested is what's deployed)
   - Deploys the application to the production server
   - Provides a production deployment URL

### Branch Strategy

The workflow is designed to work with the following branch structure:

- `main`: Primary development branch (runs tests, no automatic deployment)
- `staging`: Pre-production branch (runs tests, automatically deploys to staging)
- `release tags`: Creating a new release with a tag (e.g., v1.0.0) triggers a production deployment

### Setting Up GitHub Secrets

The workflow uses GitHub Secrets to securely store sensitive deployment information. To configure these secrets:

1. Navigate to your GitHub repository
2. Go to **Settings** > **Secrets and variables** > **Actions**
3. Click on **New repository secret**
4. Add the following secrets:

| Secret Name | Description |
|-------------|-------------|
| `DEPLOY_KEY` | SSH key or API token used for deployments (shared between environments) |
| `STAGING_SERVER` | Hostname or IP address of the staging server |
| `STAGING_API_TOKEN` | API token for staging environment (if applicable) |
| `PRODUCTION_SERVER` | Hostname or IP address of the production server |
| `PRODUCTION_API_TOKEN` | API token for production environment (if applicable) |

### GitHub Environments

The workflow uses GitHub Environments to separate staging and production deployments:

1. Navigate to your GitHub repository
2. Go to **Settings** > **Environments**
3. Create two environments: `staging` and `production`
4. For each environment, you can set up:
   - Required reviewers for manual approval before deployment
   - Wait timer to add a delay before deployment 
   - Environment-specific secrets

### Workflow File

The workflow is defined in the `.github/workflows/ci-cd.yml` file. It contains all the jobs and steps described above. You can customize it to fit your specific deployment needs.

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
6. Once verified in staging, create a new release to deploy to production

## Monitoring Deployments

You can monitor the progress and status of deployments in the GitHub Actions tab of your repository:

1. Go to the **Actions** tab
2. Select the workflow run you want to monitor
3. View the detailed logs for each job
4. Check the deployment URLs provided in the output

## Troubleshooting

If a deployment fails:

1. Check the workflow run logs for error messages
2. Verify that all secrets are correctly configured
3. Ensure your application passes all tests
4. Check server connectivity and permissions

For more information on GitHub Actions, visit the [official documentation](https://docs.github.com/en/actions). 