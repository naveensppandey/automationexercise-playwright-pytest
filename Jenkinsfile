pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Install Playwright Browsers') {
            steps {
                bat 'playwright install chromium firefox'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest --junitxml=test-results.xml'
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true, testResultsPattern: 'test-results.xml'
        }
    }
}
