pipeline {
    agent any

    environment {
        ORDER_IMAGE = "order-service:1.0"
        USER_IMAGE  = "user-service:1.0"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Order Service') {
            steps {
                dir('services/order-service') {
                    sh 'docker build -t $ORDER_IMAGE .'
                }
            }
        }

        stage('Build User Service') {
            steps {
                dir('services/user-service') {
                    sh 'docker build -t $USER_IMAGE .'
                }
            }
        }

        stage('Security Scan (Trivy)') {
            steps {
                sh '''
                trivy image $ORDER_IMAGE || true
                trivy image $USER_IMAGE || true
                '''
            }
        }
    }

    post {
        success {
            echo 'CI pipeline completed successfully'
        }
        failure {
            echo 'CI pipeline failed'
        }
    }
}
