server {
  # Reference:
  # https://serverfault.com/questions/312111/how-do-i-get-nginx-to-forward-http-post-requests-via-rewrite
  listen       80;
  server_name  jenkins.maxwellbuck.com;

  location / {
    proxy_pass http://127.0.0.1:8080;
    proxy_redirect  off;
    #proxy_redirect  http://localhost:8080/ /;
    #proxy_read_timeout 60s;

    # May not need or want to set Host. Should default to the above
    # hostname.
    #proxy_set_header          Host            $host;
    #proxy_set_header          X-Real-IP       $remote_addr;
    #proxy_set_header          X-Forwarded-For
    #$proxy_add_x_forwarded_for;
  }
}
# vim:syn=nginx
