//Jenkinsfile (Declarative Pipeline)
pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                sh 'echo "Fail!"; exit 1'
            }
        }
    }
    post {
        always {
            echo 'This always runs'
        }
        success {
            echo 'This only runs when successful'
        }
        failure {
            echo 'This only runs when failed'
        }
        unstable {
            echo 'This only runs when marked unstable'
        }
        changed {
            echo 'This only runs when the Pipeline’s state changes'
        }
    }
}
