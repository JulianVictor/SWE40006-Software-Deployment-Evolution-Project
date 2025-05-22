pipeline {
    agent any

    environment {
        IMAGE_NAME = 'cat-facts-app'
    }

    stages {
        stage('Build') {
            steps {
                script {
                    echo '🔧 Building Docker image...'
                    sh 'docker build -t $IMAGE_NAME .'
                }
            }
        }

        stage('Test') {
            steps {
                echo '✅ (Placeholder) Running tests...'
                // 你可以在这里执行 Python 单元测试或其他验证
            }
        }

        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                script {
                    echo '🚀 Deploying Docker container...'
                    sh 'docker rm -f $IMAGE_NAME || true'
                    sh 'docker run -d --name $IMAGE_NAME -p 5000:5000 $IMAGE_NAME'
                }
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully.'
        }
        failure {
            echo '❌ Pipeline failed.'
        }
    }
}
