import mutagen
import os
import os.path
import glob
import re
from mutagen.flac import FLAC

title = "None"
artist = "None"
date = "None"
album = "None"
UploaderCommentary = input("Do you have anything to say about this upload?\n")

def videoedit():
    trackstuff = ("Track: "+tracknumber+" / "+tracktotal)
    command0 = f"magick convert \"{bg}\" -resize 1920x1080 \"{bg}\"" #Resizes the background
    command2 = f"magick convert \"{bg}\" -blur 0x8 ( \"{albumart}\" -resize 725x725 -border 8 -gravity center -geometry -421 ) -composite -matte \"{generated}\"" #Makes the background
    command3 = f"magick convert \"{generated}\" -background transparent -fill black -font \"{font}\" -size 675x200 caption:\"{title}\" -gravity center -geometry +348-258 -composite -matte \"{generated}\""
    command8 = f"magick convert \"{generated}\" -background transparent -fill white -font \"{font}\" -size 675x200 caption:\"{title}\" -gravity center -geometry +346-260 -composite -matte \"{generated}\""
    command4 = f"magick convert \"{generated}\" -background transparent -fill black -font \"{font}\" -size 675x80 caption:\"{artist}\" -gravity center -geometry +348-88 -composite -matte \"{generated}\""
    command9 = f"magick convert \"{generated}\" -background transparent -fill white -font \"{font}\" -size 675x80 caption:\"{artist}\" -gravity center -geometry +346-90 -composite -matte \"{generated}\""
    command5 = f"magick convert \"{generated}\" -background transparent -fill black -font \"{font}\" -size 675x60 caption:\"{date}\" -gravity center -geometry +348+332 -composite -matte \"{generated}\""
    command10 = f"magick convert \"{generated}\" -background transparent -fill white -font \"{font}\" -size 675x60 caption:\"{date}\" -gravity center -geometry +346+330 -composite -matte \"{generated}\""
    command6 = f"magick convert \"{generated}\" -background transparent -fill black -font \"{font}\" -size 675x130 caption:\"{album}\" -gravity center -geometry +347+182 -composite -matte \"{generated}\""
    command11 = f"magick convert \"{generated}\" -background transparent -fill white -font \"{font}\" -size 675x130 caption:\"{album}\" -gravity center -geometry +345+180 -composite -matte \"{generated}\""
    command7 = f"magick convert \"{generated}\" -background transparent -fill black -font \"{font}\" -size 675x70 caption:\"{compartist}\" -gravity center -geometry +348+12 -composite -matte \"{generated}\""
    command12 = f"magick convert \"{generated}\" -background transparent -fill white -font \"{font}\" -size 675x70 caption:\"{compartist}\" -gravity center -geometry +346+10 -composite -matte \"{generated}\"" #Clusterfuck of commands, PLEASE help me fix this
    command13 = f"magick convert \"{generated}\" -background transparent -fill black -font \"{font}\" -size 675x70 caption:\"{trackstuff}\" -gravity center -geometry +348+227 -composite -matte \"{generated}\""
    command14 = f"magick convert \"{generated}\" -background transparent -fill white -font \"{font}\" -size 675x70 caption:\"{trackstuff}\" -gravity center -geometry +346+225 -composite -matte \"{generated}\""
    command15 = f"magick convert \"{generated}\" -background transparent -fill black -font \"{font}\" -size 675x90 caption:\"{artist}\" -gravity center -geometry +348-43 -composite -matte \"{generated}\""
    command16 = f"magick convert \"{generated}\" -background transparent -fill white -font \"{font}\" -size 675x90 caption:\"{artist}\" -gravity center -geometry +346-45 -composite -matte \"{generated}\""
    command = f"ffmpeg -loop 1 -framerate 1 -i \"{generated}\" -i \"{src}\" -c:v libx264 -preset veryslow -crf 0 -shortest \"{output}\"" #Makes the video
    os.system(command0)
    os.system(command2)
    print("Finished with the background")
    os.system(command3)
    os.system(command8)
    if artist == compartist:
        print("The label and artist are the same")
        os.system(command15)
        os.system(command16)
    else:
        print("The label and artist are different")
        os.system(command4)
        os.system(command9)
        os.system(command7)
        os.system(command12)
    os.system(command5)
    os.system(command10)
    os.system(command6) #WHY?
    os.system(command11)
    os.system(command13)
    os.system(command14)
    print("Finished with the metadata on the image")
    os.system(command)
    print("Finished the video")

def descriptionwriter():
    f = open(description, "w+")
    f.write("Song info: \nTitle: "+title+"\nAlbum: "+album+"\nTrack: "+tracknumber+" / "+tracktotal+"\nAlbum Artist: "+artist+"\nArtist: "+compartist+"\nDate: "+date+"\nCatalog Number: "+catalog+"\nReplay Gain: "+replaygain+"\nInsert\nYour\nDescription\nHere") #Sends the info to a text file, so I only really have to do minimal work in order to publish the description
    if not UploaderCommentary:
        print("You didn't write anything under album commentary")
        return
    else:
        print("Commentary annotated")
        f.write("\nAlbum commentary: "+UploaderCommentary)
    print("Finished writing the description")
    f.close()

def GetTags(sourcePath):    
    global title
    global artist
    global date
    global album
    global compartist
    global tracknumber
    global tracktotal
    global websites
    global replaygain
    global catalog
    fileType = os.path.splitext(sourcePath)[1]
    metadata = FLAC(sourcePath)
    title = metadata["title"][0]
    artist = metadata["albumartist"][0]
    compartist = metadata["artist"][0]
    date = metadata["date"][0]
    album = metadata["album"][0]
    replaygain = metadata["replaygain_track_gain"][0]
    catalog = metadata["catalognumber"][0]
    tracknumber = metadata["tracknumber"][0]
    tracktotal = metadata["tracktotal"][0]
    print("Finished getting tags")
        
os.chdir("./songs")
for file in glob.glob("*.flac"):
    src = file
    GetTags(src)
    mainset = tracknumber+" - "+title+" - "+album
    subset = re.sub(r"[()\"#/@;:<>{}`+=~|!?,]", "", mainset)
    output = subset+".mov"
    generated = subset+".png"
    description = subset+".txt"
    bg = "background.png"
    font = "font.ttf"
    albumart = "album.jpg"
    descriptionwriter()
    videoedit()
