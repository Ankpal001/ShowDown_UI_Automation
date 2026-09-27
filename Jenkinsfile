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

        stage('Check Workspace') {
    steps {
        bat '''
            echo ===== WORKSPACE =====
            dir
            echo ===== DOCKER COMPOSE FILE =====
            dir docker-compose.yml
        '''
    }
}
    }
}