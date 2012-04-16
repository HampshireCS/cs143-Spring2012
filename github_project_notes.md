Create Project
=============================

First you need *one* team member to create a new github repository.

1. Go to github.com
2. Click "New Repository"
3. Fill out the form
4. Follow the instructions for the first commit
    * copy ".gitignore" from other project

After you have pushed the first commit up, refresh the page to see your repo

Add Team Members
================================
1. Go to the repos Admin
2. Go to Collaborators
3. Add your teammate(s)

Your teammates can now clone the repo


First Modification
=================================
create basic app class
git push
git pull


Why not work in master?
=================================
You may have noticed on github "branch: master"
This is the "root" branch

Even if you are the only person working on a project, you don't necessarily want to work on master all the time.

* you can't easily work on multiple areas at once
   * developing two new features and not worry about breaking the "core"
   * neither has to work at any given moment
* you can switch from doing development to fixing a bug

It's a good idea to think of master as the "working" version of your code

As you add new features, your code will break, so you create "branch"

What is a branch
=================================
Branching is saying "I want a copy of my code at this point and to go in a different direction"

Think of it like a branching tree

Create a Branch
=================================
The easiest way to create a branch is to checkout one
    checkout is like saying "this is what I'm working on"

git checkout -b name


>> both create branch

>> switch to bugfix main
>> jack merges in fixed main with own stashed code

Merging
======================================
This is the opposite of branching
it brings everything together
you can merge any branches
    (pulls are actually fetch and then merge)

>> merge player branch back in

you can delete branches you are done with, but we won't here...


Collaborating
===========================================
Jack wants me too check out his enemy code
>> pushes branch to github
>> I fetch

looks good
>> I merge


Dealing with Conflicts
=========================================
Sometimes, you cannot help but work on the same file and merge's won't be the cleanest


Tagging
===========================================
The way turnin always worked was tagging a commit with the right hw number
have to do it manually now

git tag
