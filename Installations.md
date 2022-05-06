### Install VSCode Editor 
```sh
sudo apt update
sudo snap install code --classic
```


### WADL - 


#### Assign 1 - html, css, js (net required for CDN)
```sh
Just net required
```
#### Assign 2 - javascript and any backend required (net required for CDN)
```sh
Just net required
```
#### Assign 3 - install GIT bash and account on github (net required for accessing github)
```sh
sudo apt update
sudo apt install git -y
git config --global user.name "<your_name>"
git config --global user.email "<your_email>"
```
#### Assign 4 - docker installation (net required to download docker images)
```sh
sudo apt update
sudo apt install snapd
sudo apt install snap
sudo snap install docker
sudo apt update
```
#### Assign 5 - npm, nvm, angular to be installed (net required to install npm packages)
```sh
sudo apt update && sudo apt upgrade
cd ~
wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
source ~/.nvm/nvm.sh 
nvm --version
```
Restart the terminal 
```sh
nvm install --lts
```
or
```sh
nvm install node
sudo npm install -g @angular/cli
```
#### Assign 6 - npm install (net required to install npm packages)
If node is already installed nothing to be installed here
else: 
```sh
sudo apt update && sudo apt upgrade
cd ~
wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
source ~/.nvm/nvm.sh 
nvm --version
```
Restart the terminal 
```sh
nvm install --lts
```
or
```sh
nvm install node
```
#### Assign 7 - MongoDB to be installed (net required to perform CRUD operations)
node to be installed (follow steps in assignment 6 if npm is not installed)
```sh
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list
sudo apt-get update
sudo apt-get install -y mongodb
```
To check whether mongo service is running or not
```sh
sudo systemctl status mongodb
```
#### Assign 8 - JQuery CDN or js files to be installed (net required for CDN)
Files to be downloaded from the following site:
```sh
https://jquerymobile.com/ 
```
#### Assign 9 - Account on AWS/Azure/GCP required to host the application (net required for accessing the console)
```sh
No installations required (just net required)
```


### CCL - 
#### Assign 1 - Install Google cloud SDK (net required for installing the supporting plugins)
Install cloud sdk from [here](https://cloud.google.com/sdk/docs/install)
Install Python from [here](https://www.python.org/downloads/)

#### Assign 2 - Install Python to be installed and SDK to be installed (net required view access the server launched)
```sh
sudo apt install python3 -y
```

#### Assign 3 - Cloudsim 4.0 and eclipse IDE required (net required for downloading downloading zip file of cloudsim)
```sh
sudo apt update
sudo apt install snapd
sudo apt install snap
sudo snap install eclipse --classic
sudo apt install default-jdk
```
Download Cloudsim from [here](https://github.com/Cloudslab/cloudsim/releases)

#### Assign 4 - Oracle VirtualBox and VMDK image of ubuntu 18.04 required (can use other image also) (net required for downloading oracle virtualbox)
```sh
sudo apt-get update
sudo apt-get install virtualbox -y
sudo apt-get install virtualbox—ext–pack -y
```
Click OK and YES... DONE
Install VMDK image from [here](https://drive.google.com/drive/u/0/folders/1me_nJJh0fvdDOXX3ew2jzGQpoP7f_iFt) or [here](https://app.vagrantup.com/bento/boxes/ubuntu-18.04)

#### Assign 5 - Account on AWS/Azure/GCP required (net required for accessing console for launching VM)
```sh
Just net required
```
#### Assign 6 - Account on AWS/Azure/GCP required and access to any PaaS service (net required for accessing console for launching PaaS Service)
```sh
Just net required
```
#### Assign 7 - Just Web browser required (net required for accessing the web browser for salesforce)
```sh
Just net required
```
#### Assign 8 - Account on Firebase and GCP required (net required for accessing console and performing queries)
```sh
npm to be installed and net connection required (follow assignment 6 WAD)
```
