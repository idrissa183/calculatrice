pipeline{
    agent none
    stages{
      
      stage("Installation des dépendances"){
        agent {
        docker {
            image "python:3.10-alpine"
            args "-v /c/ProgramData/Jenkins/.jenkins/workspace/calculatrice:/src -w /src"
            reuseNode true
            
        }
      }
      steps{
          sh "pip install -r requirements.txt"
      }
      }
        
      stage("Execution des tests"){
        agent {
        docker {
            image "python:3.10-alpine"
            args "-v /c/ProgramData/Jenkins/.jenkins/workspace/calculatrice:/src -w /src"
            reuseNode true
            
        }
      }
      steps{
          sh "python -m pytest test.py -v"
      }
      }
    }
}