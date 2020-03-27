"""
    1. 读取配置文件时，都是字符串格式的
    2. 有些本身是int或bool类型的，放在这个类里直接解析成相应格式
    3. 对于路径，解析成字符串
"""

import configparser
import pathlib


project_root = pathlib.Path(__file__).parent.parent
default_configure_dir = project_root.joinpath('conf').absolute()

class Configure(object):
    def __init__(self, config_dir):
        config = configparser.ConfigParser(allow_no_value=True)
        # 读取配置文件
        config.read(config_dir.joinpath('server.ini'))

        # 获得字符串
        self.strtype = config.get('server', 'strtype')

        # 获得bool类型
        self.booltype = config.getboolean('server','booltype')

        # 获得int类型
        self.inttype = config.getint('server', 'inttype')

        # 获得float类型
        self.floattype = config.getfloat('server', 'floattype')

        # 解析路径--字符串
        self.pathtype = pathlib.Path(config.get('server', 'pathtype')).resolve()
        self.LoggingConfPath = pathlib.Path(config.get('server', 'LoggingConfPath')).resolve()
