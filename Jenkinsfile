pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Setting up environment...'
                sh 'python3 --version'
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'python3 test.py'
            }
        }
    }
}
