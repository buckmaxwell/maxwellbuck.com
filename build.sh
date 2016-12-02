

# Build homepage
python build_homepage.py

# Turn markdown files to HTML
for md_filename in site/*.md
do
  html_filename=(${md_filename//.md/.html})
  html_filename=`echo "print '$html_filename'.lower()" | python`
  grip $md_filename --user-content --export $html_filename
  
done

# Remove created markdown files
rm site/*.md

