from typing import final
import urllib.request
import os, glob
import eyed3
from eyed3.id3.frames import ImageFrame
from pydub import AudioSegment
import pydub

# from pydub.playback import play
# from playsound import playsound
opener = urllib.request.build_opener()
DIRECTORY = "/Volumes/GoogleDrive/My Drive/Life/UT Austin/Mahabharata/Python Projects/Gita Sanskrit Download Python Project/"
opener.addheaders = [
    (
        "User-Agent",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36",
    )
]
CHAPTERLENGTHS = [
    (1, 39),
    (2, 71),
    (3, 43),
    (4, 42),
    (5, 27),
    (6, 42),
    (7, 30),
    (8, 28),
    (9, 34),
    (10, 40),
    (11, 52),
    (12, 16),
    (13, 29),
    (14, 24),
    (15, 19),
    (16, 19),
    (17, 24),
    (18, 74),
]
TOTALCHAPTERS = 0
ALLFILES = "/Volumes/GoogleDrive/My Drive/Life/UT Austin/Mahabharata/Python Projects/Gita Sanskrit Download Python Project/All Chapters"
for i in CHAPTERLENGTHS:
    TOTALCHAPTERS += i[1]
baseURL = "https://www.bhagavad-gita.org/AudioArchive/Gita/Sanskrit/verses/"
# test1url = 'https://www.bhagavad-gita.org/AudioArchive/Gita/Sanskrit/verses/06-01.mp3'
urllib.request.install_opener(opener)
while True:
    makeFolders = input(
        "\nWould you like to create the 18 folders that represent the books of the Gita? (Y/n): "
    )
    if makeFolders == "Y":
        for i in range(1, 19):
            os.mkdir(f"Chapter {i}")
        break
    elif makeFolders == "n":
        break
    else:
        print("\nYou have entered a value that is not supported. Please try again.")
# def firstTestDownload():
#     urllib.request.urlretrieve(test1url, f'{DIRECTORY}Gita6.1Test.mp3')
while True:
    makeAllFolder = input(
        "\nWould you like to create the folders that contain every verse of the Gita? (Y/n): "
    )
    if makeAllFolder == "Y":
        for i in CHAPTERLENGTHS:
            for j in range(1, i[1] + 1):
                urllib.request.urlretrieve(
                    f"{baseURL}{str(i[0]).zfill(2)}-{str(j).zfill(2)}.mp3",
                    f"{DIRECTORY}All Chapters/Gita{str(i[0]).zfill(2)}_{str(j).zfill(2)}.mp3",
                )
        break
    elif makeAllFolder == "n":
        break
    else:
        print("\nYou have entered a value that is not supported. Please try again.")
# for i in (CHAPTERLENGTHS):
#     for j in range(1, i[1] + 1):
#         urllib.request.urlretrieve(f'{baseURL}{str(i[0]).zfill(2)}-{str(j).zfill(2)}.mp3', f'{DIRECTORY}All Chapters/Gita{str(i[0]).zfill(2)}_{str(j).zfill(2)}.mp3')
listAllChapters = glob.glob(f"{ALLFILES}/*.mp3")
listAllChapters = list(set(listAllChapters))
listAllChapters.sort()
for i in listAllChapters:
    audiofile = eyed3.load(i)
    if audiofile.tag == None:
        audiofile.initTag()
    audiofile.tag.images.set(
        ImageFrame.FRONT_COVER, open("cover.jpg", "rb").read(), "image/jpeg"
    )
    audiofile.tag.save()
while True:
    makeFullFile = input(
        "\nWould you like to create the full audio of the Gita? (Y/n): "
    )
    if makeFullFile == "Y":
        AudioList = []
        for i in listAllChapters:
            x = AudioSegment.from_file(i, format="mp3")
            AudioList.append(x)
        finalAudio = AudioSegment.silent(duration=0)
        for i in AudioList:
            finalAudio += i
        finalAudio.export("fullGita.mp3", format="mp3")
        break
    elif makeFullFile == "n":
        break
    else:
        print("\nYou have entered a value that is not supported. Please try again.")
# AudioList = []
# for i in listAllChapters:
#     x = AudioSegment.from_file(i, format = 'mp3')
#     AudioList.append(x)
# finalAudio = AudioSegment.silent(duration = 0)
# for i in AudioList:
#     finalAudio += i
# finalAudio.export("testFullGita.mp3", format="mp3")
