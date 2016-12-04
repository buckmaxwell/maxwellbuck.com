

# What's with the new blog?

![Well, wp kinda sucks...](images/fuck-wordpress.jpg)

So I have a new blog! Thanks for noticing.  This has been a long time coming. Sometime last year (or maybe even the year before) I wanted to kick my site up a notch.  A friend of mine was reading a book called *The Four Hour Work Week* and was talking to me about outsourcing.  Delegation of menial tasks to others could save me massive quantities of time.  I was enticed.  This blog is not the blog I outsourced, but rather the replacement for that blog.

## The old blog

I went to upwork.com, posted a 'personal assistant' job posting, and was off to the races.  I did 4 interviews and ended up hiring one fellow.  At the same  time, I tried a second type of outsourcing -- one involving a virtual assistant service website.  The VA companies usually employ a number of people with different skill sets.  You can pay the VA companies for a set number of hours, and they will only charge you for the hour when they work on it.  To test the waters, I paid for 15 hours (about 100 bucks) and requested they rebuild my website.  The work they did was decent.  Overall, I was pleased with the result but wasn't happy about the number of hours I had to spend describing what I wanted.  I would have liked to have given a loose description and then have been impressed by some creativity.  The cool thing was, they finished my website over the course of 2 weeks and charged me for less than 11 hours. For 60 or 70 bucks, I had gotten a killer deal.

That website was a WordPress site and was a bit cookie cutter.  It looked pretty, but I had some issues with it.

 1. **It didn't put content first.**  The site was this massive landing page with the blog at the bottom like it was an afterthought.  This massive 'About Me' section towered overhead.  If you actually did manage to find a blog post, the text was not very fun to read.  The font was unusual and the text was justified.

 2. **Code looked goofy.**  The site did not allow for proper syntax  highlighting without jumping through crazy hoops.

 3. **It was slow to edit.**  Writing posts, tagging, setting images, and all the while having to do it online through a strange interface that didn't allow for easy local testing was painful.   

 4. **It was slow in general.** My site relied almost entirely on static content, yet often took 5 seconds to load.

So new year, new blog!  I figured I could make some of these changes to my blog since it is my finals week and I should be doing other things.

## Pretty bones

I wanted this site to be a site I could update from the command line at my leisure, I wanted it to be fast, and I did not want bloat.  I wanted to see the bones and I wanted them to be pretty.

My thought was that I could write my posts in markdown, and then 'build' html from the markdown with a converter.  I'd use GitHub flavored markdown to do it. I wanted my posts to be viewable and downloadable in markdown also, so I'd have a link to the 'raw' versions of the posts.

## Getting it done

The task wasn't too hard, though there were some intracacies.  I used a tool called [grip](https://github.com/joeyespo/grip) to generate the HTML files. Since I needed to add some standard information to every page before generating the HTML, I wrote a script to do that also -- modifying the markdown before generating HTML. I also wrote code to generate a home page.  To aid in generating the homepage, I created a few metainfo tags that I could add to posts -- date and ftimage.  By specifying in the markdown the date and featured image I could put the blog posts in a smart order on the homepage, and display an image next to them.

The most complex part was the mobile view.  While it would have been possible to modify the CSS to be dynamic, it seemed a bit difficult as the CSS file (which came from GitHub via grip) was 9000+ lines long, and I was no front-end wiz kid.  I instead opted to use [Flask](http://flask.pocoo.org/) to check the User-Agent string and in the mobile case, swap the css.

All the code is on GitHub as usual.  Feel free to [check it out](https://github.com/buckmaxwell/maxwellbuck.com).

## Hosting

For ease of use and price I moved the site to Heroku.  The site is currently on a free dyno, but I hope I get enough readers that paying for they hobby dyno makes sense someday ;).  I set up automatic deploys from the GitHub master branch.  Now all I have to do is write a post, build the site with my build script, add the new files to the git repository, and push.  It's awesome.



date=20161204
ftimage=fuck-wordpress.jpg