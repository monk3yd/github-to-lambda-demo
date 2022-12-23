# Choose the AWS region and pick a name for the ECR repository

import boto3
import json


def main():
    # --- AWS ---
    AWS_REGION = "us-east-1"
    ECR_REPO = "github-to-lambda-demo"

    # Create an ECR client
    client = boto3.client("ecr", region_name=AWS_REGION)

    # Create ECR repository
    response = client.create_repository(repositoryName=ECR_REPO)
    repository = response["repository"]

    # Convert datetime into str
    repository["createdAt"] = repository["createdAt"].strftime("%m/%d/%Y, %H:%M:%S")

    print(repository)

    # Save repository data
    with open("data/ecr_repo.json", "w") as file:
        file.write(json.dumps(repository, indent=4))


if __name__ == "__main__":
    main()
