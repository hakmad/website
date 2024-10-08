---
title: Grace Hopper Is Really Smart
date: 2024-10-01
---

I'll try to keep this post short - it's more of a rant than anything else.

I work at a pretty big company. I'm still employed there so I'm going to avoid
saying too much so I don't get fired but... God. I've been here nearly a month
and I've already become very annoyed at some of the ways that we do things.

Rear Admiral Grace Hopper gave a lecture on information management at the NSA
in 1982 (they recently released it to the public and you can find it on YouTube
[here](https://www.youtube.com/watch?v=si9iqF5uTFk)). First of all: she's
really smart. Like, wow, she had amazing insight and deserves to be up there
with Ada Lovelace and the unsung women of Bletchley Park you never hear about.
She's seriously amazing.

A key point brought up in her lecture was this: we don't design around
information flows and we really should. We design for immediate needs, without
considering our future needs or how our system will grow and develop. This
really struck a chord with me, because so many of the systems, tools,
workflows, processes that we use were designed and developed almost as a
plaster to solve a problem *but never actually address the underlying problem.*
And it's so frustrating. Our tools are crippling, outdated, dysfunctional and
have limited capacity to expand or grow. They can't answer our questions. The
data they store, the information they contain, is wrong because the methods to
interact with/create/modify the data, our basic CRUD functions, are nearly
useless and do nothing to validate input or format output appropriately. It's
genuinely frustrating.

But it doesn't stop at our tools. Oh no. (Some of) our processes, at their
core, are fundamentally broken and are either:

- Non-existent
- Incomplete

I'll give examples of both.

We had an audit a few weeks ago. The person who took the lead of the audit,
rather than following some kind of standard plan/process (which is what I would
have expected), instead hounded other team members for notes about "what we
gave the auditors last year". Why? Because the person who ran the audit last
year left, and apparently all their notes and evidences left with them. Why?
Because we didn't have a documented process on how to carry out this audit and
what the results of that audit actually was. It felt like we were kids trying
to cram exam content, guessing what will come up on the paper rather than
learning the underlying concepts behind what was being assessed and answering
questions based on that. We floundered through that audit and (in my opinion)
we shouldn't have gotten away with a lot of the things we did but... I'm not
the auditor. The thing that frustrates me the most is this: *we didn't have a
process in place that was repeatable and recorded.*

We have a process for approving certain technologies for use in our
environment. Part of the process involves using a risk scoring process which
categorises the technology into low/medium/high/critical. Our process states
the following:

- If the technology is high/critical, reject.
- If the technology is low, accept.

The first question I asked on seeing this was: "what about medium?". To which I
was told "we don't know". "We don't know"? Are you kidding me?! You *know* that
the risk scoring method produces one of those 4 categories, why do you not know
what to do for that category? Why is that not part of the process? "Because we
haven't come across that usecase yet?" So!?! It *will* come up, why not build
out the process to account for that? *We didn't plan for a certain outcome to
happen, and when it (inevitably) did, we were unprepared.*

In her lecture, Grace said the most common excuse for not designing systems to
handle information with a good amount of foresight was: "we've always done
things that way". I can think of a few more:

- "We don't have the resources (time/effort) to understand the data/information"
- "We don't have the resources (time/effort) to build/procure a better tool"
- "We didn't anticipate that usecase"
- "There is no process"
- "All corporates are like this" (I hate this one the most)
- **"No one talks to anyone"**

That last one is a real killer. You **NEED** to communicate (important) things.
Effectively. Tools and systems are all about communication. An Excel
spreadsheet, a PowerPoint presentation, a fancy dashboard with all the bells
and whistles under the sun - none of these will save you if you fail to
properly communicate what you actually need to. These tools serve one purpose
and one purpose only: document previous decisions to enable you to make future
decisions. They cannot do that for you. All they do is provide you with the
data that you need to make a decision. *That* is what information is. Managed
effectively, it can be a game changer for an organisation. Managed
ineffectively (or not managed at all) and all you have is pixels on a screen
and ink on a piece of paper. Nearly useless.

Grace Hopper realised this in *nineteen eighty two*. Granted, she's very smart
and the NSA didn't release this lecture until a few weeks ago. But we've also
had *forty two years* to figure this out. Why are we only realising this *now?*

So here's my promise: from now on, I will look at the data and think to myself
"What do I actually want to do to transform this from useless stuff to useful
information? How can I manage that information so it works for me? How will it
interact with all the other bits of data that I already have?". I implore
you to at least *try* the same. All corporates are steaming hot messes, yes.
But hopefully they can be cleaned up just a little.
