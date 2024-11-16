# Sample-Pipeline-For-App-Deployment
Creating a basic deployment pipeline involves configuring tools like Git, Jenkins, Docker and testing frameworks. Below are the detailed steps for setting up and implementing a deployment pipeline with development, staging, and production environments.

1. Prerequisites
   Install Required Tools:
     1. Install Git (By default installed in Ubuntu server)
     2. Install Jenkins
     3. Install Docker

   Configure Git Repository:
   ```
   git clone https://github.com/kausalyanp/pipeline-app.git
   cd pipeline-app
   ```
   Directory Structure
   ```
   simple-web-app/
   │
   ├── app.py
   ├── templates/
   │   ├── index.html
   │
   ├── static/
   │   ├── styles.css
   │
   ├── requirements.txt
   |
   ├── tests/
   │   ├── __init__.py
   │   ├── test_app.py
   ├── README.md
   └── .gitignore
   ```
   Set up remote branches for development, staging, and production
   ```
   git checkout -b development
   git push origin development

   git checkout -b staging
   git push origin staging

   git checkout -b production
   git push origin production
   ```
   Create a virtual environment and install dependencies (install everything inside git folder)
   ```
   sudo apt update
   sudo apt install python3 python3-pip -y
   python3 --version
   pip3 --version
   pip install pytest-flask    #install flask
   pip install pytest       #install pytest for testing
   pytest --version
   sudo apt install python3-venv -y  # Install virtual environment package
   pip install -r requirements.txt #installs flask
   ```
2. Create the Pipeline Configuration
   Jenkins Setup:
   Access Jenkins: http://<your-server-ip>:8080.

3. Set Up a Virtual Environment (Optional but Recommended)
   ```
   python3 -m venv venv             # Create a virtual environment
   source venv/bin/activate         # Activate the virtual environment
   ```

4. Create Deployment Script
   Make the deploy.sh script executable:
   ```
   chmod +x deploy.sh
   ```
   
6. Pipeline Execution Steps
   Test: Executes test cases inside environment (e.g., unit tests, integration tests).
   ```
   pytest tests/
   ```

7. Add Your Jenkins User to the Docker Group (outside git folder)
   ```
   id jenkins   #Identify the Jenkins User
   sudo usermod -aG docker jenkins #Add Jenkins User to the Docker Group
   groups jenkins   #Verify that the jenkins user is now part of the docker group
   sudo systemctl restart jenkins  #Restart Jenkins Service
   ```
   (OPTIONAL STEP) Grant your user access to Docker by adding them to the docker group:
   Add your user to the docker group:
   ```
   sudo usermod -aG docker $USER 
   newgrp docker   #Apply the changes: Log out of your current session and log back in, or run
   docker ps       #Verify access: Run a Docker command without sudo
   ```
   Check Group Permissions on the Docker Socket
   Ensure the Docker socket has the correct group ownership:
   ```
   ls -l /var/run/docker.sock
   ```
   Expected output:
   srw-rw---- 1 root docker 0 <timestamp> /var/run/docker.sock


Notes:
  1. Use Uubunu server with 22.04-amd64-server, storage required is 25 GiB
  2. Enable All TCP Port in Security Groups
  3. To exit or deactivate the virtual environment in Python, simply run the following command:
     ```
     deactivate
     ```
  4. Run the which command to locate the pytest binary: (This path is required to add in Jenkinsfile while running the pytest)
     ```
     which pytest  #example path: /usr/local/bin/pytest
     ```
  5. Clean Up Unused Docker Containers and images
     ```
     docker ps -a
     docker stop <container-id>
     docker rm <container-id>
     docker rmi <image-id>
     ```
