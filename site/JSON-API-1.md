# Using the Json Api Specification, Part 1


If you have experience with more than one API,  you probably have used some APIs
 that you love and some that you hate.  Reasons to love an API include good docu
mentation, detailed responses, and good error messages.  A good API is often so 
well organized that a front end developer looking at one or two endpoints could 
give a near perfect guess at what the others do, just by their names and HTTP me
thods.

Problem is, we backend developers like to get creative! With lightweight framewo
rks like [Flask](http://flask.poco.org) and [Sinatra](http://sinatrarb.com) whip
ping up an endpoint is a cake walk.  Couple that with a solid ORM like [SQLAlche
my](http://sqlalchemy.org) and suddenly, you have an API that gets the job done.
..so long as the nutty database guy is in direct communication with the client s
ide devs.

Sure, you could write 3 pages of documentation detailing all your custom decisio
ns for every one of the 30 endpoints in your system, many do.  Thing is, "good d
ocumentation", in front-end speak means, "prewritten code for each endpoint in R
uby, Python, PHP, Node , Java, and Objective-C."  I imagine some of you are agre
eing and getting very excited about this idea.  Sad truth is though, most backen
d teams don't have the financial or human capital to just give you what you want
.  Companies like Facebook, Twitter, and Tumblr will, but they aren't the only n
eat APIs out there, at least they are not the only APIs with information worthy 
of using.


![Tumblr Dev Console](images/tumblr-dev-console.png)


Because of how delightful and easy these APIs are to use, its easy to get discou
raged when building an API.  There is a lot to live up to. You can write documen
tation till you keel over but the chances of the masses reading what you wrote a
re slim!

The key here, and what those big shots don't seem to understand, is standardizat
ion.  I can communicate with you here without giving you a "key", because I assu
me that you'll recognize I'm using the English language protocol.  I might add a
 flourish here and there, but if I stick to what I know you know, we can communi
cate fast and effectively.  An important thing to note here is you can conform t
o these standards, but you don't have to, I could begin communicating in [Yoda s
peak](http://yodaspeak.co.uk) if I so chose: The computer enforces well known st
andards for RESTful APIs not.  Yes, hmmm.

But I will not be communicating in Yoda speak, and you should not be writing you
r APIs in your own goofball idea of a way, even if it get's the job done.  I hav
e been known to throw small animals softly into the air, gently catch them, and 
set them down angrily when I notice well respected companies implementing "Yoda 
speak" APIs.  Who is on the naughty list?  Well, Twitter only uses POST and GET 
methods even when a delete is more sensible.  Twitter also generally misuses RES
T, including verbs in resource names.  Walmart (used to I happily learned) retur
n a 200 status code even when a request had failed or was malformed. And despite
 my beef with Twitter, for the most part those guys conform better than anyone. 
 Some APIs are so bizarre it would be impossible to determine the reason for HTT
P verbs or status codes at all.  The cool thing is though, just as most of us do
n't speak English perfectly, even a partial implementation of the standard goes 
a long way.  Most APIs do their best to follow these forms, even if they fall sh
ort some times.

This article is about the [JSON API specification](http://jsonapi.org) which can
 be found on http://jsonapi.org.  The goal of the spec was to do what REST and a
nd HTTP did for standardization, and extend that to the JSON responses themselve
s.  Instead of reinventing the wheel every time we must craft a JSON response fr
om a set of relational tables, why not just do it in the same predictable way ev
ery time?  Makes sense, and other specifications have existed before this for cr
eating JSON responses.  But JSON API is special, because it works really well an
d has already been adapted for plug and play use by some big shots.  One of thos
e is Ember, the extremely popular and quickly growing javascript framework, and 
there are others too.

Before I committed to using JSON API in my latest project I read through a pleth
ora of information.  I was worried that since the project utilized [neo4j](http:
//neo4j.com) (a graph database) that maybe responses couldn't be as standardized
 in the same way.  I was worried that the responses might include too much or no
t enough information.  I was annoyed that the creative touch of crafting a perso
nal response for each endpoint would be lost.  All wrong.  I ended up having a b
last making my first fully compliant "JSON API" API and I would recommend you tr
y it out too.

Why did I have so much fun?  I embraced the standard.  As I mentioned, my first 
project to fully comply with the JSON API spec was an API built around a graphin
g database.  To create my models I used an OGM (object graph mapper -- like an O
RM for a graphing database) called [NeoModel](http://github.com/robinedwards/neo
model).  NeoModel is relatively new and I emailed the developers before taking i
t for a spin.  After a test run, I was impressed.  The way NeoModel works is muc
h like SQLAlchemy: the models all inherit from a shared base class that has a fe
w built in functions.  In NeoModel this base class is called StructuredNode in r
eference to the nodes of the graphing database.  A tall can of red bull followed
 by a 45 minute nap spawned a dream that ended up changing the course of the pro
ject forever.  I extended the base class creating "SerializableStructuredNode" a
nd added a few methods to the new Base class that created standard JSON response
s based on the JSON API spec.  After the grueling process of writing this new po
werful base class, the rest of that API was done in no time.  All that it requir
ed was the endpoints themselves -- a significantly easier task than writing cyph
er (think SQL for neo4j) for 24 endpoints.

Even better?  The clients that will use that API don't need documentation.  Usin
g the correct HTTP verb, and the correct resource name, they can find any type o
f node in my database, it's attributes, and it's relationships to other attribut
es.  They can even request that those related resources be individually included
 in the response because they would rather not send a separate query for them la
ter.  If they have any questions I'll send them right to jsonapi.org. It's kick 
ass.

So you are wondering about my magic class.  Yea, it's dope.  I haven't yet publi
shed it on [GitHub](http://github.com/buckmaxwell) or the pip repository because
 I want to allow a bit more time to work out the kinks, at some point I will tho
ugh, and I plan to keep you updated on the progress of that here.  Secondly, I'd
 like to write a similar base class for SQLAlchemy.  I am getting started on tha
t soon, but have a lot of work and school on my plate at the moment also.  Eithe
r way, if you are interested in testing, using, or contributing to either of tho
se projects, please let me know.  I am very excited about this well thought out 
and widely applicable standard. Ω

