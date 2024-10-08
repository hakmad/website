---
title: Hello, World!
date: 2024-09-04
---

Hello world! This is my first post on this website.

I've made and remade this site several times over a few years but I'm hoping
that this time I actually *do* something with the website - for context, I've
spent a very long time messing around with making a script to generate posts
like this from Markdown files, but have not dedicated nearly enough time to
actually writing any posts. There's an XKCD comic somewhere which
graphs/compares the number of posts on a website against the framework/website
setup, showing that people who write barebones HTML with little/no CSS tend to
produce the most valuable and productive content (the best example I can think
of is Donald Knuth's website), people who use frameworks like Gatsby and Hugo
are somewhere in the middle mostly producing good content, while people like me
who decide to implement their own static site generator spend more time writing
the *generator* instead of actually using it. In addition to this, I've not
even dedicated enough time to writing code, meaning in six years I have nothing
to show: little to no coding experience and even less practise writing long
form text.

Hopefully that changes today.

This post is going to be about this website and some of the choices I made
around it (in particular and ironically, the script I use to generate this
website). It's not meant to be informative or useful to anyone but me - it's
either the first or the last nail in the coffin of my lack of productivity,
marking the end of one era and inshallah the start of a new one. I hope.

## DNS and Hosting

At their core, websites need 2 things: somewhere to put it (a hosting
solution) and something to find it (a domain). Technically you don't even
need a domain - if the hosting solution is connected to the internet you can
find it using the IP address, but that is not particularly useful and it's
easier to think of/type in `hakmad.com` instead of `12.34.56.78` or some other
IP address. I'm going to talk about both hosting and DNS in the same section
because in the past I've always considered them simultaneously. (That doesn't
mean you *should* do that - they are completely different things after all - I
just happen to do things that way.)

This section is going to talk about these a little bit (along with some other
things related to it) documenting my journey from GitHub to Cloudflare. I hope
it's a little insightful.

### In The Beginning (GitHub Pages)

In the beginning, when I first wanted a website, I used GitHub pages. GitHub
pages is nice, but I had 2 main gripes:

1. The domain would be `hakmad.github.io` which I didn't really like (I wanted
   something simpler).
2. URLs can be inconsistent: I didn't much fancy any of the big frameworks (to
   be honest I had no idea how to even get them up and running) so I wrote an
   earlier iteration of this script to generate HTML from Markdown files. To
   prevent GitHub from using Jekyll to try to generate website you had to
   create a `.nojekyll` file at the root of your repository and then create
   bare HTML files. This in itself is fine, but then the URLs can
   be... annoying. For example, when you first navigate to the website, you
   navigate to the root (`/`), but navigating to a particular page and then
   navigating back would result in going to `/index.html`. Not every page
   showed this - if you navigated to `/index` GitHub would happily serve you
   `index.html` with no issues. This `.html` extension that would appear
   inconsistent was very grating for me and I wanted something that was
   consistent one way or the other - either no extensions at all or extensions
   all the time.

This second point was particularly annoying to me but was also something that I
let get in the way of my productivity for a long time. As a result, I hardly
ever wrote anything and spent more time looking at alternatives or "perfecting"
my script to generate the site. I also didn't particularly like the domain, and
was very puritan about the fact that it should look neat and tidy:
`hakmad.github.io` doesn't say neat or tidy to me, it says uncool and ugly. I
think what I really wanted was to have my own domain, something that was mine
and mine alone. I may stand on the shoulders of giants but I'm *me*, not one of
hundreds of warts on the giants back.

### Grand Plans (Ionos)

Eventually, I got a job so I could afford to spend money on things like domains
and other things. I had enough money that I decided to ditch the idea of using
GitHub pages completely and for a while I wanted to self host, but a physical
server seemed wasteful environmentally and moneywise so instead I searched on
the internet and came across Ionos, which provides VPSs and domains as well as
a host of other internet things. After looking at the reviews, I decided to
give it a go. Nothing ventured, nothing gained.

A Virtual Private Server (VPS) is a server running in a (kind of) isolated
environment on top of a (typically shared) physical server. The shared
resources can be concerning if you host sensitive data or you're running an
application which demands as much as possible from the platform but for my
usecase it was ideal - I ran an SSH server to connect to/control the server and
a HTTP server to serve content. I had grand plans for it and even executed on
some of these: I wanted to host my email, private files, calendar, contacts and
much more on this server (maybe even running a Minecraft server) but only
managed to figure out how to run FTP, CalDAV and CardDAV in addition to the
above. Email is really freaking hard to get right and frankly it's worth paying
someone else to do it for you. We depend on email so much for so many things,
and I've heard plenty of horror stories about people losing access to a key
communication system over night because they forgot to pay, or the hosting
provider went down, in addition to the nightmare that is email delivery.

(Looking back, another good thing was not putting all my eggs in one basket. I
paid IONOS for both the VPS and the domain. If IONOS were to fail, I'd lose
access to everything which would be incredibly worrying.)

I enjoyed learning about hardening an SSH server, I got spooked by random spray
attacks attempting logins and learnt about tools like `fail2ban`, `ufw` and
`iptables`/`nftables` to prevent things like that. I had fun trying out
different softwares for hosting CalDAV/CardDAV (and ended up losing most of my
contacts at least twice because I decided to put all my contacts onto an E2EE
platform and then promptly lost the password), and had a similar experience
messing around with FTP software (Seafile is pretty neat!). But I digress.

