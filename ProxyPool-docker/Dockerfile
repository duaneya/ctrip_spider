From python:3.6
COPY requirements.txt /root/requirements.txt
WORKDIR /root
#RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories \
#    && apk update \
#    && apk --no-cache add git ca-certificates openssh \
#    && git clone git@gitee.com:duaneya/ProxyPool.git \
#    && cd ProxyPool \
#    && pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple \
#    && pip install --no-cache-dir -r requirements.txt
#WORKDIR /root/ProxyPool
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple \
    && pip install --no-cache-dir -r requirements.txt
CMD ["python", "/root/ProxyPool/run.py"]
