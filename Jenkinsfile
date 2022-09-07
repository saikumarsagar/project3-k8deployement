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
               // for 2nd time running job, to avoid conflicts removing previous builds and images
                sh 'sudo systemctl start docker '
              //  sh 'sudo docker stop javacal' 
                
                sh 'sudo docker rm -f javacal'
                sh 'sudo docker rm -f saidocker2048/project:1.0'
              // building docker image
             sh 'sudo docker build -t saidocker2048/project:1.0 .'
            }
        }
        
     stage('Running Docker container') {
            steps {
                
              sh 'sudo docker run -dt -p 8090:8080 --name=javacal saidocker2048/project:1.0'
            }
        }   
     stage('Pushing Image to Docker hub') {
            steps {
            withCredentials([string(credentialsId: '6636d3c5-1154-4ac0-8d3d-5f5649a671b7', variable: 'dockerpwd')])
            {
            //declared docker password, so that we can login to docker hub while pushing image
            sh "sudo docker login -u saidocker2048 -p ${dockerpwd}"
            sh 'sudo docker push saidocker2048/project:1.0'
            }
            }
        }  
            stage('k8 deployemnet') {
            steps {
                //used jenkins syntax genaratorand got below syntax, where it will connect to the k8 workstation where kops was insatlled and from there it will run deployment file.
           sshPublisher(publishers: [sshPublisherDesc(configName: 'k8server-eceusr', transfers: [sshTransfer(cleanRemote: false, excludes: '', execCommand: '''git pull;
kubectl apply -f /home/ec2-user/project3-k8deployement/k8deployemnt.yml''', execTimeout: 120000, flatten: false, makeEmptyDirs: false, noDefaultExcludes: false, patternSeparator: '[, ]+', remoteDirectory: '//home//ec2-user//project3-k8deployement', remoteDirectorySDF: false, removePrefix: '', sourceFiles: '')], usePromotionTimestamp: false, useWorkspaceInPromotion: false, verbose: true)])
            }     
            }
     
}
}
