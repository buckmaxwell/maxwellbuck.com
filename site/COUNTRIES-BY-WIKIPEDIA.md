# I clustered countries by Wikipedia references - here's what happened

A few days ago I decided I didn't know enough about the relationships between co
untries on the World stage.  To get myself up to date I made a few different 'st
udy guides' where I grouped countries by all sorts of things -- power index, reg
ion, GDP, quality of life.  After sorting the countries this way I thought I'd b
e able to start somewhere and begin reading the Wikipedia pages for all the coun
tries, fleshing out my knowledge of the world little by little.

Sorting by these arbitrary things helped, but there was some countries that were
 hard to group and I figured that since I planned to begin my search for knowled
ge by using Wikipedia, I should ask Wikipedia what it thought.  I visited the pa
ge that lists sovereign nations and included all of them (including the heavily 
contested ones),  there were 207.  Then I  started writing a little code...

You can see the [full code on GitHub](https://github.com/buckmaxwell/wiki-countr
y-scrape), but basically, I went through the country pages one by one, and on ea
ch country page I searched for references to the other countries, building weigh
ted relationships between the countries.  I then loaded this information into a 
tool called [Gephi](https://gephi.org/) (which is open source and free!) and tri
ed my hand at creating a useful visualization.

Displaying lines proved to be futile pretty quickly. Regardless of how I organiz
ed by graph, the countries were so interconnected that it was impossible to foll
ow the lines, regardless of what wacky magic I tried to apply.  I ended up findi
ng the Gephi's force Atlas 2 algorithm to be quite useful for the visualization.
  It makes heavy use of edge degrees, grouping highly connected nodes close toge
ther.  I used it in LinLog mode, which creates tighter clusters.  You can read m
ore about the algorithm [here](https://github.com/gephi/gephi/wiki/Force-Atlas-2
).  Using Force Atlas 2, clear clusters began to emerge.  It now seemed unnecess
ary to leave all the lines in, since proximity told the same tale.  I removed th
em.

Finally, I ran the modularity class algorithm with default settings a few times 
and colored the nodes accordingly.  Interestingly, the modularity class told a s
lightly different story than simple proximity did. Take Portugal for example.  P
ortugal has a great deal in common with Spain, its nearest neighbor, and a count
ry with whom it has feuded over the border with throughout history.  Most of the
 time, geographic proximity relates to distal proximity on the graph, but in the
 case of Portugal it did not.  Portugal is floating down and significantly left 
of Spain.  You'll notice it's color, however, is shared with Spain.  Something m
ust be "pulling" it left.    A Wikipedia search for Portugal will reveal that th
e Portuguese empire colonized a lot of Africa including Guinea, Angola, and Moza
mbique.  So the color and the position of the node both tell interesting stories
.  I left them both.

The size of the nodes is based on the in-degree, or number of times other countr
ies pages mentioned the country.  Here is a picture of my results ([see GitHub f
or full PNG and PDF files](https://github.com/buckmaxwell/wiki-country-scrape)).
 If you like this let me know, I may continue posting on this topic soon.

![The Final Product](images/country-clusters-large-lables.png)

*NOTE: a previous version of this post included a different version of the same 
graph that was slightly different.  The older version is still available on GitH
ub but is less legible.*




y their references to each other on Wikipedia, the results are pretty neat. 
