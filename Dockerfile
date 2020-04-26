# 基础镜像
FROM docker.io/python:latest
MAINTAINER author "maozexijr@gmail.com"

# 拷贝程序
COPY hello.py /opt/hello/
COPY config.ini /opt/hello/
COPY requirements.txt /opt/hello/

# 依赖包
RUN pip install --no-cache-dir -r /opt/hello/requirements.txt

# 执行指令
CMD ["python3", "/opt/hello/hello.py"]