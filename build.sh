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
  echo "entering grippp!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
  grip $md_filename --export --no-inline --user=buckmaxwell --pass=$1 $html_filename
  echo "grip complete!!!!!!!!!!!!!!!!!!!!!!!"
done

# Copy HTML files from site to mobile_site
cp site/*.html mobile_site

# Prettyfy markdown files for raw versions
cp posts/* site
for md_filename in site/*.md
do 
  discard_fn='.tmp-x-xffff.md'
  perl -pe 's/(.{'80'})/$1\n/sg' $md_filename > $discard_fn
  mv $discard_fn $md_filename
done

# Copy markdown files from site to mobile site
cp site/*.md mobile_site

# Remove created markdown files -- DON'T do this. They are used in the Mobile View.
#rm site/*.md

# Build resume
grip "RESUME.md" --export --no-inline --user=buckmaxwell --pass=$1 "site/resume.html"
cp site/resume.html mobile_site/resume.html

# Build 404
grip "404.md" --export --no-inline --user=buckmaxwell --pass=$1 "site/404.html"
cp site/404.html mobile_site/404.html

# Build Facebook Highlights
grip "FB-HIGHLIGHTS.md" --export --no-inline --user=buckmaxwell --pass=$1 "site/fb-highlights.html"
cp site/fb-highlights.html mobile_site/fb_highlights.html

# Copy images to mobile_site directory
cp -a site/images mobile_site/


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

# Copy thumbnails to mobile site
cp -a site/thumbs mobile_site/




