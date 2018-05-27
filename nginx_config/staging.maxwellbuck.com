server {
  listen       80;
  server_name staging.maxwellbuck.com;
  location / {
    allow 127.0.0.1;
    deny all;
  }
  return 301  http://maxwellbuck.com/staging;
 
}
# vim:syn=nginx
