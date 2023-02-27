## *********************************************************
##
## File autogenerated for the camera_laser_calibration package
## by the dynamic_reconfigure package.
## Please do not edit.
##
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'name': 'Default', 'type': '', 'state': True, 'cstate': 'true', 'id': 0, 'parent': 0, 'parameters': [{'name': 'Info', 'type': 'str', 'default': 'When you choose Save, it will save the laser_coor and image octomatically!Remember Modify the laser_coor according rviz', 'level': 0, 'description': 'How to use!', 'min': '', 'max': '', 'srcline': 273, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator.py', 'edit_method': '', 'ctype': 'std::string', 'cconsttype': 'const char * const'}, {'name': 'range_min', 'type': 'int', 'default': -140, 'level': 0, 'description': 'The min angle of laser', 'min': -140, 'max': 140, 'srcline': 273, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'range_max', 'type': 'int', 'default': 140, 'level': 0, 'description': 'The max angle of laser', 'min': -140, 'max': 140, 'srcline': 273, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'laser_coor', 'type': 'str', 'default': '0.0, 0.0', 'level': 0, 'description': 'x y', 'min': '', 'max': '', 'srcline': 273, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator.py', 'edit_method': '', 'ctype': 'std::string', 'cconsttype': 'const char * const'}, {'name': 'Save', 'type': 'bool', 'default': False, 'level': 0, 'description': 'Save this data?', 'min': False, 'max': True, 'srcline': 273, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator.py', 'edit_method': '', 'ctype': 'bool', 'cconsttype': 'const bool'}], 'groups': [], 'srcline': 245, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator.py', 'class': 'DEFAULT', 'parentclass': '', 'parentname': 'Default', 'field': 'default', 'upper': 'DEFAULT', 'lower': 'groups'}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

