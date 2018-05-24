pipeline {
    agent any
    stages {
        stage('build') {
            agent {
                dockerfile {
                    filename 'Dockerfile'
                    dir 'docker/build'
                    args '-u root:sudo -v $HOME/workspace/myproject:/myproject'
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
                sh 'echo "Moving ssh keys..."'
                sh 'echo $PRIVATE_KEY > ~/.ssh/id_ecdsa'
                sh 'echo $PUBLIC_KEY > ~/.ssh/id_ecdsa.pub'

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
