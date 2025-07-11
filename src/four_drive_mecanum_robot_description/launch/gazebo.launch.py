from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
import os
import xacro
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    robot_state_publisher = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('four_drive_mecanum_robot_description'), 'launch', 'bot.launch.py')])
        )

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')])
        )

    spawn_entity = Node(package='gazebo_ros', executable='spawn_entity.py',
        arguments=['-topic', 'robot_description',
                    '-entity', 'mecanum_robot',
                    '-z','0.05'],
        output='screen')

    mecanum_drive = Node(package='controller_manager', executable='spawner',
                         arguments=['mecanum_drive'])
    
    joint_broad = Node(package='controller_manager', executable='spawner',
                         arguments=['joint_broad'])

    return LaunchDescription([
        robot_state_publisher,
        gazebo,
        spawn_entity,
        mecanum_drive,
        joint_broad
    ])
