# Webots

For Webots `R2022a` on Ubuntu `18.04 LTS`

## Setup Python environment

```bash
# export some needed environment variables
source setup_environment.sh
```

OR

```bash
# use .env file for VS Code
cp .env /path/of/my_project/.env
```

## Configure a Webots Robot

Once the PyCharm project configured, you can start Webots and open the desired world. To allow PyCharm to start the controller instead of Webots, set the controller of the robot to <extern> and set the environment variables as explained in the [Running Extern Robot Controllers chapter](https://cyberbotics.com/doc/guide/running-extern-robot-controllers?tab-language=python).

## Start a Python Controller

```bash
# then execute your controller
cd my_project
python3 my_webots_controller.py
```