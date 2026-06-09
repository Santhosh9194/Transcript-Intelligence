pipeline {

    agent any

    stages {

        stage('Install') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Validate Dataset') {
            steps {
                sh 'python scripts/validate_dataset.py'
            }
        }

        stage('Topic Categorization') {
            steps {
                sh 'python scripts/topic_categorization.py'
            }
        }

        stage('Sentiment Analysis') {
            steps {
                sh 'python scripts/sentiment_analysis.py'
            }
        }

        stage('Bonus Insights') {
            steps {
                sh 'python scripts/bonus_insights.py'
            }
        }

        stage('Generate Report') {
            steps {
                sh 'python scripts/generate_report.py'
            }
        }
    }
}