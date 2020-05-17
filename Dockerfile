FROM python:3.6
ENV PATH /usr/local/bin:$PATH
ADD . /scrapy_taipingyang
WORKDIR /scrapy_taipingyang/fbsPro
RUN pip3 install -r requirements.txt
CMD scrapy crawl tpingyang
