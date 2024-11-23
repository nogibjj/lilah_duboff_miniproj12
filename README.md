[![Build and Push Docker Image](https://github.com/nogibjj/lilah_duboff_miniproj12/actions/workflows/build.yml/badge.svg)](https://github.com/nogibjj/lilah_duboff_miniproj12/actions/workflows/build.yml)


# Mini-Project 12: Dockerized Application
---
##### The purpose of this project is to create a python application containerized with a dockerfile. This project will demonstrate running the application within a docker container (using docker run terminal commands),and build a docker image in a CI/CD pipeline, which will be pushed to Docker Hub or other container management service.
---
### Requirements
- [x] Application Functionality
- [x] CI/CD
- [x] Docker Configuration

---
### File Structure
- Project Folder
    - .devcontainer
        - devcontainer.json
        - Dockerfile
    - .github
        - main.yml
    - .gitignore
    - app.py
    - Makefile
    - README.md
    - requirements.txt

---
### App setup
##### To get the app set up, a .env file must be used to hide dockerhub login information and the image name, for convenience. To activate the app from the terminal, a few Makefile commands must be run:

##### 1. Make login: this command takes hidden login information from github secrets (and/or a .env file) to login to Dockerhub

##### 2. Make build: this command will build the image, and upon opening Dockerhub, the user will be able to see both a container and an image

##### 3. Make run: this command "activates" the app from the docker container and image, and the Flask site will now be active for use

##### 4. Make clean: finally (and an optional command), this one will remove the docker image from the container, unless the user wants to delete it manually through the Docker app

#### Example of Running Make Build in the Terminal:
![alt text](screenshots/make_build.png)

#### Example of Running Make Run in the Terminal:
![alt text](screenshots/make_run.png)

---
### App Use
##### 

