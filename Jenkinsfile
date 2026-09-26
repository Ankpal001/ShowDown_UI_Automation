pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checkout stage'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest -v -s --browser chrome --headless'
            }
        }
    }
}