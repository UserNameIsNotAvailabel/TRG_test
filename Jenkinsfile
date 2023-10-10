stage('Build') {
    steps {
        script{
            def current_image = docker.build("simple_docker:${env.BUILD_ID}", "./docker_path/")
            withCredentials([[$class: 'AmazonWebServicesCredentialsBinding',
                            accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                            credentialsId: '<magic_id>',
                            secretKeyVariable: 'AWS_SECRET_ACCESS_KEY']]) {
                sh "aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin ${env.REGISTRY}"
                docker.withRegistry("https://${env.REGISTRY}") {
                    current_image.push()
                }
            }
        }
    }
}
