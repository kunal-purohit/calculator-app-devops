pipeline {
    agent {
        docker {
            image 'python:3.9-slim'
            args '-u root:root -v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

    environment {
        DOCKERHUB_CREDENTIALS = 'docker-credentials'
        DOCKERHUB_REPO = "kunal1323/calculator-app"
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh '''
                    apt-get update && apt-get install -y docker.io
                    pip install --no-cache-dir -r requirements.txt
                '''
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
                    dockerImageLatest.inside {
                        sh 'pytest tests/ --maxfail=1'
                    }
                }
            }
        }

        stage('Push Image to DockerHub') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.dockerhub.com', DOCKERHUB_CREDENTIALS) {
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
    }
}

