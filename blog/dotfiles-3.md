title: Dotfiles, Part 3
date: 2022-10-03

Hello again! In this post (the third part of this series), I will be talking
about my desktop environment. I will also discuss how I use my machine (i.e.
how I go from boot to a working environment), as I feel like that's important
for myself to know. Let's get into it!

## Desktop Environment?

I don't actually use a standard DE (e.g. GNOME, KDE, XFCE, etc.). Instead, I
use the following:

- A display server (Xorg)
- A window manager (BSPWM)
- A hotkey manager (SXHKD)
- A compositor (Picom)

These provide slightly less than everything a standard DE provides - notably,
they lack the visual consistency in windows that most DEs provide. For me, this
doesn't really matter because I don't use very many GUI applications, and the
ones I do use tend to be very minimal in nature anyway.

I like this setup for several reasons, the main one being that it adheres to
the Unix philosophy of "do one thing and do it well". Furthermore, I'm not
bound by the designs or requirements of someone else, I'm free to break things
as I see fit. Is it better? I like it, so yes. Is it more productive? Hard to
tell. I guess it depends on how well I can use Vim, which is not very. :D

## Xorg

Xorg is started with `xinit`/`startx`. My `~/.xinitrc` is very simple, and only
contains:

```
exec bspwm
```

This starts up BSPWM. Besides this, I haven't really configured Xorg at all. To
be honest, I don't really think there is much besides this that I'd even want
to configure in Xorg.

At some point, I'd like to move to Wayland (seeing as it's the shiny new
thing). As of right now, both BSPWM and SXHKD haven't been ported to Wayland
(yet!), so I think I'll hold off it for now.

## BSPWM

BSPWM is a window manager that uses a binary tree approach to spawning new
windows. In practice, I've never actually found this particular approach very
useful (read - I've never had enough windows to make use of this). Nonetheless,
I find this WM to be very useful for many reasons, the main one being that
BSPWM uses a client-server approach to setting different options, and as a
result the startup file (`~/.config/bspwm/bspwmrc` is actually an executable
Bash script, and the hotkeys that relate to BSPWM are just commands being sent
to the "server".

I find this architecture really cool and useful. It's such a clean way to do
things! It also means that I can start different programs in my `bspwmrc`, and
do other neat things like checking if a monitor is connected before attempting
to display stuff on that monitor.

Currently, my BSPWM is setup to:

- Set the window gap to 0 pixels and set the border to 2 pixels - to maximise
  screen real estate.
- Configure certain windows to be floating (mainly `feh`, `mpv`, and
  Pavucontrol).
- Add/remove desktops from an external monitor depending on whether it is
  actually connected.
- Start some extra programs (SXHKD, Picom, etc.).

I used to use i3, and i3 was nice as a first WM but there were several quirks
that meant I eventually jumped ship. To be honest I don't actually remember
what the issues were, but I'm fairly confident that I'll be using BSPWM for a
very long time.

## SXHKD

SXHKD is a hotkey manager that was written by the same person who wrote BSPWM.
As a result, they fit together very nicely, but if you wanted you could also
use SXHKD in basically any Xorg environment. It's pretty cool!

I'm not going to go through every hotkey that I have here, but instead I'll try
to focus on the broader "classes" of hotkeys I use:

- BSPWM focused hotkeys: things like moving between desktops and windows,
  moving actual windows, sending windows to different workspaces, etc.
- Utilities: starting a terminal emulator (in my case, Alacritty), starting a
  dialog box that lists some desktop applications I use, etc.
- Displaying information: showing the current network, date/time, volume, etc.
- Other things like changing the screen brightness or audio levels.

## Picom

Picom is a compositor. It was forked from Compton, which in turn was forked
from something else, which I think might have been forked from something else?
I'm not really sure. Anyway, I switched to Picom after Compton sort of...died?
Again, I'm not familiar with the history of Picom/compositor managers in
general.

Currently, my Picom is setup to only show fading effects when spawning new
windows. That's it. I used to have it also show shadows, and I had a really
cool setup where the shadows were really well defined and boxy, but I've
removed that becuase the shadows don't actually show up with my current BSPWM
setup. I might add a thing where the currently focused window is brighter than
the other windows (or just make the other windows darker) but for now, it's
fine as it is.

## From Boot to Working Environment

As a quick aside, I wanted to talk about how I go from a laptop that is off to
a environment that I can do some work in. The steps are generally as follows:

- Turn on my laptop with the "power on" button.
- After a few seconds, I am presented with a TTY that prompts me to login.
- After entering my login details, Bash (usinR `~/.bash_profile`) automatically
  starts Xorg, which in turn starts BSPWM. I am now ready to work!

I know people use display and login managers to manage this process from a GUI
(or at least, a more GUI-ish environment), but I like this. A lot. It's so
clean and simple, and it's very comfy to work with.

## Conclusion

That concludes this post! The next post will focus on the actual desktop
applications I use (finally!), and the one after that will focus on the scripts
I use in my day to day life. I hope to see you then!
