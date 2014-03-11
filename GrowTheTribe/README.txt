Basics:

1. login system via twitter, Facebook, and google auth
2. Profiles e.g. simply to add other authentications than the one they
logged in with for now, but for other reasons such as bios or past events
attended, etc., later on. If we could make the users' name a link to their
profile, then I would love to allow them to publish their
Twitter/Facebook/LinkedIn handles/URLs so folks can get in touch.
3. The ability for admins or some other privileged role to go in an add
conferences.
4. The ability for a user to select from these added conferences, and fill
out a form about them, that might include the following
	A. Title of their talk
	B. Description of their talk
	C. Date/time of their talk
	D. Relevant links/resources (this is separate than description so
they can drop links here in a bulleted list to PDF, PPT, and other files, ya
know?) NO UPLOADING, just links.
5. A main page that can display the coverage e.g. 100+ accessibility
presentations in California in March. CSUN is there/then, so that would be a
high number.

Medium:

1. Users to be able to add conferences, and admins can review/approve.
2. Users to be able to vote on conferences e.g. I'm not presenting at the
Seattle Python unconference, but I really wish someone would do
accessibility there, and five of my friends agree (I'd like to then allow
the system to suggest the conference to someone who lives in Seattle, but
that's in advanced).
3. Because I know reverse lookups are easy in django, could we have the
conferences be links that display talks folks have said they've done at them
e.g. if I click PyCon 2013, I get all the accessibility talks, but if I look
at Ian's profile, I'll get all of his across all conferences, etc.

Advanced:

1. Showing charts of coverage over time (not even worth doing until data
exists)
2. Integrating location aware information e.g. if it knows I'm in RTP, and
there's a conference in Charlotte with a lot of votes, it could ask me if
I'm willing to go give the talk.

Again, trying to be respectful of what's easy and what's hard e.g. things
that might take an entire hour to implement should be moved off, whereas the
5 to 10 minute hacks, we should promote so we can just get something to play
with.
