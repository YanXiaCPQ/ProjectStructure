# ProjectStructure
python通用目录结构和用法 


```
ProjectName
├── README.md              # 项目说明文档   
├── bin                    # 存放脚本，执行文件 
│   ├── Readme.md
│   ├── run_test.sh        # 运行单元测试
│   └── safe_server.sh     # 运行整个项目
├── conf                   # 配置文件目录
│   ├── logging.ini
│   └── server.ini
├── dosc                   # 说明文档
│   └── Readme.md
├── logs                   # 日志
│   └── Readme.md
├── server                 # 项目源码，包括测试源码
│   ├── cache              # 缓存目录
│   │   └── Readme.md
│   ├── config.py          # 读取配置文件（全局）
│   ├── controllers        # MVC中的controllers，根据需要取舍，下同
│   │   └── __init__.py
│   ├── __init__.py
│   ├── logger.py          # 设置日志格式（全局）
│   ├── __main__.py        # 程序入口
│   ├── models
│   │   └── __init__.py
│   │   └──orm.py          # mysql异步模块
│   │   └──mysqlModel.py   # mysql同步模块
│   ├── test               # 单元测试
│   │   └── __init__.py
│   └── views
│       └── __init__.py
├── requirements.txt       # 存放依赖的外部Python包列表
└── setup.py               # 安装、部署、打包的脚本
```


# 使用方式
这里都只是样例，需要按照实际需求进行修改。
这个框架减轻了不必要的重复造轮子，如配置问题、日志问题、数据库问题等。

1. 主要解决了统一配置问题，包括写配置的格式，解析配置的格式，参考
    * conf目录 ：写配置的格式 
    * config.py: 解析配置的格式
    * __main__.py ： 获取解析配置的方式
2. 解决了统一处理log问题，定义了log的样式，只需要参考样例进行配置就可以全局使用不同的log对象，满足同时写不同服务的log的需求，参考
    * conf/logging.ini : 配置log样式
    * logger.py : 获得log对象
    * __main__.py ：使用log对象
3. 解决数据库读写问题，分为异步和同步问题
    * 同步：使用mysqlModel.py
    * 异步：使用orm模型