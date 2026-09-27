pipeline {

    agent any

    environment {
        TEST_PASSWORD = credentials('TEST_PASSWORD')
    }

    stages {

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest -v -s --browser chrome --headless --alluredir=allure-results'
            }
        }
    }
    post {
    always {
        archiveArtifacts artifacts: 'screenshots/**/*', allowEmptyArchive: true
        archiveArtifacts artifacts: 'allure-results/**/*', allowEmptyArchive: true
    }
  }
}