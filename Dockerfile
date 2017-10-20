# aliyun
FROM ubuntu:14.04

LABEL AUTHOR="teachmyself@126.com"
LABEL PROJECT="teachmyself/aliyun"

ENV TIMEZONE Asia/Shanghai
ENV DOCKER 1
ENV DEBUG 1
ENV WORKHOME /aliyun
ENV EXPOSE 8000

RUN set -xue; \
        echo "${TIMEZONE}" > /etc/timezone; \
        cp /usr/share/zoneinfo/${TIMEZONE} /etc/localtime; \
        apt-get update && apt-get install -y \
        build-essential \
        libmysqlclient-dev \
        python-dev \
        python-pip \
     && rm -rf /var/lib/apt/lists/* \
     && apt-get autoremove -y;

COPY . ${WORKHOME}

WORKDIR ${WORKHOME}

VOLUME ["/aliyun"]

USER root

EXPOSE ${EXPOSE}

HEALTHCHECK --interval=30s --timeout=5s --retries=3 --start-period=10s \
    CMD curl --silent --fail localhost:${EXPOSE}|| exit 1

ENTRYPOINT ["/usr/bin/python"]
CMD ["-m", "SimpleHTTPServer"]
