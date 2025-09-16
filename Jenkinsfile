pipeline {
    agent {
        docker {
            image 'docker:28.3.3-cli'
            args '-u root -v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

    environment {
        DOCKERHUB_CREDENTIALS = credentials('docker-credentials')
        DOCKERHUB_REPO = "kunal1323/calculator-app"
    }

    stages {
        stage('Install Dependencies & Run tests') {
            agent {
                docker { image 'python:3.9-slim' }
            }
            steps {
                sh '''
                    pip3 install --no-cache-dir -r requirements.txt
                    pytest tests/ --maxfail=1
                '''
            }
        }

        // stage('Run Unit Tests') {
        //     steps {
        //         sh 'python3 -m pytest tests/ --maxfail=1'
        //     }
        // }

        stage('Build Docker Image') {
            steps {
                // script {
                //     dockerImageLatest = docker.build("${env.DOCKERHUB_REPO}:latest")
                // }
                sh "docker build -t ${env.DOCKERHUB_REPO}:latest ."
            }
        }

        // stage('Test in built image') {
        //     steps {
        //         script {
        //             dockerImageLatest.inside {
        //                 sh 'pytest tests/ --maxfail=1'
        //             }
        //         }
        //     }
        // }

        stage('Push Image to DockerHub') {
            steps {
                // script {
                //     docker.withRegistry('https://registry.hub.docker.com', DOCKERHUB_CREDENTIALS) {
                //         dockerImageLatest.push("latest")
                //     }
                // }
                sh """
                    echo "${DOCKERHUB_CREDENTIALS_PSW}" | docker login -u "${DOCKERHUB_CREDENTIALS_USR}" --password-stdin
                    docker push ${DOCKERHUB_REPO}:latest
                """
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
            sh """
                docker logout
                docker rmi ${DOCKERHUB_REPO}:latest || true
            """
        }
    }
}
