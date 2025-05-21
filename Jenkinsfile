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

        stage('Install Python Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    ./venv/bin/pip install --upgrade pip
                    ./venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Run App') {
            steps {
                sh '''
                    nohup ./venv/bin/python app.py > app.log 2>&1 &
                    echo $! > app.pid
                '''
            }
        }
    }
}
