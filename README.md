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
根据需要，把不需要的模块删除，如models中的orm.py