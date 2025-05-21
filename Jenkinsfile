pipeline {
    agent any

    stages {
        stage('Checkout') {
    steps {
        git credentialsId: 'github-pat', url: 'https://github.com/yourusername/devops-demo-pipeline.git'
    }
}
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run App') {
            steps {
                sh 'nohup python3 app.py &'
            }
        }
    }
}
