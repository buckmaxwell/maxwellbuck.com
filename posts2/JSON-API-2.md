

# Using the Json Api Specification, Part 2: NeoAPI

Hey Guys!  If you read the [first part of this post](json-api-1.html), which is certainly not necessary for you to do now if you haven't, then you remember how I praised the [JSON API specification](http://jsonapi.org) and told you it was totally the cheese and that standards are great, and yada yada yada.  Well all that is very true, but I have followed through and put together a python package that I think will prove I walk the walk AND talk the talk.

The package is called [NeoAPI](http://github.com/buckmaxwell/neoapi) and is built on the [NeoModel](http://github.com/robinedwards/neomodel) package by Robin Edwards.  The way NeoModel works is much like SQLAlchemy -- it creates an abstraction layer between the database and the API.  Essentially, classes represent tables, and instances of those classes represent rows within the table.  Since Neo4j is a graphing database it's a bit different but the concept is the same.

What I did was to take those NeoModel classes, which have the title StructuredNode, and write an extension class for it.  That extension class adds methods like create_resource, update_resource, set_resource_inactive, and get_resource_or_collection.  These methods correspond directly to the standard create, update, delete, and get sequence.  There are also methods to manipulate relationships between objects, and also to fetch related resources.  The added methods mean that by installing NeoAPI and creating a few models, all you have to do is set up endpoints that call the correct method on the model, and BOOM! You have a working API.

NeoAPI is the coolest thing I've ever built.  If you want to use it and have any questions, please do not hesitate to email me at maxbuckdeveloper@gmail.com.  There is a [sample project](https://github.com/buckmaxwell/sample-neo-api) on GitHub that you should also use for reference, as well as consulting the [NeoModel docs](http://neomodel.readthedocs.org/en/latest/), and the [JSON API spec](http://jsonapi.org).

Have fun!

NeoAPI: https://github.com/buckmaxwell/neoapi

Sample Project: https://github.com/buckmaxwell/sample-neo-api


ftimage=graphdb.png
date=20150915
