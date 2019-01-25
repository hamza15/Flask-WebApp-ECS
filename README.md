# Flask-WebApp-ECS

*This repository covers the deployment of an Anagram Solver as a web application deployed on AWS Fargate with the neccessary 
configuration files to deploy a Continuous Deployment (CD) pipeline. If you choose to fork this repo please make sure to setup
AWS IAM roles according to the services you provision. AWS has a detailed explanation of the required roles for setting up ECS
[here](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/IAM_policies.html).*


## Prerequisites

* Create a Docker image repository inside AWS ECR. This repo is where you will be pushing your new image into everytime new
code is committed in your github repo. 

* Create an ECS task definition that references your Docker image in ECS. The following is how your task definition should look:

```json
{
  "taskDefinition": {
    "family": "Anagram",
    "containerDefinitions": [
      {
        "name": "Anagram",
        "image": "your-repo-number.dkr.ecr.your-region.amazonaws.com/anagram:6a57b99",
        "cpu": 100,
        "portMappings": [
          {
            "protocol": "tcp",
            "containerPort": 80,
            "hostPort": 80
          }
        ],
        "memory": 128,
        "essential": true
      }
    ]
  }
}
```
* Create an ECS cluster and an ECS Service which consumes the task definition you just created in the previous step. 
