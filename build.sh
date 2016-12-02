

# Build homepage
python build_homepage.py

# Turn markdown files to HTML
for md_filename in site/*.md
do
  html_filename=(${md_filename//.md/.html})
  html_filename=`echo "print '$html_filename'.lower()" | python`
  echo "entering grippp!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
  grip $md_filename --user-content --export --user=buckmaxwell --pass=$1 $html_filename
  echo "grip complete!!!!!!!!!!!!!!!!!!!!!!!"
  
done

# Remove created markdown files
rm site/*.md

# Build resume
grip "RESUME.md" --user-content --export --user=buckmaxwell --pass=$1 "site/resume.html"

