# When you just don't git it.

Git is probably one of the most widely used tools by developers today.  Most of
us have learned to love it, but few of us really understand it. We go about our
merry lives with no more than a cursory understanding of how version control is
really working, until we bork our repo somehow, and somehow, we find the right
Stack Overflow post, and very rarely, all is lost.

You are here for 1 of 2 reasons.

1. You borked your repo and are trying to backpeddle
2. You are the type of nerd who plans ahead.

Both reasons are valid and I'll do my best to accomodate you no matter why
you're here. With the first user-type in mind, this post will prioritize
brevity.  If you are in the latter camp, please read on, but know that for a
more fine-grained look at Git you should consult [git-scm.com](git-scm.com).

## How you should use git regularly 

Ain't that the truth.  According to git-scm.com, "an almost endless number of
workflows can be implemented with relative ease."

But that doesn't help you, and since decisions suck, here is what to do in a few
common situations. 

I'll be describing a `merge` based workflow as opposed to a `rebase` and
`cherry-pick` based flow. Some good discussion about the advantages and
disadvantages of each can be found
[here](https://stackoverflow.com/questions/1241720/git-cherry-pick-vs-merge-workflow).
My main reason for prefering the merge flow is based on ease of understanding
and use.

If you want to follow along using this as a tutorial, feel free to make a
repository and toss a README or other files in it, though you don't need to.

---

*git branch.* You don't have to do this every time, but checking where you are
once in a while is a good thing. Stick to the conventions.  Master is not to be
trifled with, do development in a different branch.

```bash
$ git branch
* master
```

*git status.* Looks like we're on master now.  Since we don't want to do dirty work directly
on master, it looks like we've got to check out a branch.  Before we do, let's
check that any local changes to master have been commited or stashed.

```bash
$ git status
On branch master
Your branch is up-to-date with 'origin/master'.

nothing to commit, working tree clean
```

Great.  That should always be the case, since no dev work should *ever* happen
on master.  But what would we do if we checked and it weren't the case?

```bash
$ git status
On branch master
Your branch is up-to-date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:  README.md 

no changes added to commit (use "git add" and/or "git commit -a")
```

Oops.  A file has been modified.  Since we are on master we know we need to
throw this work away... it was probably an accident anyway?

If it was, do this awful thing that you've copy-pasted from a Stack Overflow
article out of dispair a thousand times.  But if it wasn't an accident, wait!

```bash
$ git reset --hard
HEAD is now at 0c146e3 Initial commit
```

Congrats all your local changes that haven't been pushed are now gone. I'll
remind you that **this is throwing away all uncommited changes on your local
branch.** If this is what you want to do, it's great.

Its also possible that when running git status you see something telling you
your branch is `ahead of 'origin/master'` by x number of commits. If you did not
intend this, and you **aren't** wedded to the work you accidentally did in the
master branch, just blow it away.  Why not?

```bash
$git reset --hard origin/HEAD
```
This is destructive.  It throws away all your local changes, including those you
commited but didn't push.  Sometimes, this is what you want, but **a lot of the
time it's not.**  So what then?

### What nobody seems to know

What then? Well, you can always just not thow away your working code.

Let's imagine that I just made some changes that I really like, but that I
accidentally made them on the master branch. I haven't pushed, so I don't owe
the dev team any beer yet, but I don't want to blow away a days work with a hard
reset.  It shouldn't have been a day of work of course, but alas, we all make
mistakes, and yours, on this day, was twofold,

  1. not checking which branch you were on, and 
  2. not pushing to a remote repository frequently enough.

In this case, your second mistake turns out to be a small blessing, but don't
let that make you think you should do it again.

Let's fix your error without blowing away your local changes. First, commit the
changes on master if you haven't yet.

```bash
$ git commit -am "changes I like, wrong branch, we all make mistakes"
```

**REMEMBER,** don't push yet! If you do, you'll break master! Now, let's see
where we are, and where we wanna go.

```bash
$ git log
commit 84db201c2cacc1c8dc68286573647da6cae83a77 (HEAD -> master)
Author: Max Buck <maxwellhigginsbuck@gmail.com>
Date:   Tue Mar 6 21:04:07 2018 -0500

    changes I like, wrong branch, we all make mistakes

commit 0c146e35a1b382a4b22ae27d0666a271eedfd168 (origin/master, origin/HEAD)
Author: Max Buck <maxwellhigginsbuck@gmail.com,>
Date:   Tue Mar 6 20:17:44 2018 -0500

    Initial commit
```

We want to restore the state we had before in a new commit, without modifying
the old stuff.  To do this we will use checkout.


```bash
$ git cd <PROJECT ROOT> # this is very important
$ git checkout 0c146e35a1b382a4b22ae27d0666a271eedfd168 .
```

Don't forget the `.` at the end of the second command.  This will apply the
changes to the whole tree as long as you are in the project root. Feel free to
run `git status` again.  You should see that there were modifications to your
files. Now you can commit your changes.

```bash
$ git commit -am "restored state to the way it was before"
[master 92cda7d] restored state to the way it was before
 1 file changed, 3 deletions(-)
$
$ # Run git log to see how you did
$ git log
commit 92cda7dfc39d0f466b10a84cd57bb551bbae2543 (HEAD -> master)
Author: Max Buck <maxwellhigginsbuck@gmail.com>
Date:   Tue Mar 6 21:15:18 2018 -0500

    restored state to the way it was before

commit 84db201c2cacc1c8dc68286573647da6cae83a77
Author: Max Buck <maxwellhigginsbuck@gmail.com>
Date:   Tue Mar 6 21:04:07 2018 -0500

    changes I like, wrong branch, we all make mistakes

commit 0c146e35a1b382a4b22ae27d0666a271eedfd168 (origin/master, origin/HEAD)
Author: Max Buck <buck.169@osu.edu>
Date:   Tue Mar 6 20:17:44 2018 -0500

    Initial commit
$
```

There is now an extra commit.  The latest commit has exactly the same state as
master does on the remote repository.  Master is saved! We can now push it
without fear.

```bash
$ git push origin master
```

So what about all the stuff you worked on in the master branch that you liked?
The stuff in that middle commit? Don't worry, we haven't forgotten about that.

Find the SHA of the commit for the changes you like using git log, and do a
checkout.  You'll get a message saying you are in a detached HEAD state.

```bash
$ git checkout 84db201c2cacc1c8dc68286573647da6cae83a77
Note: checking out '84db201c2cacc1c8dc68286573647da6cae83a77'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by performing another checkout.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -b with the checkout command again. Example:

  git checkout -b <new-branch-name>

HEAD is now at 84db201... changes I like, wrong branch, we all make mistakes
```

Great, now let's check out another branch.  Naming branches is really tough
because sometimes the functionality they cover is very hard to include in a
reasonably sized name.  If you are using GitHub, I recommend naming your
branch after the issue number that it corresponds to. At this time, I've made a
GitHub issue in my repository with a description of the development work I am
doing. Suggestions on how to use GitHub issues as a successful project
management tool is a blog post for another day.

```bash
$ git checkout -b iss1
Switched to a new branch 'iss1'
```

If I were to run git log in this branch, the latest change would not be the
revision we made on master, but the last commit before that -- the SHA we
checked out into the detached HEAD state. Finish doing development work for your
feature in this branch, then commit the changes. At this point, we are ready to
merge our changes back into the master branch, but first, we should merge master
into our own branch.  That way, if there are merge conflicts, we can resolve
them on the feature branch instead of on master.  When they are resolved, we can
confidently merge our branch into master.

```bash
$ git branch
* iss1
  master
$ git fetch
$ git merge master
Auto-merging README.md
CONFLICT (content): Merge conflict in README.md
Automatic merge failed; fix conflicts and then commit the result.
```
*NOTE: git fetch followed by git merge is the same as git pull.*

We've got a merge conflict. Are you surprised?

We edited the same parts of a file in multiple places. Perhaps in our
restoration of master we deleted a line, but in our feauture branch left it. All
sorts of things could have happened. If we knew for a fact that we wanted the
feature branch versions of everything, we could tell git to prefer the current
branch in the case of conflicts. Since we can't really have perfect confidence
in most cases (who knows what your cowboy coder coworker did to master) it's
best to just deal with the merge conflicts.  It's not nearly as hard as you
might think, and chances are, there REALLY aren't that many merge conflicts.

So how do we resolve them the right way?

```bash
# git-it
A simple project to assist with learning to be effective with Git
<<<<<<< HEAD


I LOVE THIS CHANGE. I am going to keep adding to it.
=======
>>>>>>> master
```

As you might expect HEAD refers to our current branch.  The line space between
the string of less-than signs and the string of equals signs represents what our
current branch thinks that part of the file should look like.  The space between
the string of equals signs and the string of greater-than signs represents what
master thinks that part of the file should look like. You can pick one or the
other side, or write something completely new to resolve the conflict.  In this
case, we will pick the head side, and modify the file to look like this.

```bash
# git-it
A simple project to assist with learning to be effective with Git


I LOVE THIS CHANGE. I am going to keep adding to it.
```

Once you resolve the conflict, do `git add YOURFILENAME`. This will stage the
file and tells git that the conflict has been resolved.  Go through conflicting
files one-by-one with this process.  When you think you are done, run `git
status`; when all conflicts have been resolved you will see a message that says,
"All conflicts fixed but you are still merging.  (use "git commit" to conclude
merge)".  That's exactly what you should do.  This time, just do git commit and
don't supply a message. A text editor prompt will pop up with a default commit
message, I recommend keeping the default. Save the file and exit. You are done
merging.


