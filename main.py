#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import time
import random

CurrentDirectory = os.path.dirname(os.path.realpath(__file__))


def GetLocalTime():
    CurrentTime = time.localtime().tm_hour
    return CurrentTime


def GetTimeInDay():
    CurremtTime = GetLocalTime()

    if CurremtTime >= 5 and CurremtTime <= 7:
        Status = 'SunRise'
    elif CurremtTime > 7 and CurremtTime <= 11:
        Status = 'Morning'
    elif CurremtTime > 11 and CurremtTime <= 16:
        Status = 'AfterNoon'
    elif CurremtTime > 16 and CurremtTime <= 19:
        Status = 'SunSet'
    elif CurremtTime > 19 and CurremtTime < 5:
        Status = 'Night'

    return Status


def ChangeBackGround(CurrentTimeOfDay, ImageName):
    ImagePath = CurrentDirectory + '/WallPapers/' + CurrentTimeOfDay \
        + '/' + ImageName

    os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri '"
               + 'file://' + ImagePath + "'")


# Our Main
while True:

    ImagesNames = []
    StatusOfDay = GetTimeInDay()

    for (path, dirs, files) in os.walk(CurrentDirectory + '/WallPapers/'
             + StatusOfDay):
        for File in files:
            ImagesNames.append(File)

    # Choose Random Image From The Directory of The Current State
    ImageName = random.choice(ImagesNames)

    ChangeBackGround(StatusOfDay, ImageName)

    # Wait For 15 Min To Move To Another Wallpaper
    time.sleep(15 * 60)
