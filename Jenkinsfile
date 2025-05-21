pipeline {
  agent any
  stages {
    stage('Build Docker Image') {
      steps {
        sh 'docker build -t yourusername/sample-app .'
      }
    }
    stage('Push to Docker Hub') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
          sh 'docker login -u $USERNAME -p $PASSWORD'
          sh 'docker push yourusername/sample-app'
        }
      }
    }
    stage('Deploy to EC2') {
      steps {
        sshagent (credentials: ['ec2-key']) {
          sh 'ssh -o StrictHostKeyChecking=no ec2-user@your-ec2-ip "docker pull yourusername/sample-app && docker stop app || true && docker rm app || true && docker run -d -p 80:3000 --name app yourusername/sample-app"'
        }
      }
    }
    stage('Run Selenium Tests') {
      steps {
        sh 'python3 test_app.py'  // Python script to run Selenium
      }
    }
  }
}
