# Webots

For Webots `R2022a` on Ubuntu `18.04 LTS`

## Install Webots

know your Linux OS with the following command :
```bash
cat /etc/issue
```

### With .deb archive

Simply open .deb file.Your OS will popup a windows to install the package.

### With .tar.gz archive

Download `.tar.gz` Webots file https://cyberbotics.com/ for Ubuntu `18.04 LTS`

Add Webots `R2022a` to you system `PATH`
```bash
mkdir ~/Apps
tar -xvf ~/Téléchargements/webots-R2022a-x86-64.tar.bz2 -C ~/Apps
```

Setup environment using `.bashrc` user environment variable
```bash
echo 'export PATH=$PATH:~/Apps/webots' >> ~/.bashrc
echo 'alias webots="webots & disown"' >> ~/.bashrc
echo 'export WEBOTS_HOME=/home/$(whoami)/Apps/webots' >> ~/.bashrc
echo 'export WEBOTS_CONTROLLER=${WEBOTS_HOME}/lib/controller/' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=${WEBOTS_HOME}/lib/controller' >> ~/.bashrc
echo 'export PYTHONPATH=${WEBOTS_HOME}/lib/controller/python36' >> ~/.bashrc
source ~/.bashrc
```

Verify variables
```bash
file $WEBOTS_HOME
file $WEBOTS_CONTROLLER
file $LD_LIBRARY_PATH
file $PYTHONPATH
```

## Play with Webots

### **1 - Start Webots from a terminal**

Following commands will detach webots from your current shell
```bash
# with 'disdown' command
disown --help
webots seatech_simu/worlds/seatech_simu.wbt & disdown

# with 'nohup' command
nohup --help
nohup webots seatech_simu/worlds/seatech_simu.wbt &
```

### **2 - Create your first Webots Simulation**

Follow [First Webots tutorial](https://cyberbotics.com/doc/guide/tutorial-1-your-first-simulation-in-webots?tab-language=python#create-a-new-world). 

* Name the project `seatech_simu`
* Add `e-puck` Robot to the simulation.

Here is the full list of [Webots Robots](https://cyberbotics.com/doc/guide/robots?tab-language=python)

### **3 - Create your first Webots Controller**

Follow [First Webots controller](https://cyberbotics.com/doc/guide/tutorial-1-your-first-simulation-in-webots?tab-language=python#create-a-new-controller)

Name the controller `seatech_base_controller`

### **4 - Start a Python Controller outside of Webots**

**IMPORTANT**: Python environment must be setup

To allow `VS Code` to start the controller instead of Webots, set the controller of the robot to <extern> and set the environment variables as explained in the [Running Extern Robot Controllers chapter](https://cyberbotics.com/doc/guide/running-extern-robot-controllers?tab-language=python).

```bash
# then execute your controller
cd my_project
python3 my_webots_controller.py
```

## Configure VS Code

Using `.env` environment variable file with **VS Code**
```bash
# use .env file for VS Code
sed "s/XXXXXX/$(whoami)/" .env
cp .env /path/of/my_project/.env
```