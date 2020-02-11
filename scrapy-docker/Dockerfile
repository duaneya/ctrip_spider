From scrapinghub/scrapinghub-stack-scrapy:1.5-py3
WORKDIR /root/ctrip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple \
    && pip install --no-cache-dir scrapy-splash scrapy-fake-useragent \
    && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
CMD ["python", "/root/ctrip/crontab.py"]
