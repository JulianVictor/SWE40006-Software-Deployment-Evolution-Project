pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "julianjee/cat-facts-app"
        EC2_HOST = "54.165.71.97"
        EC2_USER = "ec2-user"
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/JulianVictor/SWE40006-Software-Deployment-Evolution-Project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t $DOCKER_IMAGE .'
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    script {
                        sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                        sh 'docker push $DOCKER_IMAGE'
                    }
                }
            }
        }

        stage('Deploy to EC2') {
            steps {
                sshagent(['ec2-key']) {
                    sh '''
                    ssh -o StrictHostKeyChecking=no $EC2_USER@$EC2_HOST << EOF
                      docker pull $DOCKER_IMAGE
                      docker stop cat-facts-container || true
                      docker rm cat-facts-container || true
                      docker run -d --name cat-facts-container -p 80:5000 $DOCKER_IMAGE
                    EOF
                    '''
                }
            }
        }
    }
}
