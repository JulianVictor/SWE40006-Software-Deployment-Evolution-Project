pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    credentialsId: 'github-pat',
                    url: 'https://github.com/JulianVictor/SWE40006-Software-Deployment-Evolution-Project.git'
            }
        }

        stage('Install System Dependencies') {
            steps {
                sh 'sudo apt update && sudo apt install -y python3-venv'
            }
        }

        stage('Install Python Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run App') {
            steps {
                sh '''
                    . venv/bin/activate
                    nohup python3 app.py > app.log 2>&1 &
                    echo $! > app.pid
                '''
            }
        }
    }
}
