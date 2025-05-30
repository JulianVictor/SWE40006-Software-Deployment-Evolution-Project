pipeline {
  agent any

  environment {
    DOCKER_IMAGE = 'julianjee/cat-facts-app'
  }

  stages {
    stage('Clone Repo') {
      steps {
        git 'https://github.com/JulianVictor/SWE40006-Software-Deployment-Evolution-Project.git'
      }
    }

    stage('Build Docker Image') {
      steps {
        sh 'docker build -t $DOCKER_IMAGE .'
      }
    }

    stage('Push to Docker Hub') {
      steps {
        withCredentials([string(credentialsId: 'dockerhub-creds', variable: 'DOCKER_PASSWORD')]) {
          sh '''
            echo $DOCKER_PASSWORD | docker login -u julianjee --password-stdin
            docker push $DOCKER_IMAGE
          '''
        }
      }
    }

    stage('Deploy to EC2') {
      steps {
        sshagent (credentials: ['ec2-key']) {
          sh '''
            ssh -o StrictHostKeyChecking=no ec2-user@54.165.71.97 "
              docker pull $DOCKER_IMAGE &&
              docker stop cat-facts-app || true &&
              docker rm cat-facts-app || true &&
              docker run -d -p 80:5000 --name cat-facts-app $DOCKER_IMAGE
            "
          '''
        }
      }
    }
  }

  post {
    success {
      echo '✅ Deployment completed successfully.'
    }
    failure {
      echo '❌ Deployment failed.'
    }
  }
}
