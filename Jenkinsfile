pipeline {
    agent { docker { 
            image "python:3.9-slim"
            args '-u root' 
        }
    } // Runs on the main Jenkins node or any available agent.

    stages {
        stage('Run Unit Tests') {
            steps {
                sh 'pip install pytest && pytest tests/'
            }
        }
    }
    post {
        success {
            echo 'Pipeline finished.'
        }
        failure {
            echo 'Pipeline failed. Check logs!'
        }
    }
}
