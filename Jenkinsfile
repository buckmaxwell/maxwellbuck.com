pipeline {
    agent any
    stages {
        stage('build') {
            agent {
                dockerfile {
                    filename 'Dockerfile'
                    dir 'docker/build'
                    args '-u root:sudo -v $HOME/workspace/myproject:/myproject'
                    additionalBuildArgs  "--build-arg BUILD_KEY=${env.BUILD_KEY} --build-arg BUILD_KEY_PUB=${env.BUILD_KEY_PUB}"
                }
            }
            environment {
                GITHUB_PASS = credentials('github-pass')
                PRIVATE_KEY = credentials('build-key')
                PUBLIC_KEY = credentials('build-key-pub')
            }
            steps {
                sh 'echo "Beginning BUILD..."'

                sh 'echo "Cloning repository..."'
                script {
                  try {
                    sh 'rm -r maxwellbuck.com'
                  }
                  catch (exc) {
                    sh 'echo "Cloning..."' 
                  }
                }

                sh 'echo "Move keys..."'
                sh "mkdir ~/.ssh"
                sh "echo ${env.BUILD_KEY} > ~/.ssh/id_ecdsa"
                sh "echo ${env.BUILD_KEY_PUB} > ~/.ssh/id_ecdsa.pub"
                sh "chmod 400 ~/.ssh/id_ecdsa"
                sh "cat ~/.ssh/id_ecdsa"

                sh 'echo "Copy dummy file to host"'
                sh 'touch fakeassdummy.txt'
                sh 'scp -o StrictHostKeyChecking=no fakeassdummy.txt max@maxwellbuck.com:'

                sh 'git clone https://github.com/buckmaxwell/maxwellbuck.com.git'

                sh 'echo "Installing python requirements..."'
                sh 'cd maxwellbuck.com'
                sh 'pip install -r requirements.txt'

                sh 'echo "Running build script..."'
                sh './build.sh'
            }
        }
        stage('test') {
            steps {
                sh 'echo "Beginnning TEST..."'
            }
        }
        stage('deploy') {
            steps {
                sh 'echo "Deploying maxwellbuck.com..."'
                sh 'echo "Success! maxwellbuck.com has been deployed."'
            }
        }

    }
}
