
# I have been using tensorflow to detect subject verb agreement errors 


At the start of this year I began working at a non-profit education technology
company based in New York City called Quill.org. Their mission is to help
students become better writers.  The tool is free to use for teachers, but has a
paid tier that provides an extra layer of assessment for teachers, principles,
or administrators. Quill strives to give students as much freedom as possible
with their answers, while still giving good feedback – 'multiple choice sucks'
has become a sort of unofficial motto.

To be true to this unofficial motto, we have a talented in-house content team
that grades student responses to our questions before we have a suitable number
of answers, then our algorithms can generalize about which answers are correct
and incorrect based on whether answers are similar to a graded answer. It's a
system that has worked pretty well so far, but it has limitations that are
pretty easy to imagine. A standout issue is the intense amount of human grading
required for great algorithmic feedback to start kicking in, a measure that
increases exponentially for every extra word of freedom a student is given in
their response. Another is the methodology for deciding which sentences resemble
each other well enough to warrant identical feedback – 'I am good' and 'I is
good' share a verb with the same simple and complex part of speech, but one is
incorrect and the other, perfectly okay.

In order to strengthen our feedback, I've been working for the past 2 months on
using a deep neural network to classify sentences based on different types of
problems.  Early on, I built a participle phrase detection model, that could
recognize participle phrases without main clauses and point this out to the
author. 'Worrying needlessly about the state of the world while
pacing on the precipice' would warrant such feedback. Emboldened by this
success, I built a few other models until I arrived at the problem of Subject -
Verb agreement. I began by constructing a rule based system, but it fell flat
quickly, only capable of detecting main-verb errors.  I was blown away by the
how the seemingly simple problem, see if a subject and verb agree in number,
could have so many surprises. The conditional mood, the strange 'going to'
tense, the oddities presented with idioms, the grave difficulties posed by
parsing out subjects ('What I like about books is characters', Swimming is fun',
'To be the greatest swimmer in the world is the only true pleasure', are all
examples of sentences with subjects that are not simple noun or pronoun
constructions).  If there was ever a problem with enough idiosyncracy to require
ML I figured this must be it.

I built an early model, and my test suite ripped it to shreds.  You can read
about it [here](why-our-sva-model-sucks.html). I took what I learned and built
another that accounted for sentence mood and the strangeness of irregular verbs.
I iterated again.  With ML, each failed iteration is painful because reducing
sentences, training, vectorizing, and then training a model on less than baller
hardware is quite time consuming. With automation, concurrenct programming, and
better hardware I've been able to decrease model generation times considerably,
but early on, it could take a week or more.  I began naming my models after NBA
players (mostly Cavs and former Cavs). Irving was less than ideal, James, my first
minor success.  Thompson, my current model, is promising, but has some major
weaknesses (the freethow line??). The issues facing each new model are different
than the ones from the last – often an error caused by an overreduction can
become a sparse data error when fixed.

My next model (Green?) will attempt to solve 3 problems,

1. ***Reductions with missing subjects.*** Often our current reducer misses a
   subject that is non-obvious (read, not a noun or pronoun phrase). I think
   using AllenNLPs constituency parser could help alleviate this issue.
2. ***Errors caused by total sentence evaluation.*** By evaluating an entire
   sentence at once, common clauses are likely to be marked erroneous because of
   their prevalence in incorrect sentences (even though they prevail in correct
   sentences too). In the Thompson model, sentences that result in the single
   reduction 'they are' are marked wrong with 77% confidence! I believe the
   prevalence of the phrase in correct and incorrect sentences caused this,
   paired with an unfortunate selection of mangled sentences which is done
   probabailistically. Because about 16% of our incorrect sentences are actually
   correct (we generate them and don't do a perfect job), the '50/50' spot for
   confidence is above 50 percent, so 77% may not be an outrageous statistical
   fluke.
3. ***Sparse data errors.*** The biggest problem of all with our current model
   is sparse data, plain and simple. Increasing our training data should take
   care of some of the errors that are clearly related to having no labeled data
   that matches. The hard part here is the extra time it takes to do so.
   Automating the reduce-vectorize-train pipeline, beefing up hardware, and
   relying on GPU processing for training tensorflow models will help us get
   where we need to be.

I am eager to share how it goes.
Updates soon.


Max

date=20180528
ftimage=sva2.jpg
descrip=I have been spending the past few months using tensorflow to train natural language models. Here are some things I've learned.
