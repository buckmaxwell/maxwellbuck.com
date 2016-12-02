
# Background By Reddit

Hey Guys,

I was bored between classes a few days ago and decided it would be cool to [stream pictures posted on Reddit to my desktop background](https://github.com/buckmaxwell/background-by-reddit).  Reddit has a really neat API in that every page that is publicly assessable normally, can be converted to JSON  simply by [appending .json to the end of the regular URL](https://www.reddit.com/.json?raw_json=1).

Then, to limit calls all they do is have you set your User-Agent string in the request header to something fun and playful for the requests that you make.  If your User-Agent is set to the default -- ie, you use urllib for Python or something like that, and don't set the User-Agent in the header on your own--then in a little bit you'll get a 429 status code.  So sad.  So come up with something creative and you can make 60 requests a minute.  If you need to double that, or hit some endpoints that would only be assessable to a signed in user, then use Oauth (ug, I know).

But anyway, the Reddit API kicks ass, so I hooked everything up in about 45 minutes and tossed it up on GitHub.  Hope you have fun with it! I was very satisfied with the results, and have been experimenting with different subreddits in order to increase the fun.  For an extra challenge, set it up on your friends computer, and watch with delight as they try to figure out where all these pictures of Vladimir Putin and Teacup Pigs are coming from.

https://github.com/buckmaxwell/background-by-reddit

ftimage=redditapi.png
date=20150929