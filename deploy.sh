#!/usr/bin/env bash

# Must perform command as root because of directory permissions
scp -r zipped_site/* root@165.227.83.90:/var/www/html
