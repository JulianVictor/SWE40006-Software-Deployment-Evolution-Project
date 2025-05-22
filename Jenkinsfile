pipeline {
    agent any
    
    environment {
        DOCKER_HUB_CREDENTIALS = credentials('docker-hub-credentials')
    }
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/your-repo/swe40006-project.git'
            }
        }
        
        stage('Test') {
            steps {
                sh 'python -m pip install -r requirements.txt'
                sh 'python -m pytest test_app.py'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("your-dockerhub-username/cat-facts-app:${env.BUILD_NUMBER}")
                }
            }
        }
        
        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
                        docker.image("your-dockerhub-username/cat-facts-app:${env.BUILD_NUMBER}").push()
                    }
                }
            }
        }
        
        stage('Deploy') {
            steps {
                sh 'docker-compose down || true'
                sh 'docker-compose up -d'
            }
        }
        
        stage('Smoke Test') {
            steps {
                sh 'python test_app.py'
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
        success {
            slackSend(color: "good", message: "Build ${env.BUILD_NUMBER} succeeded!")
        }
        failure {
            slackSend(color: "danger", message: "Build ${env.BUILD_NUMBER} failed!")
        }
    }
}
