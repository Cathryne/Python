# forked from https://github.com/Ultraschall/Coding-Shownotes-Python/tree/f51d1e0c0cc45b676402ba5eb59c4ef4f89daa5b  to fulfil "Learn Python the Hard Way | Exercise 41: Learning To Speak Object Oriented | Reading More Code" http://learnpythonthehardway.org/book/ex41.html


import sys
import os.path
import datetime

# Get the Reaper scripts folder and add it to pythons library path
script_path = os.path.join(os.path.expanduser("~"), 'Library', 'Application Support', 'REAPER', 'Scripts')
sys.path.append(script_path)
from sws_python64 import *

from reaper_python import *

def msg(msg_text):
	RPR_ShowConsoleMsg(msg_text)

def getTrackByName(name):
	"""iterate all tracks and find the one with the specified name"""
	for i in range(RPR_GetNumTracks()):
		track = RPR_GetTrack(0, i)
		track_name = RPR_GetSetMediaTrackInfo_String(track, 'P_NAME', None, False)[3]
		if track_name == name:
			return track
		else:
			continue
