title: Dotfiles, Part 2
date: 2022-10-01

Welcome back to the second post in this series about my personal dotfiles! This
post will be focused on my every day programs, which are:

- Bash
- SSH
- Git
- Vim

I won't focus on the desktop applications I use just yet, nor will I talk about
my desktop environment (it's not really a DE but I call it that). Those are
topics for another time.

## Bash

I use Bash as my shell. The reason for this is because Bash is *everywhere*. My
phone, the servers my university uses to get us to do coursework, the server
I'm using to serve this website (along with some other stuff), the list goes
on. I could use another shell (in particular, Zsh seems very interesting) I'm
content with Bash and don't have any serious reason to migrate. To be honest, I
haven't tried out Zsh other than using it in the live installation environment
- it was pretty cool and the tab completion was very nice, so maybe I'll give
it a shot at some point.

The other reason I'm sticking with Bash is because I also script in Bash quite
a lot. I know that the interpreter can be set with the shebang line at the
beginning of a script, so if I wanted to I could switch to another shell and
keep all my Bash scripts, but I like consistency, and it just feels cleaner to
me to have the shell I use on a daily basis be the same shell I use when
writing scripts to perform certain tasks.

Bash is configured through 2 main files: 

- `~/.bash_profile`, which is run when the user logs in (in my case, from TTY)
- `~/.bashrc`, which is run when the user starts a new shell (e.g. a new
  terminal emulator)

My `~/.bash_profile` contains things that are set once and not changed after
the user logs in. These include:

- Environment variables, like the `$EDITOR` I use by default, and the `$PATH`
  to look for programs:
	- In particular, I've set my `$PATH` to search the current working
	  directory. This might be a bit of a security risk but it's more
	  ergonomical to type `a.out` instead of `./a.out` in my opinion.
- Shell options (set with `shopt`)
- Starting X on login with `startx` - see
  [this article](https://wiki.archlinux.org/title/Silent_boot#startx) for
  details

My `~/.bashrc` contains things that might change from time to time, or are just
generally more dynamic. These include:

- Sourcing some completion scripts (so I get better autocompletion)
- Aliases - things like `alias cp="cp -r"` which makes life so much easier
- Prompts
	- I've set `$PS1` to add a `R` before the actual prompt so I know if
	  I'm on a remote machine or not, which helps if the remote machine
	  also has my dotfiles setup on it

Finally, I also have an empty file `~/.hushlogin` which disables the login
banner.

Overall, I'm pretty happy with my current setup. I could add other things to
Bash (functions seem pretty interesting) or switch entirely to a different
shell but for now, this setup is:

1. Minimal
2. Stable

Which is exactly what I want from something that provides such a core aspect of
my system.

## SSH

I haven't really configured much of my SSH setup, mostly just generating SSH
keys with `ssh-keygen` and adding these to this server. I have, however,
configured this server to be called just `server` on my personal computer, so
all I have to do is `ssh server` and I'm presented with a remote connection to
my server. It makes my life easier as I don't have to type out my username,
hostname, the port the server listens to SSH on, and my password. It also helps
with things like `scp`, especially the port option (`scp` uses `-P` as it's
port option, which I always mess up as I think it's the same as `ssh` which
uses `-p`). I'm fairly content with my SSH setup as it stands.

## Git

Like SSH, I haven't really configured much of my own Git. Just my username and
an email that GitHub provides so I don't get spam. Unlike SSH though, I think
there are some useful options I could add to Git - in particular, aliases. I
actually used to use aliases at one point, I would do `git l` and it would show
the log. I got rid of them because they interfered with some of the other
things I would do but I might add them back at some point (for example, to
alias a particularly long command). We'll see. I might also change my email to
something else, but I need to actually set up email on this server before I can
do that.

## Vim

Vim is my default text editor. I've been using for almost everything for just
over a year now, and to be honest I've barely scratched the surface of what's
possible. There are still so many things I could configure, packages I could
add, *things to learn!* It's kind of exciting, but also a little overwhelming.

My current Vim configuration sets up basic things like auto-indentation, line
numbers, syntax highlighting, etc. and also adds a custom colour scheme. I'm
still configuring it, there are a bunch of small things that still bother me
(titles in Markdown are coloured with this weird flesh pink colour, I should
probably change that), but other than that, I'd also like a more IDE-like setup
from Vim.

Things like better code completion would be awesome, especially for things like
Java or LaTeX which have lots of boilerplate code (being able to type something
like `\begin{environment}` and having the corresponding `\end{environment}`
show up would be really helpful). Other things like
[limelight](https://github.com/junegunn/limelight.vim) for more focused
writing, customising the status bar, adding a window on the side, setting
maximum line widths depending on file type...there's just so much to do and
customise that it is a bit scary and paralysing. I love it though. I'm hoping
by the end of this year I can get a bit more seriously into Vim and *finally*
set it up the way I like it, but don't count on it. :)

## Conclusion

That concludes this post. Next post, I'll be focus on the actual desktop
environment and desktop applications, and then finally the scripts. I hope you
see you then!
