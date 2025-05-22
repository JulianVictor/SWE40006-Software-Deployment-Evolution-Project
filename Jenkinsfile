pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'julianjee/cat-facts-app'
        DOCKER_TAG = "${env.BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'export DOCKER_BUILDKIT=1'
                    sh "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(
                        credentialsId: 'dockerhub-creds',
                        passwordVariable: 'DOCKER_PASS',
                        usernameVariable: 'DOCKER_USER'
                    )]) {
                        sh "echo ${DOCKER_PASS} | docker login -u ${DOCKER_USER} ${DOCKER_PASS}"
                        sh "docker push ${DOCKER_IMAGE}:${DOCKER_TAG}"
                    }
                }
            }
        }

        stage('Deploy to EC2') {
            steps {
                script {
                    sshagent(['ec2-key']) {
                        sh """
                            ssh -o StrictHostKeyChecking=no ubuntu@3.87.77.121 << EOF
                            docker pull ${DOCKER_IMAGE}:${DOCKER_TAG}
                            docker stop cat-facts-app || true
                            docker rm cat-facts-app || true
                            docker run -d --name cat-facts-app -p 80:5000 ${DOCKER_IMAGE}:${DOCKER_TAG}
                            EOF
                        """
                    }
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
