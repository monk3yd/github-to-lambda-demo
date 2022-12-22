# Github to Lambda Demo

## Steps to follow for CICD setup:

1. Create a new lambda project github repository by using [aws-lambda-template](https://github.com/monk3yd/aws-lambda-template)

2. Clone new lambda project github repository into local machine
```bash
git clone git@github.com:monk3yd/github-to-lambda-demo.git
```

3. Create ECR for new lambda project using create_ecr.py script
```bash
python3 create_ecr.py
```

4. Add to github actions secrets:
  - AWS_ACCESS_KEY
  - AWS_SECRET_ACCESS_KEY
  - AWS_REGION
  - AWS_ACCOUNT_ID (AWS_ECR_REGISTRY)
  - AWS_ECR_REPOSITORY

5. Configure .github/workflows/deploy.yaml for updating ECR container image when push is detected within repo

6. Create lambda function using AWS console. Configure filename and lambda function name as template (app.py & lambda_handler respectively)
