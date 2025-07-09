import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/don/four_drive_mecanum_robot/install/four_drive_mecanum_robot_description'
