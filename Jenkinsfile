pipeline {
    agent { dockerfile { 
            filename "Dockerfile"
        }
    } // Runs on the main Jenkins node or any available agent.

    stages {
        stage('Run Unit Tests') {
            steps {
                sh 'pytest tests/'
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
