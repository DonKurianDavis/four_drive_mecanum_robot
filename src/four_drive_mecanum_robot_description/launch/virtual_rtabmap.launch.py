from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, SetEnvironmentVariable, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.conditions import IfCondition, UnlessCondition
from launch_ros.actions import Node
import os
from launch.launch_description_sources import PythonLaunchDescriptionSource

from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    
    localization = LaunchConfiguration('localization')
    parameters = {'frame_id':'base_link',
        'use_sim_time':'True',
        'subscribe_depth':'True',
        'rtabmap_viz':'True',
        'use_action_for_goal':'True',
        'qos':'2',
        'Reg/Force3DoF':'true',
        'Optimizer/GravitySigma':'0',
        'database_path':'database/virtual_octomap.db',
        'subscribe_scan':'True',
        'scan_topic':'/scan',
        'approx_sync':'True',
        'camera_info_topic':'/camera/camera_info',
        'depth_topic':'/camera/depth/image_raw',
        'rgb_topic':'/camera/image_raw',
        # 'publish_tf':'False',
        'queue_size':'20',
        'RGBD/Octomap':'True',
        'Mem/SaveDepth16Format':"true",
        'Grid/Sensor':'1',
        'publish_tf_odom':'False',
        'map_topic':'/map',
        'odom_frame_id':'odom',
        'localization':localization
    }
    
    return LaunchDescription([
        DeclareLaunchArgument(
            'localization', default_value='false',
            description='Launch in localization mode.'),

        IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('rtabmap_launch'), 'launch', 'rtabmap.launch.py')]),
            launch_arguments=parameters.items()
        )
    
    ])