# Album-Art-Music-Video-Generator
Python / FFMPEG / Imagemagick script to generate album art music videos using a style which I really like.
Also note that aside from this being my first published code on github, I'm still a newbie when it comes to coding, so it still looks like spaghetti.
Originally this was based on:  **[Music-Video-Generator](https://github.com/JPBotelho/Music-Video-Generator)**
But because I changed the code too much, I decided to open a new repo.

## Features
Generates a video using a set of images which are defined by the user and also writes 'some' metadata to a text file, so you can post it on a streaming website in an easy way.
Allows the user to make a commentary which will then be sent to each text file as an "album commentary:"

## Things I need help fixing:
1. There's too much code for something that *should* be a fairly simple task.
2. Imagemagick was used because I wasn't able to get FFMPEG to work based on what I wanted to do, and even still, it was done in a sloppy way because I wasn't able to separate the command into chunks, so the easiest way was to just make a bunch of commands that did work.
3. The metadata may be missing depending on whether it exists or not (obviously), but I don't really know how to write an if statement so it writes something else based on it's presence.


# Example 
##### Here's how it will look if you've done everything right:
![9 - タイニーリトル・アジアンタム - TOHO BOSSA NOVA 2](https://user-images.githubusercontent.com/62615566/120726983-c813e500-c4af-11eb-8647-28bf46495dcf.png)
*innit cool?*

# Requirements
- FFMPEG;
- imagemagick;
- python3;
- it's also a good idea to install the requirements for python such as mutagen and glob, check the imports in renderer.py if something is amiss;

For creating the actual video, make a folder called "song" and place the following files in it:
1. A background image named "background.png"
2. An album cover art named "album.jpg"
3. A font file named "font.ttf" (I used Mplus 1p Light)
4. The actual music files in .flac format

The script will run a for loop until it finishes with the files, so the usual idea is to place an entire album on the folder and wait till it's done.
