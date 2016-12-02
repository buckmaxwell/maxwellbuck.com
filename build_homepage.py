from datetime import datetime
from os import listdir
from operator import itemgetter


def get_base():
	with open("BASE.md", "r") as f:
		base = f.read()
	return base

def get_post_links():
	posts = ""
	post_list = []
	for fn in listdir("./posts"):
		if fn.endswith(".md"):
			with open("./posts/{}".format(fn), "r") as f:
			
				ftimage = "default.png"
				title = "Untitled"
				date = int(datetime.strftime(datetime.now(), '%Y%m%d'))
				url = fn.lower().replace('.md', '.html')
				for line in f:

					# get title
					if line.startswith("# ") and title=="Untitled":
						title = line.split("# ")[1].split("\n")[0]

					# get ftimage
					if line.startswith("ftimage="):
						ftimage = line.split("ftimage=")[1].strip()

					# get date
					if line.startswith("date="):
						date = int(line.split("date=")[1].strip())

				post_list.append( ('<p><img src="../images/{img}" width="100" height="100" \
				 hspace="10"><a href={url}>{title}</a></p>\n'.format(img=ftimage, title=title,
				  url=url), date) )

	post_list.sort(key=itemgetter(1), reverse=True)
	for post, _ in post_list:
		posts += post

	return posts

def get_intro():
	with open("INTRO.md", "r") as f:
		intro = f.read()
	return intro


def build_index(base, intro, posts, filename="INDEX.md"):
	with open("./site/{}".format(filename), "w+") as f:
		index = base.format(intro=intro, body=posts, year=datetime.now().year)
		f.write(index)

def remove_meta_info_lines(filename):
	metainfolines = ['ftimage', 'date']
	removed_lines = []
	with open(filename,"r") as f:
		lines = f.readlines()

	with open(filename,"w") as f:
		for line in lines:
  			if not any([line.startswith(mi) for mi in metainfolines]):
  				f.write(line)
  			else:
  				removed_lines.append(line)
  	return removed_lines

def build_posts(base):
	removed_metainfo = {}
	for fn in listdir("./posts"):
		mi = remove_meta_info_lines("./posts/{}".format(fn))
		removed_metainfo[fn] = mi
		with open("./posts/{}".format(fn), "r") as f:
			body = f.read()
		with open("./site/{}".format(fn), "w+") as f:
			f.write(base.format(intro="", body=body, year=datetime.now().year))
	return removed_metainfo

def add_meta_info_lines(removed_metainfo):
	
	filenames = [fn for fn in listdir("./posts")]

	for fn in filenames:
		with open("./posts/{}".format(fn), "a+") as f:
			for mi in removed_metainfo[fn]: 
				f.write(mi)


if __name__ in '__main__':
	base = get_base()
	intro = get_intro()
	posts = get_post_links()
	build_index(base, intro, posts)
	removed_metainfo = build_posts(base)
	add_meta_info_lines(removed_metainfo)












