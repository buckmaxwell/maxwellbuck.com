import requests
import json


image_types = ['.gif', '.png', '.jpg', '.jpeg'] 
MIN_LIKES = 25
start_link="https://graph.facebook.com/v2.8/me?fields=id%2Cname%2Cposts%7Breactions.limit(25)%2Cmessage%2Ccreated_time%7D&access_token=EAACEdEose0cBAEAgm6yubvrZAUxR4ZAwnbFs510dGIVkLcWZABSJuNDK19YZAZAmtYlOnjzyGDf4mu31ZBMheNt1honYaSXBZCk9JI6ZBkxbA9ZALW2SJkxOCOQmgzUa6toXokDPVVritcSk1RgVXhRFCrnQl8p78JZAbZC2CHYttoOZAGvr2IXbVIYjz2BHesyYlKUZD"

start_link="https://graph.facebook.com/v2.8/me?fields=posts%7Bmessage%2Cfull_picture%2Creactions.limit(25)%2Ccreated_time%7D&access_token=EAACEdEose0cBAEAgm6yubvrZAUxR4ZAwnbFs510dGIVkLcWZABSJuNDK19YZAZAmtYlOnjzyGDf4mu31ZBMheNt1honYaSXBZCk9JI6ZBkxbA9ZALW2SJkxOCOQmgzUa6toXokDPVVritcSk1RgVXhRFCrnQl8p78JZAbZC2CHYttoOZAGvr2IXbVIYjz2BHesyYlKUZD"

with open('FB-HIGHLIGHTS2.md', 'w+') as f:

	f.write('# Facebook Highlights\n')
	f.write("This page aggregates public and private posts I've made on Facebook that got over {} likes.  Some posts are old and I might not necessarly agree with them anymore. All the same, here they are.""".format(MIN_LIKES))

	pc = 0 # page count
	r = requests.get(start_link)
	robj = json.loads(r.text)

	# Deal with first link
	for post in robj['posts']['data']:
		try:
			message = post.get('message')
			time = post['created_time']
			no_likes = len(post['reactions']['data'])

			if message and no_likes >= MIN_LIKES:
				message = message.encode('utf8')
				pic = post.get('full_picture')
				f.write('## {}\n'.format(time[:10]))
				if pic:
					f.write("![]({})\n".format(pic))
				f.write("{}\n".format(message))
				f.write('\n')
		except Exception as e:
			print repr(e)
	pc += 1
	print 'finished page {}'.format(pc)
	link = robj['posts']['paging'].get('next')

	# Deal with other links
	while link or pc == 500:
		r = requests.get(link)
		robj = json.loads(r.text)
	
		for post in robj['data']:
			try:
				message = post.get('message')
				time = post['created_time']
				no_likes = len(post['reactions']['data'])
				if message and no_likes >= MIN_LIKES:
					message = message.encode('utf8')
					pic = post.get('full_picture')
					f.write('## {}\n'.format(time[:10]))
					if pic:
						f.write("![]({})\n".format(pic))
					f.write("{}\n".format(message))
					f.write('\n')
			except Exception as e:
				print repr(e)
		pc += 1
		print 'finished page {}'.format(pc)
		link = robj['paging'].get('next')


print 'Done'
