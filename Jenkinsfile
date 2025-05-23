pipeline {
    agent any

    stages {
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
                sshagent (credentials: ['ec2-key']) {
                    sh 'ssh -o StrictHostKeyChecking=no ubuntu@54.226.89.1 "docker pull julianjee/cat-facts-app:latest && docker stop cat || true && docker rm cat || true && docker run -d -p 5000:5000 --name cat julianjee/cat-facts-app:latest"'
                }
            }
        }


    post {
        success {
            echo '✅ All stages completed successfully!'
        }
        failure {
            echo '❌ One or more stages failed. Check the console output.'
        }
    }
}
