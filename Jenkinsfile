pipeline {
    agent any

    environment {
        PROJECT_DIR = "/var/jenkins_home/workspace/travel-intelligence-pipeline"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Show Workspace') {
            steps {
                sh '''
                pwd
                ls -la
                '''
            }
        }

        stage('Python Version') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Create Virtual Environment') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                python -m pip install --upgrade pip
                '''
            }
        }

        stage('Install Requirements') {
            steps {
                sh '''
                . venv/bin/activate
                pip install -r requirements/common.txt
                pip install -r requirements/api.txt
                pip install -r requirements/streamlit.txt
                '''
            }
        }

        stage('Run ML Pipeline') {
            steps {
                sh '''
                . venv/bin/activate
                python -m src.pipeline.main_pipeline
                '''
            }
        }

        stage('Build Docker Images') {
            steps {
                sh '''
                sudo docker build -t travel-streamlit -f Dockerfile .
                sudo docker build -t travel-fastapi -f Dockerfile.api .
                '''
            }
        }

    }

    post {

        success {
            echo 'Travel Intelligence MLOps Pipeline Completed Successfully'
        }

        failure {
            echo 'Pipeline Failed'
        }

    }

}