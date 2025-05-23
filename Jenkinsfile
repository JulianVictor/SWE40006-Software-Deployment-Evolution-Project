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
                sh 'ssh -o StrictHostKeyChecking=no ubuntu@54.83.88.113 "docker pull julianjee/cat-facts-app:latest && docker stop cat || true && docker rm cat || true && docker run -d -p 5000:5000 --name cat julianjee/cat-facts-app:latest"'
            }
        }

        stage('Run Selenium Tests') {
      steps {
        sh ' python3 tests/selenium_test.py'  // Python script to run Selenium
      }
    }
  }
}
