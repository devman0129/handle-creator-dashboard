# 1. Setup & Running Locally
## 1.1 Prerequisites
### 1.1.1 Python

Install Python3 and dependencies!

```bash
# Install Python3
$ sudo apt update
$ sudo apt install python3-pip

# Install python3-venv to set up virtual environment 
$ sudo apt install python3-venv
```

### 1.1.2 PostgreSQL
Install PostgreSQL DB
```bash
# Install PostgreSQL DB
$ sudo apt update
$ sudo apt install postgresql postgresql-contrib

# Check if it is installed and running successfully
$ sudo systemctl status postgresql
```
![PostgreSQL](images/postgre_running.png "Sign In")

## 1.2 DB Configuration

```bash
# Login to PostgreSQL using 'postgres' user
$ sudo su - postgres

# Access the shell
$ psql

# Check the connection information
$ \conninfo

# List databases
$ \l

# Create a new db
$ CREATE DATABASE webchat_db;

# Create a user and password
$ CREATE USER dash WITH ENCRYPTED PASSWORD 'admin12345';

# Grant all privileges to the user
$ GRANT ALL PRIVILEGES ON DATABASE webchat_db TO dash;
```

## 1.3 Setup & Running Project Locally

### 1.3.1 Project Configuration

```bash
# Clone project from Github
$ git clone https://github.com/Forte-AI/handle-creator-dashboard.git

# Create .env file and configure it
$ cd handle-creator-dashboard
$ touch .env

DB_NAME=
DB_USERNAME=
DB_PASSWORD=
DB_HOST=
DB_PORT=
OPENAI_API_KEY=
OPENAI_ORGANIZATION=
DJANGO_SECREAT_KEY=
```

### 1.3.2 DB migration & Running

```bash
# Setting virtual environment and activate
$ python3 -m venv venv
$ source venv/bin/activate

# Install packages
$ python3 -m pip install -r requirements.txt

# Migrate DB models
$ python3 manage.py migrate

# Creat a new superuser
$ python3 manage.py createsuperuser

# Run server
$ python3 manage.py runserver
```

# 2. Setup & Running on AWS EC2

## 2.1 Create a new AWS EC2 instance
You can create two kinds of EC2 instances based on Ubuntu AMI or Amazon Linux AMI

A new pem file will be created according to EC2 server. (askhandle-linux.pem)

```bash
    Public IPv4 DNS : ec2-54-196-68-195.compute-1.amazonaws.com
    Public IPv4 Address : 54.196.68.195
```

## 2.2 Allowing access using user name and password by Putty (or WinSCP)

```bash
# SSH login using the pem file
$ ssh -i askhandle-linux.pem ec2-user@ec2-54-196-68-195.compute-1.amazonaws.com

# Set configuration for SSH (/etc/ssh/sshd_config) (PasswordAuthentication no -> PasswordAuthentication yes)
$ sudo nano /etc/ssh/sshd_config

# Restart ssh daemon
$ sudo systemctl restart ssh

# Set a new password for default user (pwd : linux)
$ sudo passwd ec2-user
```
Now it's ready to login using user name (ec2-user) and password (linux) by Putty or WinSCP

## 2.3 Install & Setup Docker and Docker Compose

```bash
# Install & Enable Docker
$ sudo yum install docker -y
$ sudo systemctl enable docker.service
$ sudo systemctl start docker.service

# Add uesr to docker group
$ sudo usermod -aG docker ec2-user

# Add Docker-compose
$ sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose

# Add permission to execute
$ sudo chmod +x /usr/local/bin/docker-compose

# Check Docker & Docker-compose is running
$ docker --version
$ docker-compose --version
```

## 2.4 Copy cert & key file to EC2 (/etc/ssl)

```bash
$ scp -i askhandle-linux.pem askhandle.com.cert.pem ec2-user@ec2-54-196-68-195.compute-1.amazonaws.com:/home/ec2-user/     
$ scp -i askhandle-linux.pem askhandle.com.key.pem ec2-user@ec2-54-196-68-195.compute-1.amazonaws.com:/home/ec2-user/
$ sudo cp /home/ec2-user/askhandle.com.cert.pem /etc/ssl/
$ sudo cp /home/ec2-user/askhandle.com.key.pem /etc/ssl/
```

## 2.5 Project Deployment from Github

```bash
# Install Git
$ sudo yum install git -y
$ git --version

# Git clone
$ git clone https://github.com/Forte-AI/handle-creator-dashboard.git

# Build & Run
$ cd handle-creator-dashboard
$ docker-compose -f docker-compose.prod.yml up -d --build
$ docker-compose -f docker-compose.prod.yml up

# Check running on https://creator.askhandle.com/
```

