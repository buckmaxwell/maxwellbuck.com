
from datetime import datetime
from os import listdir
from operator import itemgetter
import os


def get_ordered_posts():
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

				rd = str(date)
				readabledate = rd[4:6] +'.' + rd[6:8] + '.' + rd[0:4] 
				post_list.append( (fn, date) )

	post_list.sort(key=itemgetter(1), reverse=True)
	post_list = [x[0] for x in post_list]
	return post_list


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

				rd = str(date)
				readabledate = rd[4:6] +'.' + rd[6:8] + '.' + rd[0:4] 
				post_list.append( ('<p title="post-date" \
                                align=right>{date}</p><h2><img \
                                title="thumbnail-img" align="middle" src="images/{img}" width="100" height="100" \
                                        hspace="10" ><a href={url}>{title}</a></h2>\n'.format(img=ftimage, title=title,
				  url=url, date=readabledate), date) )

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
		index = base.format(intro=intro, body=posts, year=datetime.now().year, raw=filename)
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

def build_non_post_page(filename, base):
    with open("./{}".format(filename), "w+") as f:
        body=f.read()
        f.write(base.format(intro="", body=body, year=datetime.now().year,
            raw=filename))
    print filename
    return None



def build_posts(base):
	#filenames = [fn for fn in listdir("./posts")]
	filenames = get_ordered_posts()
	filenames.reverse()
	removed_metainfo = {}
	for i, fn in enumerate(filenames):
		mi = remove_meta_info_lines("./posts/{}".format(fn))
		removed_metainfo[fn] = mi
		with open("./posts/{}".format(fn), "r") as f:
			body = f.read()

			next_link = "Next"
			prev_link = "Prev"
			if i+1 < len(filenames):
				print filenames[i+1]
				next_link = filenames[i+1].lower().split('.')[0] + '.html'
				next_link = "<a href={}>Next</a>".format(next_link)

			if i:
				prev_link = filenames[i-1].lower().split('.')[0] + '.html'
				prev_link = "<a href={}>Prev</a>\n".format(prev_link)

			if next_link and prev_link:
				links = "<p align=center>"+ prev_link + " <> " + next_link +"</p>"
			else:
				links = "<p align=center>"+ prev_link + next_link +"</p>"
			body += links

		with open("./site/{}".format(fn), "w+") as f:
			f.write(base.format(intro="", body=body, year=datetime.now().year, raw=fn))
	return removed_metainfo

def add_meta_info_lines(removed_metainfo):
	
	#filenames = [fn for fn in listdir("./posts")]
	filenames = get_ordered_posts()

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
        #build_non_post_page('RESUME.md', base)
        #build_non_post_page('404.md', base)
	add_meta_info_lines(removed_metainfo)


