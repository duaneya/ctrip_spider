 docker run -p 8050:8050 scrapinghub/splash --disable-private-mode
  time scrapy crawl ctripspy -o c.csv -t csv
docker run --name my-custom-nginx-container -v /home/d/PycharmProjects/ctrip/nginx.conf:/etc/nginx/nginx.conf:ro -d nginx