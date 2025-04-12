# S3 Event-Driven Notification System

This project implements an event-driven architecture using AWS serverless services that sends email notifications when files are uploaded to an S3 bucket.

## Architecture Overview

1. User uploads a file to the S3 bucket
2. S3 event triggers a Lambda function
3. Lambda function processes the event and publishes a message to SNS
4. SNS sends an email notification to subscribed email addresses

## AWS Services Used

- **Amazon S3**: Storage for uploaded files
- **AWS Lambda**: Serverless compute to process upload events
- **Amazon SNS**: Notification service to send emails
- **AWS SAM**: Infrastructure as Code to define and deploy resources
- **GitHub Actions**: CI/CD pipeline for automated deployment

## Deployment Instructions

### Prerequisites

- AWS CLI installed and configured
- AWS SAM CLI installed
- GitHub account with repository access

### Local Development

1. Clone the repository:
   ```
   git clone https://github.com/your-username/s3-notification-service.git
   cd s3-notification-service
   ```

2. Build the SAM application:
   ```
   sam build
   ```

3. Deploy to development environment:
   ```
   sam deploy --config-env dev --parameter-overrides $(cat env/dev.json)
   ```

### CI/CD Pipeline

The project includes a GitHub Actions workflow that automatically builds and deploys the application when changes are pushed:

- Push to `develop` branch: Deploys to the development environment
- Push to `main` branch: Deploys to the production environment

You can also manually trigger a deployment via the GitHub Actions workflow dispatch and select the environment.

### Required GitHub Secrets

Set up the following secrets in your GitHub repository:

- `AWS_ACCESS_KEY_ID`: AWS access key with permissions to deploy resources
- `AWS_SECRET_ACCESS_KEY`: Corresponding AWS secret key
- `AWS_REGION`: AWS region to deploy resources (e.g., us-east-1)

## Testing

1. Navigate to the S3 console
2. Upload a file to the created bucket
3. Check the subscribed email address for notifications

## Cleanup

To remove all deployed resources:

```
sam delete --config-env dev  # For development environment
sam delete --config-env prod  # For production environment
```

## Project Structure

s3-notification-service/
├── .github/
│   └── workflows/
│       └── sam-pipeline.yml
├── src/
│   └── handlers/
│       └── notification_handler.py
├── samconfig.toml
├── template.yaml
├── env/
│   ├── dev.json
│   └── prod.json
└── README.md