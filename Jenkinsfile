pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/JulianVictor/SWE40006-Software-Deployment-Evolution-Project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t cat-facts-app .'
            }
        }

        stage('Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                    sh 'docker tag cat-facts-app julianjee/cat-facts-app:latest'
                    sh 'docker push julianjee/cat-facts-app:latest'
                }
            }
        }

        stage('Deploy on EC2') {
            steps {
                sh 'ssh -o StrictHostKeyChecking=no -i /path/to/deploy.pem ubuntu@54.165.71.97 "docker pull julianjee/cat-facts-app:latest && docker stop cat || true && docker rm cat || true && docker run -d -p 5000:5000 --name cat julianjee/cat-facts-app:latest"'
            }
        }

        stage('UI Tests') {
            steps {
                sh 'pytest tests/test_ui.py'
            }
        }
    }
}
