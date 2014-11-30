# forked from https://github.com/Ultraschall/Coding-Shownotes-Python/tree/f51d1e0c0cc45b676402ba5eb59c4ef4f89daa5b  to fulfil "Learn Python the Hard Way | Exercise 41: Learning To Speak Object Oriented | Reading More Code" http://learnpythonthehardway.org/book/ex41.html


import os
import sys
import codecs
import os.path
import datetime

# Get the Reaper scripts folder and add it to pythons library path
script_path = os.path.join(os.path.expanduser("~"), 'Library', 'Application Support', 'REAPER', 'Scripts')
sys.path.append(script_path)
from sws_python64 import *

import ultraschall_functions as ULT

__author__ = "Malte Dreschert, Ralf Stockmann"
__copyright__ = "Copyright 2014, Ultraschall"
__credits__ = []
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = ""
__email__ = ""
__status__ = "Development"


def export_chapter_marks():
	track = ULT.getTrackByName('Chapters')

	lines = []

	for i in range(RPR_CountTrackMediaItems(track)):
		item = RPR_GetTrackMediaItem(track, i)
		time = RPR_GetMediaItemInfo_Value(item, 'D_POSITION')
		timestr = RPR_format_timestr_pos(time, None, 5, 5)[1]

		msg_text = ULT_GetMediaItemNote(item)
		lines.append(timestr + ' ' + msg_text + '\n')

	#def a():

	#	selected_file_tuple = RPR_GetUserFileNameForRead(None, 'Select Shownote file to import', 'osf')
	#	filepath = None
	#	if(selected_file_tuple[0] == 0):
	#		return
	#	else:
	#		filepath = selected_file_tuple[1]

	filepath = os.path.join(os.path.expanduser("~"), 'Desktop', 'chapter_test.mp4chaps')
	# open the file and read the content into an arrayreap
	with codecs.open(filepath, 'w', encoding='utf-8') as f:
		f.writelines(lines)

export_chapter_marks()

