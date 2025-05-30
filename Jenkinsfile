pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'julianjee/cat-facts-app'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Check Docker Access') {
            steps {
                sh '''
                echo 🔍 Checking Docker access...
                docker ps
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                echo 🛠️ Building Docker image...
                docker build -t $DOCKER_IMAGE .
                '''
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([string(credentialsId: 'dockerhub-creds', variable: 'DOCKER_PASSWORD')]) {
                    sh '''
                    echo 🔐 Logging into Docker Hub...
                    echo $DOCKER_PASSWORD | docker login -u julianjee --password-stdin
                    echo 📦 Pushing image to Docker Hub...
                    docker push $DOCKER_IMAGE
                    '''
                }
            }
        }

        stage('Deploy to EC2') {
            steps {
                sshagent(['ec2-deploy-key']) {
                    sh '''
                    echo 🚀 Deploying to EC2...

                    ssh -o StrictHostKeyChecking=no ubuntu@18.234.87.16 << 'EOF'
                    DOCKER_IMAGE="julianjee/cat-facts-app"

                    echo 🐳 Pulling latest image...
                    docker pull "$DOCKER_IMAGE"

                    echo 🧹 Cleaning up old container (if exists)...
                    docker stop cat-facts-app || true
                    docker rm cat-facts-app || true

                    echo 🚀 Starting new container...
                    docker run -d -p 80:5000 --name cat-facts-app "$DOCKER_IMAGE"
                    EOF
                    '''
                }
            }
        }
    }

    post {
        failure {
            echo '❌ Deployment failed.'
        }
        success {
            echo '✅ Deployment succeeded.'
        }
    }
}
