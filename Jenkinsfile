pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                script {
                    docker.image('node:18.18.0-alpine3.18').inside {
                        sh 'node --version'
                    }
                }
            }
        }
    }
}

