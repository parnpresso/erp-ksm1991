FROM nginx:1.19.0-alpine

COPY ./service-nginx/erp.conf /etc/nginx/conf.d/default.conf

RUN mkdir /static

COPY ./service-web/erp/static /static
COPY ./service-web/erp/media /media

CMD /usr/sbin/nginx -g "daemon off;"
