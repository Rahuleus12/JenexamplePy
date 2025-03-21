pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                script {
                    checkout scm
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh 'pytest test_calculate.py --tb=short'
                }
            }
        }
    }

    post {
        success {
            echo 'All tests passed successfully! 🎉'
            emailext(
                subject:"Successful build ${currentBuild.currentResult}: ${env.JOB_NAME} ${BUILD_NUMBER}",
                to:"rajeshunique.31@gmail.com",
                body:"${env.BUILD_URL}"
            )
        }
    }
}
