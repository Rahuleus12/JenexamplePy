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
        }
    }
}
