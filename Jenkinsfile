pipeline{
    agent none
    stages{
      agent {
        docker {
            image "python:3.10-alpine"
            args "-v /c/ProgramData/Jenkins/.jenkins/workspace/calculatrice:/src -w /src"
            reuseNode true
            
        }
      }
      stage("Installation des dépendances"){
          steps{
              sh "pip install -r requirements.txt"
          }
      }
        
      stage("Execution des tests"){
          steps{
              sh "python -m pytest test.py -v"
          }
      }
    }
}