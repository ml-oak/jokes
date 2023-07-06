# Jokes App Deployment Using Azure DevOps Pipeline

This repository contains a Flask app and an Azure DevOps pipeline configuration to automate the deployment process. Follow the instructions below to run the pipeline and deploy the Flask app using Azure DevOps.

## Prerequisites

- Azure DevOps account
- Basic knowledge of Azure DevOps Pipelines
- Azure DevOps project created with appropriate permissions

## Getting Started

### 1. Clone this repository to your local machine:

git clone https://github.com/your-username/flask-app-azure-pipeline.git

### 2. Navigate to the cloned repository:

cd flask-app-azure-pipeline

### 3. Create a virtual environment and activate it (optional but recommended):
python -m venv env
source env/bin/activate  # For macOS/Linux
env\Scripts\activate  # For Windows

### 4. Install the required dependencies using pip:

pip install -r requirements.txt

### 5. Configure Azure DevOps Pipeline:

a. Log in to your Azure DevOps account.
b. Create a new project or select an existing project.
c. Navigate to the Pipelines section and create a new pipeline.
d. Select your repository as the source and choose the appropriate pipeline configuration file (e.g., azure-pipeline.yml).
e. Modify the pipeline configuration to suit your needs, such as specifying the appropriate trigger, agent pool, and deployment targets.

### 6. Commit and push your changes to trigger the pipeline:

git add .
git commit -m "Add Flask app and pipeline configuration"
git push

### 7. Monitor the pipeline execution in Azure DevOps:

a. Navigate to your project's Pipelines section.
b. Select your pipeline and view the pipeline run details.
c. Monitor the pipeline's progress, logs, and any potential errors.

Once the pipeline completes successfully, your Flask app will be deployed to the local environment. You can access the app using the local endpoint.


