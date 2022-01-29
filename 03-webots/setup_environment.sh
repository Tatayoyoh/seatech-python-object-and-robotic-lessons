export WEBOTS_HOME=/home/$(whoami)/Apps/webots
export WEBOTS_CONTROLLER=${WEBOTS_HOME}/lib/controller/
export LD_LIBRARY_PATH=${WEBOTS_CONTROLLER}
export PYTHONPATH=${WEBOTS_CONTROLLER}/python38