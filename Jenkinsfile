node{
  stage('SCM Checkout'){
     git 'https://github.com/vishnu2198/python-jenkins-helloworld.git'
     }
  sshagent(['jenkinstom']) {
   stage('Installing Dependencies'){
     
    sh 'scp -o StrictHostKeyChecking=no /var/lib/jenkins/workspace/python_pipeline/*.py  ec2-user@34.202.157.47:/home/ec2-user/'
    //sh  "ssh  ec2-user@54.167.84.225 'ls' "
    sh  "ssh  ec2-user@34.202.157.47 'sudo  python autoimport.py' "
     //sh "python autoimport.py"
    
   }
    stage('Deploying python file in other instance'){
     sh  "ssh  ec2-user@34.202.157.47 'nohup python app.py &' "
      //sh "python app.py"
     }
     }
}
