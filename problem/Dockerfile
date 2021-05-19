FROM alpine

LABEL MAINTAINER="yoshino-s"
ENV REFRESHED_AT 2021-5-19
ENV LANG C.UTF-8

WORKDIR /app

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/' /etc/apk/repositories

RUN apk update && \
    apk add --no-cache libcap

COPY ./docker-entrypoint /
RUN chmod +x /docker-entrypoint

RUN adduser -D ctf

COPY ./app /app

# RUN ....

EXPOSE 80

CMD ["/docker-entrypoint"]