# Webots

For Webots `R2022a` on Ubuntu `18.04 LTS`

## Install Webots

Download `.tar.gz` Webots file https://cyberbotics.com/

know your Linux OS with the following command :
```bash
cat /etc/issue
```

Add Webots `R2022a` to you system `PATH`
```bash
cd ~/Téléchargements
tar -xvf webots-R2022a-x86-64.tar.bz2
file webots
mkdir ~/Apps
mv webtos ~/Apps/webots
echo 'PATH=$PATH:~/Apps/webots' >> ~/.bashrc
```

## Create you first Webot Project

Follow [First Webots tutorial](https://cyberbotics.com/doc/guide/tutorial-1-your-first-simulation-in-webots?tab-language=python). 

Name the project `seatech_simu`

## Setup Python environment

### Using `.env` environment variable file with **VS Code**
```bash
# use .env file for VS Code
sed "s/<XXX>/$(whoami)/" .env
cp .env /path/of/my_project/.env
```

### **OR** Using `.bashrc` user environment variable
```bash
echo 'WEBOTS_HOME=/home/$(whoami)/Apps/webots' >> ~/.bashrc
echo 'WEBOTS_CONTROLLER=${WEBOTS_HOME}/lib/controller/' >> ~/.bashrc
echo 'LD_LIBRARY_PATH=${WEBOTS_CONTROLLER}' >> ~/.bashrc
echo 'PYTHONPATH=${WEBOTS_CONTROLLER}/python38' >> ~/.bashrc
```

## Configure a Webots Robot

Once the PyCharm project configured, you can start Webots and open the desired world. To allow PyCharm to start the controller instead of Webots, set the controller of the robot to <extern> and set the environment variables as explained in the [Running Extern Robot Controllers chapter](https://cyberbotics.com/doc/guide/running-extern-robot-controllers?tab-language=python).

## Start a Python Controller

```bash
# then execute your controller
cd my_project
python3 my_webots_controller.py
```