pipeline {
    agent any

    stages {
        stage('CheckOut') {
            steps {
                git url: 'https://github.com/ssingh9631/Cloudnative/', branch: 'main'
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t ssingh/maingame:0.1 .'
            }
        }
        stage('Run') {
            steps {
                sh 'docker run -d --name game -p 5000:5000 ssingh/maingame:0.1'
            }
        }
        stage('Test') {
            steps {
                sh 'docker exec game python e2e.py'
            }
        }
        stage('Cleanup') {
            steps {
                sh 'docker stop game'
                sh 'docker rm game'
                sh 'docker rmi ssingh/maingame:0.1'
            }
        }
    }
}
