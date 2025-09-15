pipeline {
    agent {
        docker {
            image 'python:3.9-slim'
            args '-u root:root -v /usr/bin/docker:/usr/bin/docker'
        }
    }

    environment {
        DOCKERHUB_CREDENTIALS = credentials('docker-credentials')
        DOCKERHUB_REPO = "kunal1323/calculator-app"
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install --no-cache-dir -r requirements.txt'
            }
        }

        // stage('Run Unit Tests') {
        //     steps {
        //         sh 'pytest tests/'
        //     }
        // }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImageLatest = docker.build("${env.DOCKERHUB_REPO}:latest")
                }
            }
        }

        stage('Test in built image') {
            steps {
                script {
                    dockerImage.inside {
                        sh 'pytest tests/ --maxfail=1'
                    }
                }
            }
        }

        stage('Push Image to DockerHub') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.dockerhub.com', "${DOCKERHUB_CREDENTIALS}") {
                        dockerImageLatest.push("latest")
                    }
                }
            }
        }
    }
    post {
        success {
            echo 'CI/CD Pipeline successfully completed.'
        }
        failure {
            echo 'Pipeline failed. Check logs!'
        }
        always {
            echo "Cleaning up local Docker image..."
            sh "docker rmi \"$DOCKERHUB_REPO:latest\" || true"
        }
    }
}

