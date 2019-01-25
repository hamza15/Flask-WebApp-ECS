# Flask-WebApp-ECS

*This repository covers the deployment of an Anagram Solver as a web application deployed on AWS Fargate with the neccessary 
configuration files to deploy a Continuous Deployment (CD) pipeline with AWS CodePipeline. If you choose to fork this repo please make sure to setup
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
* Create an ECS cluster and an ECS Service which consumes the task definition you just created in the previous step. **You will create an Application Load Balancer as part of the service creation. Select target type as IP since AWS Fargate uses type IP.** 

## Build Process

Once the prerequisites have been deployed, we can build our Continuous Deployment Pipeline. *When setting up CodePipeline create service roles with the neccessary permissions.*

* The source stage is set to Github which is connected to your Pipeline using OAuth. Select your repository and the branch. Use web-hooks which will is also the AWS recommended path.

* At the build stage we use AWS CodeBuild and create a new project. We use managed image for the build environment, Ubuntu as the Operating System, Docker as Runtime and the latest runtime and image version. **We will be using our own buildspec file which is provided in the repo. Make sure to change the Repository URI to reflect your own repository.**

* At the deploy stage we select ECS where we choose the AWS ECS Cluster and Service we created in the prerequisite steps. 



### Once your pipeline kicks off and all the stages succeed, you should be able to hit the load balancer from your web browser and see your Anagram-Web-App up and running. 

