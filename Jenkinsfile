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

        stage('Install Dependencies') {
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
                    nohup python3 app.py > app.log 2>&1 &
                    echo $! > app.pid
                '''
            }
        }
    }
}
