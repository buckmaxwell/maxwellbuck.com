pipeline {
    agent {
        docker {
            image 'ubuntu:16.04'
            args '-u root:sudo -v $HOME/workspace/myproject:/myproject'
        }
    }
    stages {
        stage('build') {
            steps {
                sh 'echo "Beginning BUILD..."'

                sh 'echo "Installing python..."'
                sh 'apt-get update -y'
                sh 'apt-get install -y python'
                sh 'apt-get install -y python-pip'

                sh 'echo "Installing perl..."'
                sh 'apt-get install -y perl'

                sh 'echo "Installing git..."'
                sh 'apt-get install -y git'
                
                sh 'echo "Cloning repository..."'
                sh 'git clone https://github.com/buckmaxwell/maxwellbuck.com.git'

                sh 'echo "Installing python requirements..."'
                sh 'cd maxwellbuck.com'
                sh 'pip install -r requests.txt'
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
