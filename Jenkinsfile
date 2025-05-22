pipeline {
    agent any

    environment {
        DEPLOY_BRANCH = 'main'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm 
            }
        }

        stage('Build') {
            steps {
                script {
                    sh 'docker build -t your-app .'
                }
            }
        }

        stage('Test') {
            steps {
                sh 'echo "Running tests..."'
            }
        }

        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                sh 'echo "Deploying..."'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
