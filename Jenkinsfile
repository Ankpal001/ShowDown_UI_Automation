pipeline {

    agent any

    environment {
        TEST_PASSWORD = credentials('TEST_PASSWORD')
    }

    stages {

        stage('Check Docker') {
            steps {
                bat '''
                    docker --version
                    docker compose version
                '''
            }
        }

        stage('Build & Run Tests') {
            steps {
                bat '''
                    docker compose down --remove-orphans
                    docker compose up --build --abort-on-container-exit --exit-code-from test-runner
                '''
            }
        }
    }

    post {
        always {

            allure([
                results: [[path: 'allure-results']]
            ])

            archiveArtifacts(
                artifacts: 'screenshots/**/*',
                allowEmptyArchive: true
            )

            bat '''
                docker compose down --remove-orphans
            '''
        }
    }
}