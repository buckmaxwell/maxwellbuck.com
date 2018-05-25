#!groovy
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
                /* WEBHOOK TEST */

                sh 'git clone https://github.com/buckmaxwell/maxwellbuck.com.git'

                sh 'echo "Installing python requirements..."'
                sh 'cd maxwellbuck.com'
                sh 'pip install grip==4.5.2'

                sh 'echo "Running build script..."'
                sh './build.sh'
                sh 'echo "Build successful!"'


                sh 'echo "Copying site to host..."'
                sshagent (credentials: ['build-ssh']) {
                  sh 'scp -o StrictHostKeyChecking=no -r zipped_site/* max@maxwellbuck.com:/var/www/html/staging'
                }
                sh 'echo "Staging successfully deployed..."'
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
