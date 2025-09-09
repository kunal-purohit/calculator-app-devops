pipeline {
    agent any // Runs on the main Jenkins node or any available agent.

    stages {
        stage('Run Unit Tests') {
            // Use a specific Docker image as the build environment for this stage.
            // Jenkins will automatically pull this image and run the steps inside it.
            agent {
                docker { image 'python:3.9-slim' }
            }
            steps {
                echo 'Running tests inside a Python container...'
                // Install dependencies and run pytest
                sh 'pip install pytest'
                sh 'pytest tests/'
            }
        }
        stage('Build Docker Image') {
            steps {
                echo 'Building the application Docker image...'
                // The 'bat' command is for Windows agents. Use 'sh' for Linux.
                // Builds a Docker image using the Dockerfile in the workspace.
                bat 'docker build -t my-calculator-app:latest .'
            }
        }
        stage('Sanity Check') {
            steps {
                echo 'Running a quick check on the new Docker image...'
                // Run the newly built image to see its output.
                bat 'docker run --rm my-calculator-app:latest'
            }
        }
    }
    post {
        always {
            echo 'Pipeline finished.'
            // Clean up old containers and images to save space
            bat 'docker image prune -f'
        }
    }
}
