pipeline {
    agent any
    stages {
        stage('Check Docker Version') {
            steps {
                script {
                    // Вы можете выполнять команды Docker внутри этой оболочки
                    sh 'docker --version'
                }
            }
        }
    }
}

