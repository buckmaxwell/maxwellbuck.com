#!/usr/bin/env bash

# set env vars
export GRIPURL='//./'

# Build homepage
python build_homepage.py

# Turn markdown files to HTML
for md_filename in site/*.md
do
  # Make HTML files
  html_filename=(${md_filename//.md/.html})
  html_filename=`echo "print '$html_filename'.lower()" | python`
  grip $md_filename --export --no-inline --user=buckmaxwell --pass=$(cat .githubpass) $html_filename
done


# Prettyfy markdown files for raw versions
cp posts/* site
for md_filename in site/*.md
do 
  discard_fn='.tmp-x-xffff.md'
  perl -pe 's/(.{'80'})/$1\n/sg' $md_filename > $discard_fn
  mv $discard_fn $md_filename
done

# Remove created markdown files -- DON'T do this. They are used in the Mobile View.
#rm site/*.md

# Build resume
# Build 404
grip "404.md" --export --no-inline --user=buckmaxwell --pass=$1 "site/404.html"

# Build Facebook Highlights
grip "FB-HIGHLIGHTS.md" --export --no-inline --user=buckmaxwell --pass=$1 "site/fb-highlights.html"


# Resize images and add to thumbnail directory -- faster page load on index 
# THIS SCRIPT REQUIRES IMAGEMAGICK
# $ brew install imagemagick or apt-get install imagemagick
FOLDER="site/images"
WIDTH=100
HEIGHT=100
#resize to either height or width, keeps proportions using imagemagick
for file in $FOLDER/*
do
  # Try to resize each file in images folder, if one fails, don't tell us, it's
  # probably just not an image file.
	convert -quiet $file -resize $WIDTHx$HEIGHT\> site/thumbs/${file##*/} 2> /dev/null
done


# Gzip all html, md, and css files. Don't touch image files which can grow when
# compressed.
# Compress html and markdown files
for file in site/*
do
  # file could be a directory, if so ignore error
  gzip < $file > zipped_site/${file##*/}.gz 2> /dev/null 
done

# Compress css files
for file in site/asset/*
do
  # file could be a directory, if so ignore error
  gzip < $file > zipped_site/asset/${file##*/}.gz 2> /dev/null 
done

# Move images to zipped site
cp -a site/static zipped_site
cp -a site/images zipped_site
cp -a site/thumbs zipped_site
cp -a site/asset zipped_site
# DONE with site compression



