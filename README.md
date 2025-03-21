Since the assignment required a VM I have installed an Arch based system for ease of use and quick configuration. 

# In case of a proper install:
## 1.Install jdk17
```bash
sudo apt install openjdk-17-jdk #since most of our practice has been on ubuntu i have opted for its default manager here
```
## 2. Download Jenkins.war file from jenkins and install it using java:
```bash 
java -jar jenkins.war
```

# Installing and Running Jenkins on Arch Linux

## 1. Install Java
Jenkins requires Java to run. Install the LTS version:
```bash
sudo pacman -Sy jdk17-openjdk
```

## 2. Install Jenkins
Install Jenkins from the AUR using an AUR helper like `yay`:
```bash
paru -Sy jenkins
```

## 3. Start Jenkins Service
Enable and start the Jenkins service:
```bash
sudo systemctl enable jenkins
sudo systemctl start jenkins
```

## 4. Initial Setup
1. Get the initial admin password:
```bash
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```

2. Open your web browser and navigate to:
```
http://localhost:8080
```
3. Enter the initial admin password
4. Install suggested plugins
5. Create your admin user account
6. Configure Jenkins URL if required I chose not to change

## 5. Installing Python Tools
Install necessary Python packages:
```bash
sudo pacman -S python python-pytest
```

## 6. Configure Jenkins for Python

1. Go to "Manage Jenkins" → "Manage Plugins"
2. Install "Python" plugin

3. Go to "Manage Jenkins" → "Global Tool Configuration"
4. Add Python installation

## 7. Create a demo repository
I have used an old pytest code to test this out it is available at https://github.com/Rahuleus12/JenexamplePy    

## 8. Create Jenkins Pipeline
Configure the pipeline by creating a pipeline in jenkins accordingly:
1.Add the github project and add the repo address
2.Select Github hook trigger for GITScm polling
3.Configure Pipeline
3.1.Give it a definition and define the scm as preffered in this case git
3.2. Enter the Repository link and add credentials in case of private repository
3.3.Specify the branch of as main as required then specify the Jenkinsfile.

## 9. Run the Pipeline

 Click "Build Now" in your pipeline project or commit to the git repo for it to build, succeed and send an email notification.

