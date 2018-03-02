FROM kyma/docker-nginx
COPY nginx.conf /etc/nginx/sites-enabled/default
COPY site/ /var/www
CMD 'nginx'
