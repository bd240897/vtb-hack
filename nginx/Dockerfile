FROM nginx

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/conf.d/

ENV MEDIA_DIR=/home/project/lms/media
ENV STATIC_DIR=/home/project/lms/static
RUN mkdir -p $MEDIA_DIR
RUN mkdir -p $STATIC_DIR