Besides SSH (it's so undescribably *cool* being able to run commands on a
server half the world away), the most fun thing was actually setting up and
running a HTTP server. That moment, where you type in some obscure commands
from a docs page that hasn't been updated in years and then hop on your
browser, navigate to your domain, and seeing *something* - a fancy HTML site
all styled with CSS and a sprinkle of JS, a plaintext document, a file, even
the placeholder page that Apache serves when you first start the web server -
that moment is **magical**. You're no longer just someone who browses the
internet. You're a part of it. You contribute to the wonderful place we call
the internet.

Anyway. I messed around with 3 different HTTP servers, namely Apache, `nginx`
and Caddy. Apache and `nginx` were kind of overkill for what I wanted (static
site hosting) but it was a fun learning experience figuring out how to get them
up and running (and also how to get them to play nice with other services I
wanted to run). Caddy was the coolest though: the configuration was easy,
effortless and readable, the documentation was thorough and covered many use
cases (including rewriting URLs to remove extensions or redirecting `www` to
point to just the website) while also being simple, it felt light and powerful,
and best of all, there was HTTPS out of the box. No extra configuration needed.
(I should note that this is a static website, there's no dynamic content being
served here so yes, HTTPS doesn't *really* matter, but still. It's nice to have.)
Sometimes I think I miss hosting on a server, but really I just miss Caddy.

The main reason I moved away from using a VPS was actually a simple one: cost.
I was paying about £6 per month (which is cheap) but when compared to other
offerings such as GitHub pages which does the same for free - I just didn't
feel like I was getting my money's worth. I had also given up on the pipe dream
of hosting my own email and had been burned too many times by losing
contacts/calendar information (my own fault), and other projects like hosting a
Minecraft server or running a more fleshed out website seemed out of reach. (I
never tried. I should have.) The experience was valuable, but in my mind it was
a waste of money to continue paying for a service when free/more reliable/both
alternatives are available, so eventually I moved off my VPS and started
hunting again for an appropriate solution.

### Back To ~~Reality~~ The Cloud (Netlify and Cloudflare)

I didn't want to go back to GitHub pages because I knew that I'd get annoyed by
the issues I'd faced previously and try something else. I also didn't want to
go back to VPS's because I felt like I'd get overconfident, tempt fate, lose,
and then fall from the sky like many an Icarus before me. So I started looking
for alternatives and found 2: Netlify and Cloudflare. To be honest because all
I do is serve plain HTML, I can't really tell you the difference between the
two other than Cloudflare is more reliable (it's Cloudflare, they're massive),
has better documentation and has a larger community. The main reason I chose
Cloudflare was actually because around the same time I also decided to move my
domain away from Ionos. I chose Namecheap to begin with because they seemed
cheap, but then moved to Cloudflare because they hiked the prices a little more
than I expected them to and it just seemed like a better idea to have all of my
eggs in one basket - running the website *and* the DNS one service makes sense
to me.

(I know what you're going to say: "but hakmad, isn't putting all your eggs in
one basket exactly what you recommended *against* not a few paragraphs
earlier?". Yes, but this and that are different. If Cloudflare Pages fail, it
doesn't matter if the DNS works, no one will see my website. If Cloudflare DNS
fails, it doesn't matter if Pages works because no one will see the website
*and* the internet will be on fire.  Plus, I'm just running a simple website in
one basket, not trying to store most of my digital life in a service that will
potentially fall apart. It boils down to this: realistically, I can afford to
have my website disappear for a while because at the end of the day it's nice
to have, and if it breaks it breaks. I can't afford to lose my emails, personal
contacts, and whatever else I potentially would have had stored online. That's
it.)

So. Here I am, having tried lots of different things and eventually settling
for Cloudflare. In the future I might get an itch to try (semi or fully) self
host again. If I had my own place, it would be pretty cool to run my website
off a Raspberry Pi or some small home server which is attached to the internet
24/7, but alas, I am poor and do not have my own place so that is a dream I
will save for the future.

## Website Design Choices

This section lists out some of the different choices I've made (stylistic or
otherwise) when making this website. I'm going to say less on this because here
I'm just listing out my opinions, and frankly there isn't more to say other
than a few words justifying or explaining a certain choice. I'll try to be a
somewhat comprehensive but I'll probably leave some stuff out.

| Choice | Reasoning |
| --- | --- |
| Little/No JS | I don't need it (yet). In the future I could do stuff with KaTeX or Pygments, but I don't need that right now |
| Few colours | It's less distracting and it looks aesthetic. To me anyway. |
| Default fonts | The website loads quickly and the default fonts are good enough for everyday use. |
| No analytics/comment section/interactivity | I don't see a need for this personally. Some people might find it hugely important. If I want to see how someone interacts with the content I make, I can share this to other websites (e.g. Reddit or HN) and see how people react there. |
| Dark mode | I like dark mode. :D |

Some these design choices might be rethought in the future, depending on the
sort of content I write (I'm fairly confident that I'd add something like
Pygments or some other code highlighting tool) but I think that most of these
are good because they help keep things simple. And if things are simple, I can
focus on other things. Like actually doing. Like actually *writing*.

That was the plan anyway. I hope to write a lot more in the coming months and
years inshallah. I've started a new job but I want to learn, grow and develop
and hopefully use this as a platform to document that and share it. I hope it's
worth your time reading this. Thank you for doing so. :)