Now that we've merged master into our branch, it is a good time to run our test
suite, and confirm things are still working properly.  If all systems are go,
it's time to merge our changes into master. Before you do, it might be a good
time to push local changes to our branch to the remote repository.

```bash
$ git checkout master
$ git pull
Already up-to-date.
$ # master is up to date. If this is not true, you may need 
$ # to tell your team to cool it with the pushes to master for
$ # a hot second. Then repeat the last thing we did -- checkout
$ # the feature branch, merge master, resolve conflicts.
$ # then checkout master again and ensure you're up-to-date.
$ git merge iss1
Updating 92cda7d..e6465ba
Fast-forward
 README.md | 3 +++
 1 file changed, 3 insertions(+)
```

Excellent. We see a fast-forward.  Since we merged master into the feature
branch first, the state tree looked like a like a line before the merge.  All
the merge does is fast forward the pointer for master, so we go from
       
```
x-x-x-x-x-x-x
    m       f
```

to

```
x-x-x-x-x-x-x
            m
            f
```

Since master and the feature branch now point to the same place in the state
tree, the feature branch is no longer important. We can push our changes on
master, then delete the feature branch.

```bash
$ git push origin master
$ git branch -d iss1
Deleted branch iss1 (was e6465ba).
```

Hooray! You're a Git hero.  And that's the pattern you should use whenever
you're using git. 

