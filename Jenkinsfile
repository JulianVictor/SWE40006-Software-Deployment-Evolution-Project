pipeline {
  agent any

  stages {
    stage('Clone') {
      steps {
        git 'https://github.com/JulianVictor/SWE40006-Software-Deployment-Evolution-Project.git'
      }
    }

    stage('Build Docker') {
      steps {
        sh 'docker build -t julianjee/cat-facts-app .'
      }
    }

    stage('Run Container') {
      steps {
        sh 'docker run -d -p 5000:5000 --name cat-facts julianjee/cat-facts-app'
      }
    }

    stage('Selenium Test') {
      steps {
        sh 'pytest tests/selenium_test.py'
      }
    }
  }

  post {
    always {
      sh 'docker rm -f cat-facts || true'
    }
  }
}
