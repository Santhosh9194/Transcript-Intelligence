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
                sh 'python validate_dataset.py'
            }
        }

        stage('Topic Categorization') {
            steps {
                sh 'python topic_categorization.py'
            }
        }

        stage('Sentiment Analysis') {
            steps {
                sh 'python sentiment_analysis.py'
            }
        }

        stage('Bonus Insights') {
            steps {
                sh 'python bonus_insights.py'
            }
        }

        stage('Generate Report') {
            steps {
                sh 'python generate_report.py'
            }
        }
    }
}
