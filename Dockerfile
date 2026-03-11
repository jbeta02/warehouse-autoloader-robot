FROM osrf/ros:humble-desktop

# Prevent interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install ROS packages needed for the project
RUN apt update && apt install -y \
    sudo \
    nano \
    ros-humble-joint-state-publisher-gui \
    ros-humble-ros2-control \
    ros-humble-ros2-controllers \
    ros-humble-gazebo-ros2-control \
    ros-humble-slam-toolbox \
    ros-humble-navigation2 \
    ros-humble-nav2-bringup \
    ros-humble-moveit \
    ros-humble-moveit-resources-panda-moveit-config \
    ros-humble-franka-msgs \
    ros-humble-franka-description \
    python3-colcon-common-extensions \
    python3-rosdep \
    git \
    && rm -rf /var/lib/apt/lists/*

# Initialize rosdep
RUN rosdep init || true
RUN rosdep update

# Create a user that matches host UID/GID
ARG USERNAME=dev
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers


# Set workspace permissions
RUN mkdir -p /workspace && chown -R $USERNAME:$USERNAME /workspace

USER $USERNAME
WORKDIR /workspace

# Automatically source ROS
RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc