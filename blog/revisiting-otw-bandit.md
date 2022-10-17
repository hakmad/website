title: Revisiting OverTheWire Bandit
date: 2022-10-17

My about page says my interests include game development and cybersecurity.
Despite that, all of my posts so far have been about my dotfiles, and really
they've not even been that good. (I haven't forgotten about the last post about
my scripts that I still need to write - I've been busy (read: lazy) so I
haven't been writing as much recently). Until today! Sort of.

A few years ago, when I first wanted to get into cybersecurity related stuff, I
read a few guides and most of them suggested doing CTF challenges. At the time
I was very green (I still am) and so I was looking around for beginner friendly
things when I stumbled across [OverTheWire](https://overthewire.org). If you
don't know, they host several wargames, which are essentially a series of CTF
challenges where the flag for one challenge gives you access to the next. These
are a really fun and hands-on way to learn, as you don't just do rote
memorisation - you actually *apply* what you learnt. I enjoyed completing
Bandit which is mostly focused on basics on Linux and some Git stuff. Recently,
I've been trying to get back into this sort of thing so I figured I'd give it
another shot. This post details my thoughts about Bandit having done it twice.

Note: this post doesn't contain solutions. I'm pretty sure the flags change
anyway, so there's no point in taking them from me. I also won't provide guides
to how to complete challenges because:

1. I'm dumb.
2. Find them yourself.
3. If you can't find them yourself, look at someone else's guide.

Who am I kidding, who even reads this site haha.

## The Good

If I had to describe my Bandit experience in one word, it'd be "weird". Or at
least "different". In a good way.

The very second level has a file that begins with a dash. You can't just `cat`
it normally, you have to do some extra stuff to get the content out of the
file. The twelfth level has a file that has been archived and compressed to the
point where I'm pretty sure it's larger than the original size of the file. The
25th and 33rd levels are my favourite, they were really weird - no spoilers,
try them out and you'll see what I mean. :D

My point is, it takes what you already know and subverts your expectations. It
doesn't play by the rules, because it's trying to teach *you* to not play by
the rules, to tinker and experiment, to break things. That sort of hacker
spirit it's trying to imprint on you is something I think is quite important,
beyond just the regular learning. Having the knowledge is one thing, but it's
quite another to have the mindset and creativity to know where the
vulnerabilities are and how to exploit them.

## The Bad

Honestly? Not much! For a "Linux Basics" style wargame, I thought it was pretty
solid. I think more could've been covered though, like creating files (though
I'm not sure how you'd be able to trigger a flag from creating a file) and
directories, symlinks, file permissions, redirection and pipes (this is a big
one) and other related stuff. I'm not an expert though, so take that with a
grain of salt.

I would've appreciated better explanations for some of the challenges. I think
the worst was probably 20, I didn't realise that *I'm* supposed to listen and
connect at the same time, so I was trying to use `nmap` to find the port I
needed to listen to. That might just be me though, so I'll leave it at that.

## The Ugly

Again, not much to say here. In fact the only thing I didn't like was the fact
it uses a non-standard SSH port (2220 instead of 22), though I guess it makes
sense if they're running multiple wargames on the same machine. Me from a few
years ago found it incredibly frustrating to type out the port number as well
as the full URL, but me from today just added it to my SSH configuration. I
will say it made me *very* frustrated when I got to the Git part, because I
forgot what port I was supposed to be `clone`ing from.

## Conclusion

Overall, if you're looking for a introduction to cybersecurity/hacking and
aren't sure where to begin, try this. I'm not saying it's the best but it'll
definitely scratch the itch that you're looking for and make you come back
wanting for more. Which OverTheWire has. :)

I'm going to be doing Natas and Krypton at some point, so when I do I'll post
my thoughts on those. I actually started both of these after I did Bandit the
first time around but...I never finished it. Hopefully I'll finish it this
time!
