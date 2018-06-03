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
                FAKE_ENV = "fakeFAKEfake"
            }
            steps {
                sh 'echo "Beginning BUILD..."'
                sh 'printenv'

                sh 'echo "Installing python requirements..."'
                sh 'pip install grip==4.5.2'

                sh 'echo "Running build script..."'
                script {
                  if ("$env.BRANCH_NAME" == 'develop') {
                    sh './build.sh staging'
                  }
                  else {
                    sh './build.sh'
                  }
                }

                
                sh 'echo "Build successful!"'
            }
        }
        stage('test') {
            steps {
                sh 'echo "Beginnning TEST..."'
                sh 'cd zipped_site'
                sh 'cd ..'
                sh 'echo "stash successfully opened"'
                sh 'echo "listing contents of static"'
                sh 'ls zipped_site/static'
            }
        }
        stage('deploy') {
            steps {
                script {
                  if ("$env.BRANCH_NAME" == 'master') {
                    sh 'echo "Deploying maxwellbuck.com..."'
                    sh 'echo "Translating urls to staging versions..."'
                    sh 'echo "Copying site into place..."'
                    sshagent (credentials: ['build-ssh']) {
                      sh 'scp -o StrictHostKeyChecking=no -r zipped_site/* max@maxwellbuck.com:/var/www/html'
                      sh 'scp -o StrictHostKeyChecking=no -r nginx_config/* max@maxwellbuck.com:/etc/nginx/sites-enabled'
                    }
                    sh 'echo "Success! maxwellbuck.com has been deployed."'
                  }
                  else if ("$env.BRANCH_NAME" == 'develop') {
                    sh 'echo "Copying site to staging directory..."'
                    sshagent (credentials: ['build-ssh']) {
                      sh 'scp -o StrictHostKeyChecking=no -r zipped_site/* max@maxwellbuck.com:/var/www/html/staging'
                      sh 'scp -o StrictHostKeyChecking=no -r nginx_config/* max@maxwellbuck.com:/etc/nginx/sites-enabled'
                    }
                    sh 'echo "Staging successfully deployed!"'
                  }
                  else {
                    sh 'echo "deploy stage ignored; you are not on master or develop."'
                  }
                }
                sh "sudo /var/lib/jenkins/jobs/maxwellbuck.com/scripts/restart-nginx.sh"
            }
        }

    }
}
