FROM nginx

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/conf.d/

ENV MEDIA_DIR=/home/project/mysite/media
ENV STATIC_DIR=/home/project/mysite/static
RUN mkdir -p $MEDIA_DIR
RUN mkdir -p $STATIC_DIR