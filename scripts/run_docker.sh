#!/bin/bash

xhost +local:docker

docker run -it \
--env DISPLAY=$DISPLAY \
--volume /tmp/.X11-unix:/tmp/.X11-unix \
--volume $(pwd):/workspace \
warehouse_robot_env