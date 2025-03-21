pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout your code from version control
                git 'https://your-repo-url/jenkins-python-test.git'
            }
        }

        stage('Setup Python') {
            steps {
                // Set up Python environment
                sh 'python -m pip install pytest'
            }
        }

        stage('Run Tests') {
            steps {
                // Run Python tests
                sh 'python -m pytest test_calculator.py -v'
            }
        }
    }

    post {
        always {
            // Clean up workspace
            cleanWs()
        }
    }
}
