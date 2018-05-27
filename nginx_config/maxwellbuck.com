server {

  server_name maxwellbuck.com; # managed by Certbot

	root /var/www/html;

	# Don't gzip assets on the fly, instead, use precompressed assets
	gzip_static always;

	# Add index.php to the list if you are using PHP
	index index.html;

	# permanent redirect to countries cluster image (bots seem to be looking for it)
	rewrite ^/wp-content/uploads/2016/11/country-clusters.png$ /images/country-clusters-large-lables.png permanent;
	rewrite ^/index.php/2015/09/10/utilizing-the-json-api-specification-part-1/?$ /json-api-1.html permanent;
	rewrite ^/index.php/2016/09/20/how-many-seasons-are-there-really/?$ /how-many-seasons.html permanent;
	rewrite ^/index.php/2015/09/29/background-by-reddit/?$ /background-by-reddit.html permanent;

	location / {
		# First attempt to serve request as file, then
		# as directory, then fall back to displaying a 404.
		# try_files $uri $uri/ =404;
	}
	error_page  404              /404.html;
	error_page  401              /401.html;

	location ~*  \.(jpg|jpeg|png|gif|ico|css|js)$ {
    expires 365d;
	}
	
	location ~* \.(html|md)$ {
		expires 5m;
	}
  
  location ^~ /staging/ {
    auth_basic "Restricted Content";
    auth_basic_user_file /etc/nginx/.htpasswd;
    error_page  404              /staging/404.html;
    error_page  401              /staging/401.html;
    #allow 127.0.0.1;
    #deny all;
  }
  location = /staging/404.html {}
  location = /staging/401.html {}
  location ^~ /staging/static/ {}
  

error_page  404              /404.html;

listen [::]:443 ssl ipv6only=on; # managed by Certbot
listen 443 ssl; # managed by Certbot
ssl_certificate /etc/letsencrypt/live/maxwellbuck.com/fullchain.pem; # managed by Certbot
ssl_certificate_key /etc/letsencrypt/live/maxwellbuck.com/privkey.pem; # managed by Certbot
include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

}
server {
  if ($host = maxwellbuck.com) {
    return 301 https://$host$request_uri;
  } # managed by Certbot

	listen 80 ;
	listen [::]:80;
  server_name maxwellbuck.com;
  return 404; # managed by Certbot
}
# vim:syn=nginx
