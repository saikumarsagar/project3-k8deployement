pipeline {
    agent {
  label 'java'     // running pipeline on worker node
}

    stages {
        stage('check out from SCM') {
            steps {
                git 'https://github.com/saikumarsagar/project1-docker.git'
            }
        }

    stage('MVN Build and Junit testing by MVN') {
            steps {
             sh 'mvn clean package'
              junit 'target/surefire-reports/*.xml'
            }
        } 
    stage('Docker build') {
            steps {
             sh 'sudo docker build -t saidocker2048/project:1.0 .'
            }
        }
        
     stage('Running Docker container') {
            steps {
              sh 'sudo docker run -dt -p 8090:8080 saidocker2048/project:1.0'
            }
        }   
     stage('Pushing Image to docker hub') {
            steps {
            withCredentials([string(credentialsId: '6636d3c5-1154-4ac0-8d3d-5f5649a671b7', variable: 'dockerpwd')])
            {
            sh "sudo docker login -u saidocker2048 -p ${dockerpwd}"
            sh 'sudo docker push saidocker2048/project:1.0'
            }
            }
        }  
        
          
    }
}
