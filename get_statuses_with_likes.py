import requests
import json


image_types = ['.gif', '.png', '.jpg', '.jpeg'] 
MIN_LIKES = 25
start_link = "https://graph.facebook.com/v2.8/me?fields=id%2Cname%2Cposts%7Breactions.limit(25)%2Cmessage%2Ccreated_time%7D&access_token=EAACEdEose0cBAEdySgAuL9060JmYYmyZBlpA9YAU5bMuymYezsmF8s1WNZCmMElm28Q4WkZBzEgN3BZBwZBloxLiOfRs2ApEZCIMnzwl7j8IBXgUC5BHVmVUdYfrOhdmDEWFEXFhXM11NH3La2X8gKohqjHtEGH4saYoB5PZAyVegZDZD"

start_link =  "https://graph.facebook.com/v2.8/me?fields=posts%7Bmessage%2Cfull_picture%2Creactions.limit(25)%2Ccreated_time%7D&access_token=EAACEdEose0cBAFpWyhYIoGaQuGjmh8tYcVLOUJ9X3ZAZBYH9nlZAJKj5dN0bhqWUWG8JqnrBXGowFazgDGMEnZBObhPZALaUHHH7mlZB6sVNsJESWot70mZBpouqQEHnUzBoRVyOdHg7gx102fhUvACqR5rHVxLmnj2Ms9BWTZBFCQZDZD"

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