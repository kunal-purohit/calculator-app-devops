# Calculator-App-Pipeline

CI/CD Pipeline for a Basic Calculator app using Jenkins and Docker

## Steps:

1. Configured Jenkins with Docker using Docker Plugins available in Jenkins.
2. Docker by default runs in Linux containers, hence installed WSL2 for its running.
3. Created a Sample Calculator App.
4. Added Tests using `pytest` package in python.
5. Built a CI/CD pipeline using Jenkinsfile.
6. Containerized it using Dockerfile.
7. Built and Tested the entire pipeline.

## Webhooks

-   Added webhooks to automate the pipeline execution by adding triggers whenever commits are pushed to git.

## Steps:

1. Used ngrok to create public URL of the Jenkins localhost.
2. Configured Jenkins to listen to the git repository for new commits pushed.
3. Added webhook in GitHub using the public URL.
4. Tested the pipeline execution after pushing commits.
