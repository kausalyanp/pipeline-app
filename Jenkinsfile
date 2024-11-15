pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t my-app:${BUILD_NUMBER} .'
            }
        }
        stage('Setup Environment') {
            steps {
                sh '''
                    #!/bin/bash
                    python3 -m venv venv
                    pip install pytest
                '''
            }
        }
        stage('Test') {
            steps {
                sh '''
                    #!/bin/bash
                    pytest tests/
                '''  // Replace with your test command
            }
        }
        stage('Deploy to Development') {
            steps {
                sh './deploy.sh development'  // Script for deploying to development
            }
        }
        stage('Approval for Staging') {
            steps {
                input 'Deploy to Staging?'
            }
        }
        stage('Deploy to Staging') {
            steps {
                sh './deploy.sh staging'  // Script for deploying to staging
            }
        }
        stage('Approval for Production') {
            steps {
                input 'Deploy to Production?'
            }
        }
        stage('Deploy to Production') {
            steps {
                sh './deploy.sh production'  // Script for deploying to production
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: '**/target/*.war', fingerprint: true
        }
    }
}
