FROM python:3.6
ENV DEBIAN_FRONTEND noninteractive
ENV TZ Asia/Shanghai
WORKDIR /root
COPY requirements.txt /root/requirements.txt
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple \ 
    && pip install --no-cache-dir -r requirements.txt
WORKDIR /root/proxy_pool
CMD [ "python", "Run/main.py" ]
