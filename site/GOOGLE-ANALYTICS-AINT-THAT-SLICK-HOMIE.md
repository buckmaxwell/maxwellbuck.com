
# Is Google Analytics really that slick?

If you love Google Analytics great. I've used it plenty and have only recently g
one ahead and cut it out of my site as I wander down the path of technical minim
alism.  Keep in mind I still track my users, but the things I actually cared abo
ut in GA were so simple to gather on my own that a self-built version had very l
ittle technical overhead (think 2.5 hour time investment) and allowed me to cut 
*Google's prying eyes* out of the picture while sparing my users from having to 
run JavaScript and fill their browsers with an absolutely goofy amount of cookie
s, not to mention an extra HTTP request being made for *every single page* on my
 website.

![Sorry Google, you're creeping me out...](images/Google-Big-Brother.png)

## What I liked about GA

There is a few things I like about GA.  It can tell me 

 1. Where my visitors are from
 2. How they got to my site
 3. The path they took through the site
 4. Whether they use a mobile device
 5. Whether they are a new or returning visitor
 6. How long they stayed on pages

Depending on the type of sites you run, you may care about different things than
 I do, but I believe that these metrics tend to be the most useful regardless of
 site purpose and discipline.  It should be mentioned that other metrics can be 
derivied from this information.  A cursory read of [this Google Analytics page](
https://developers.google.com/analytics/resources/concepts/gaConceptsTrackingOve
rview) will show you that Google's code is not really doing that much.  The Java
Script code that Google Analytics uses is not what gathers information about ref
errals, or IP addresses, and it's not what Google uses to determine whether the 
visitor is a new or returning visitor.  Google makes it clear that the JavaScrip
t running on the page is gathering extra information from 'the DOM [which] provi
des access to more detailed browser and system information, such as Java and Fla
sh support and screen resolution'.  While this may sound cool, as a site manager
, it's actually not that interesting to me what the screen resolution of my aver
age client is...

![Cool metrics bro.](cool-story.jpg)


## How I cut out GA and still have all the metrics I need

Those 6 core metrics are actually pretty easy to record.  IP address information
, referals, and the User-Agent are all possible to determine from the headers.  
While each of these things is trust-based, as a user could set the headers to wh
atever they feel like, most folks are using a browser and browsers tend to respe
ct convention.  This information alone, all tacked on to the header, is enough t
o provide answers for 1-4.

The 5th question can be answered with a simple long lasting session cookie. The 
6th is hard to answer conclusively no matter what.  Information about the DOM he
lps to create a better answer for this question, but clickthrough rate is possib
ly equally useful.  

So if these metrics can be obtained without running 3rd party code on a site, wh
y does everyone do it?  I believe it's the pretty graphs and charts.  Nice user 
friendly dashboards (even one's that we should admit don't tell us all that much
) are nice.  My next step will be to build a killer dashboard for my site.  When
 I do, I'll let you know.

![Such beauty, much wow](doge-wow.jpg)

## So how exactly are you tracking me?

The way I track users is effective but primitive. If you are a new user to my si
te, you'll access a page of the site and your browser will not send any cookies.
  My server will see that and so along with the webpage you requested, it will s
end back a cookie with the suggestion that your browser store it.  I do this by 
setting a Set-Cookie header on the response.  My Set-Cookie response header look
s something like this.

```http
Set-Cookie: ooh_so_tasty=PhyllisBeverlySealPage9120; Expires=Wed, 01 Jan 2116 23
:00:00 GMT;
```

If you haven't set your browser to do differently, it will remember this cookie 
is associated with my site, and pass it along with every request to my site for 
the next 100 years (when the cookie will finally expire).  I will keep a record 
of you, PhyllisBeverlySealPage9120, and with it store information about you -- y
our ip address, User-Agent, and whether or not you are on a mobile device.  I wi
ll also store each 'event' you engage in. This will include the page name, time 
fetched, and referral page.  Using this information, I can create effective visu
alizations of traffic on my network, whilst allowing my guests to remain persona
lly anonymous.  As always, feel free to look at the [code for my website](https:
//github.com/buckmaxwell/maxwellbuck.com), and please write me with your comment
s and critiques.




date=20161210
ftimage=Google-Big-Brother.png
