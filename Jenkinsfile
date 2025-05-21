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
                // If you already preinstalled them manually, you can remove this stage
                sh '''
                    sudo apt update
                    sudo apt install -y python3 python3-pip python3-venv libgl1 libglib2.0-0
                '''
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
