/*pipeline {
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
}*/
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

        stage('Install Dependencies') {
            steps {
                script {
                    sh 'pip install pytest'
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

            // Send email notification
            emailext (
                subject: 'Jenkins Build Successful: All Tests Passed',
                body: 'The Jenkins pipeline ran successfully, and all tests passed!',
                to: 'rajeshunique.31@gmail.com'
            )
        }
    }
}
