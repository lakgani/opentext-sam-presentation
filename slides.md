---
theme: seriph
class: text-center
title: AWS SAM
lineNumbers: false
favicon: https://media.amazonwebservices.com/blog/2018/sam_squirrel_1.jpg
# force color schema for the slides, can be 'auto', 'light', or 'dark'
colorSchema: 'dark'
# syntax highlighter, can be 'prism' or 'shiki'
highlighter: 'prism'
fonts:
  sans: 'Roboto'
  serif: 'Roboto Slab'
  mono: 'Fira Code'
defaults:
  layout: 'center'
background: './images/background-1.png'
---


##  Simplify serverless workflow with 
# AWS SAM
---

# Why Serverless

<v-clicks>

![Traditional vs Serverless](/traditionalvsserverless1.webp)

</v-clicks>

---

# AWS Lambda

<v-click>

## Advantages

</v-click>

<v-clicks>

* No need to handle server provisioning and maintainance
* No need to pay for any resources if its not being used.
* No need to handle the scaling.

</v-clicks>

<v-click>

## Disadvantages

</v-click>

<v-clicks>

* Cold boot
* Increased development complexity
* run-time has upper cutoff at 15mins
* No hardware selection except for memory and cpu architecture

</v-clicks>

---

# Serverless primary usecases

<v-clicks>

* Event driven applications (S3, SNS, SQS, DynamoDB, etc)
* scheduled applications
* API

</v-clicks>

---

# Traditional development pattern

<v-clicks>

* Manually creating infra using AWS UI.
* Changing file locally and uploading everytime a change is done / Using Cloud9 tool to write the lambda functions.
* Write a lot of custom code to zip and deploy for CICD.

</v-clicks>

---

# AWS SAM to rescue

combination of 
* Template file
* cli


---

# SAM Key features
* Infrastructure as code.
* Local debugging and testing support
* View logs of Lambdas running on AWS
* real-time development in AWS
* Generate sample event payloads


---

# Prerequisites
* AWS account with necessary priviliges 
* AWS credentials configured for cli usage
* AWS SAM installed
* Docker (only for local dev setup)


---

# Infrastructure as code

<v-clicks>

* Time saving
* Repeatable
* Consistent
* ease of tracking changes (when paired with git)

</v-clicks>

---

# Infrastructure as code
## Supported resources 


* Lambda
* API Gateway 
* DynamoDB


---

# Infrastructure as code
## Example: Simple lambda template file

```yaml{0|1,2|3|4|5|6-11|12-20|all}
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Resources:
  HelloWorldFunction:
    Type: AWS::Serverless::Function
    Properties:
      CodeUri: hello_world/
      Handler: app.lambda_handler
      Runtime: python3.9
      Architectures:
        - x86_64
      Events:
        HelloWorld:
          Type: Api
          Properties:
            Path: /hello
            Method: get
```


---

# Infrastructure as code

## building

```shell
$ sam build
```
<v-clicks>

* Installs all the required dependencies for supported platforms like python, node etc
* package the code and dependencies as zip or docker imageas based on configuration

</v-clicks>

---




# Infrastructure as code
## Simplified deployment

```shell
$ sam deploy --template-file template.yml
             --stack-name <stack-name>
             --s3-bucket <bucket-name>
             --capabilities <capabilities>
             --confirm-changeset
```
<v-click>

Doesn't feel simple isn't it?

</v-click>



---

# Infrastructure as code

## deploy - guided mode

```shell
$ sam deploy --guided
```

<v-click>

![Guided mode](/public/sam-guided-form.jpg)

</v-click>


---

# Infrastructure as code
# deploy - samconfig.toml

```yaml
version = 0.1
[default]
[default.deploy]
[default.deploy.parameters]
stack_name = "gpendyala-sam-hello"
s3_bucket = "aws-sam-cli-managed-default-samclisourcebucket-tgzgwr7f4742"
s3_prefix = "gpendyala-sam-hello"
region = "ap-south-1"
confirm_changeset = true
capabilities = "CAPABILITY_IAM"
image_repositories = []
```

---

# Infrastructure as code

# delete a stack

```shell
$ sam delete --stack-name <stack-name>
```


---



# Local debugging and testing support

<v-click>

## Invoke lambdas with predefined events

```shell
$ sam local invoke "HelloWorldFunction" -e events/event.json
```

</v-click>

<v-click>

## Emulate API Gateway HTTP server locally
```shell
$ sam local start-api
```

</v-click>

---

# Generate sample event payloads

```shell
$ sam local generate-event
```




---

# View logs of Lambdas running on AWS

<v-click>

## Get logs of a lambda
```shell
$ sam logs -n mystack-HelloWorldFunction-1FJ8PD36GML2Q
```

</v-click>

<v-click>

## tail  logs of lambda 
```shell
$ sam logs -n HelloWorldFunction --stack-name mystack --tail
```
</v-click>

<v-click>

## filter logs of lambda
```shell
$ sam logs -n HelloWorldFunction --stack-name mystack --filter 'error'
```
</v-click>


---

# real-time deployment to AWS
```shell
$ sam sync
```

---

# Demo

---

# Other notable features
* Lambda layers
* tracing
* AWS CDK support


---

# Few issues
* Not all features are supported locally
* Real-time development in AWS is still slow for regular development tasks

---

# Popular alternatives
* Serverless framework
* Serveless stack (has a unique local debugging support which is miles faster than CDK)