## When you're already screwed 

So your branch is already borked.  You can use git the right way tomorrow, but
for today, you just want to get unfucked. I get that.

Take a deep breath.


ahh.


Good. Now, let's get to work. Here are some general guidelines.

 1. Try not to rewrite history. Don't attempt to permanently get rid of any
    commits unless it's an obvious thing that you'd use git reset --hard for
    like in the examples in the first part.  There are much better ways of
    restoring state to a previous time, without getting rid of history or
    changing it.
 2. Find the spot where things broke, and take things back to that spot.


### I accidentally added a file (or bunch of files) to git
We've all been here. Please don't do `git rm`! To untrack a file tracked by git
do `git reset FILENAME`. Then add it to your .gitignore. Oh, and remove `git add
-A` from your workflow forever.

### I flubbed my commit message
Yea, not a big deal.  `git --amend -m "New message"`

You can also add a file to a commit with ammend.

```bash
git add forgotten_file
git commit --amend
```

### I don't know where things broke
Try using `git bisect`. Mark the bad version, and the last known working version.
Then allow git bisect to, well, bisect the versions in between until you've
tracked down the last working version.

[docs](https://git-scm.com/docs/git-bisect)

### I really do need to rewrite history
If you committed a file you shouldn't have to a public repository, you may want
to rewrite history. A common example is commiting a file with database
credentials to a public repository. 

I personally prefer the example of accidentally commiting an enormous file (like
an archive file).  Realistically having a db credential pushed to a public repo
even for a second means the credentials are compromised, and after they are, who
cares, they must be changed. Once they are changed does it really matter that
the old credentials were exposed in the git history? Commiting  an enormous file
is different. It is stuck in the history for eternity, slowing down cloning and
pushing and bloating the repository size. The file must be removed!

```bash
$ git filter-branch --force --index-filter \
  'git rm --cached --ignore-unmatch hugefile.gz' \
  --prune-empty --tag-name-filter cat -- --all
```

This will remove the file from every branch and tag.  It will also remove any
commits that would be empty as a result of the above operation.  **THIS WILL
REWRITE HISTORY** which can be very annoying.  Only do this if absolutely
necessary.


### I merged the wrong branch
No worries. do a git reset --hard to the commit before the merge. You won't lose
anything so long as you keep the branch you merged lying around so it's not
really destructive.


### I rebased the wrong branch

To undo a rebase, check the [reflog](https://git-scm.com/docs/git-reflog). Find
the  find the head commit of the branch as it was immediately before the rebase
started in the reflog. Then do a git reset --hard. Again, as long as the branch
you accidentally rebased from still exists, you aren't being overly destructive
by doing this.

```bash
$ git reset --hard HEAD@{5} # 5 signifies 5 operations before HEAD
```

### I don't know what I did
When you don't know what you did, sometimes it's best to go back to a place
where you knew what was going on. Use `git log` to see your commit history, and
pick a commit SHA. Just like we did in the first section, go to the top level
directory of the repository and check out the SHA

```bash
$ git checkout SHA-OF-UNDERSTANDING .
$ git commit -am "revert to when I understood"
```

**As before, don't forget the . in the first command.** The cool thing about
this, is now you still have all your other commits.  Sure they broke things, but
why throw the baby out with the bath water?

If you want to go back to a commit, just check it out, then create a branch to
work on it. When you get things working again, merge it back into the original
branch.


maxout.

date=20180306
ftimage=git.png
