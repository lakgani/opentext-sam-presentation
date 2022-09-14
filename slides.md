---
theme: seriph
class: text-center
title: AWS SAM
lineNumbers: false
favicon: https://media.amazonwebservices.com/blog/2018/sam_squirrel_1.jpg
fonts:
  sans: 'Roboto'
  serif: 'Roboto Slab'
  mono: 'Fira Code'
defaults:
  layout: 'center'
---

# AWS SAM


---
background: './images/background-1.png'
---​

# Why Serverless

<v-click>

## Advantages

</v-click>

<v-clicks>

* No need to pay for any resources if its not being used.
* No need to handle server provisioning and maintainance
* No need to handle the scaling.

</v-clicks>

<v-click>

## Disadvantages

</v-click>

<v-clicks>

* Cold boot
* Increased development complexity

</v-clicks>


---


# Types of serverless applications
* API
* Event driven applications
* scheduled applications


---

# Traditional development pattern and its issues
* Manually creating infra using AWS UI is not scalable.
* Changing file locally and uploading everytime a change is done / Using Cloud9 tool to write the lambda functions has its fair share of issues
* Need to write a lot of custom code to zip and deploy for CICD.


---

# AWS SAM to rescue
* Its a combination of 
  * Template file
  * cli


---

# SAM Key features
* Infrastructure as code.
* Local debugging and testing support
* Stream logs of Lambdas running on AWS
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
* Time saving
* Repeatable
* Consistent


---

# Supported resources 

* Lambda
* API Gateway 
* DynamoDB


---

# Example: Simple lambda

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

# Simplified deployment

`sam deploy`


---

# Local debugging and testing support

## Invoke lambdas with predefined events
`sam local invoke "HelloWorldFunction" -e event.json`

## Emulate API Gateway HTTP server locally
`sam local start-api`


---

# Generate sample event payloads

`sam local generate-event s3 [put/delete] --bucket <bucket> --key <key>`

```json {maxHeight:'100'}
{
  "Records": [
    {
      "eventVersion": "2.0",
      "eventSource": "aws:s3",
      "awsRegion": "us-east-1",
      "eventTime": "1970-01-01T00:00:00.000Z",
      "eventName": "ObjectCreated:Put",
      "userIdentity": {
        "principalId": "EXAMPLE"
      },
      "requestParameters": {
        "sourceIPAddress": "127.0.0.1"
      },
      "responseElements": {
        "x-amz-request-id": "EXAMPLE123456789",
        "x-amz-id-2": "EXAMPLE123/5678abcdefghijklambdaisawesome/mnopqrstuvwxyzABCDEFGH"
      },
      "s3": {
        "s3SchemaVersion": "1.0",
        "configurationId": "testConfigRule",
        "bucket": {
          "name": "gpendyala",
          "ownerIdentity": {
            "principalId": "EXAMPLE"
          },
          "arn": "arn:aws:s3:::gpendyala"
        },
        "object": {
          "key": "key",
          "size": 1024,
          "eTag": "0123456789abcdef0123456789abcdef",
          "sequencer": "0A1B2C3D4E5F678901"
        }
      }
    }
  ]
}
```


---

# Stream logs of Lambdas running on AWS

```shell
$ sam logs -n mystack-HelloWorldFunction-1FJ8PD36GML2Q
```

```shell
$ sam logs -n HelloWorldFunction --stack-name mystack --tail
```

```shell
$ sam logs -n HelloWorldFunction --stack-name mystack --filter 'error'
```


---

# real-time deployment to AWS
`sam sync`


---

# 

# Other notable features
* Lambda layers
* tracing


---

# Few issues
* Not all features are supported locally
* Real-time development in AWS is still slow for regular development tasks(Serverless Stack seems to be good alternative here)
