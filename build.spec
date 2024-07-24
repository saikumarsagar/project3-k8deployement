
version: 0.2

env:
  variables:
    S3_BUCKET: "artifact121212"  # Replace with your actual S3 bucket name
    DEPLOYMENT_PATH: "allartifacts"  # Replace with your desired deployment path

phases:
  install:
    runtime-versions:
      java: corretto11  # Specify the Java runtime version
    commands:
      - echo Installing Maven...
      - mvn --version

  pre_build:
    commands:
      - echo Running pre-build steps...
      - mvn clean

  build:
    commands:
      - echo Building the application...
      - mvn install

  post_build:
    commands:
      - echo Running post-build steps...
      - aws s3 sync target/ s3://$S3_BUCKET/$DEPLOYMENT_PATH --delete

artifacts:
  files:
    - target/**/*

cache:
  paths:
    - /root/.m2/**/*  # Cache Maven dependencies to speed up subsequent builds
