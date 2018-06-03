

# Let's Continuously Integrate

This is a static site served with nginx. If you haven't noticed, it's quite
fast.  The pages are delivered compressed, the images delivered in smaller
versions when sensible, and no content is created dynamically. I write the site
in markdown, and then use joeyespo's `grip`
[link](https://github.com/joeyespo/grip) to convert the markdown to something
friendlier – github README looking pages.

It works for me because I like to be able to include code in my blog posts and I
know how GitHub makes things look (and like it!).

I like to use this blog to try out new technologies, and this week I switched
from using deploy scripts to publish this blog, to using Jenkins, a certified CI
server (woot woot). Right now it's a pretty simple setup, with a pipeline that
treats the `master`, `develop`, and any other branch on Github a little
differently.  When I push to develop, Jenkins grabs the Jenkinsfile from my
repository and begins running the pipeline. It builds my site from the markdown
files, using my old script, compresses things, and moves my current nginx config
into place.  Then it copies the zipped site to the staging site if I am on the
`develop` branch, or the production site if I am on `master`.  Pushes to other
branches result in a build, but don't deploy to staging or prod.  My staging
site runs on the main site and is protected with basic auth. My whole site is on
GitHub, including the Jenkinsfile and nginx config - please have a look [at
it](https://github.com/buckmaxwell/maxwellbuck.com) if you like.

Even without a full suite of tests I have already appreciated the peace of mind
that comes with seeing a site in staging before the production push. Missing
image files on new blog posts (gotta do that `git add`) get me everytime, and
seeing their lack of presence on the page in staging is so much less stressful
than noticing it in production and hoping nobody important is on the site.

I love that Jenkins has streamlined what was becoming a rather convoluted
process.  It's a powerful tool and I plan to do a lot more with it very soon.
First up on that list – parallelization and not rebuiling unmodified pages.


date=20180528
ftimage=jenkins.png
descrip=Using Jenkins multi-branch piplelines to increase confidence in my deploys.
