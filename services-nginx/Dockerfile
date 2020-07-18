FROM nginx:1.19.0-alpine

COPY ./services-nginx/erp.conf /etc/nginx/conf.d/default.conf

RUN mkdir /static

COPY ./services-web/erp/static /static
COPY ./services-web/erp/media /media

CMD /usr/sbin/nginx -g "daemon off;"
