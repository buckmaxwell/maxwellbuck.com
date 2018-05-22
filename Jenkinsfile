pipeline {
    agent { docker { image 'ubuntu:16.04' } }
    stages {
        stage('build') {
            steps {
                sh 'echo "Beginning BUILD..."'
                sh 'echo "Installing python..."'
                sh 'sudo apt-get update -y'
                sh 'sudo apt-get install -y python'
                sh 'sudo apt-get install -y python-pip'
                sh 'echo "Installing perl..."'
                sh 'sudo apt-get install -y perl'
                sh 'sudo apt-get install -y curl'
                sh 'echo "Installing python requirements..."'
                sh 'sudo pip install -r requests.txt'
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
