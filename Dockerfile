# 该镜像从官方 python:3.8 镜像继承
FROM python:3.8

# 创建 App 目录
WORKDIR /app

# 拷贝 Python 依赖配置文件
COPY src/requirements.txt ./

# 安装 Python 依赖包
RUN pip install -r requirements.txt

# 拷贝 App Python 源码到目标目录
COPY src /app

# 导出服务端口
EXPOSE 1024

# 容器启动后立刻启动 Python 服务
CMD [ "python", "main.py" ]