pipeline {
    agent any // Runs on the main Jenkins node or any available agent.

    stages {
        stage('Run Unit Tests') {
            steps {
                echo 'Running tests inside a Python container...'
                // Manually run the container and mount the workspace volume.
                // This gives us precise control over the path format.
                bat '''
                    docker run --rm -v "%WORKSPACE%:/app" -w /app python:3.9-slim sh -c "pip install pytest && pytest tests/"
                '''
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
