#!groovy
pipeline {

    agent {
        label 'auto-test-slave'
    }

    stages {

        stage('Setup') {
            steps {
                sh '''
                source .venv/bin/activate
                '''
            }
        }

        stage('Run') {
            steps {
                sh '''
                export PYTHONPATH=${WORKSPACE}
                source .venv/bin/activate
                python main.py run
                '''
            }
        }

    }

    post {
        success {
            //当此Pipeline成功时打印消息
            sh '''
            echo "测试任务全部成功"
            '''
        }
        failure {
            //当此Pipeline失败时打印消息
            sh '''
            echo "测试任务失败"
            '''
        }
    }
}

