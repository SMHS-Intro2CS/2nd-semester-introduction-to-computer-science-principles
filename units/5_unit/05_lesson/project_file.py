#python code
#
#script_name: unit 5 project
#
#author: ying
#
#description: this is project 5 solution adapted from the exercise 4.2 solution sample code
#
#

#setup
from  earsketch import*
init()
setTempo(120)

#variables
drum=DUBSTEP_DRUMLOOP_MAIN_004
pad=TECHNO_CLUBRICH_PAD_002
bass=HIPHOP_BASSSUB_004
lead=ELECTRO_ANALOGUE_LEAD_004

hiphop=HIPHOP_DUSTYGROOVEPART_001
drum=DUBSTEP_DRUMLOOP_MAIN_003
panValues=[0,9.2,-9.2]
panString="0++1++2++0+11+2+"
beatPattern="0-0-0+++0--00++0"



def chorus(starting_measure, length): 
	#music section
	fitMedia(drum, 1, starting_measure, starting_measure + length)
	fitMedia(pad,2,starting_measure + 1,starting_measure + length)
	fitMedia(bass,3,starting_measure + 2,starting_measure + length)
	fitMedia(lead,4,starting_measure + 3,starting_measure + length)
	return starting_measure + length

def bridge(starting_measure, length): 
	for i in range(starting_measure, starting_measure+length, 2): 
		fitMedia(bass,1,i,i+1)
		fitMedia(bass, 2, i + 1, i+2)
	
	fitMedia(drum, 3, starting_measure, starting_measure + length)	
	return starting_measure + length

	
def verse1(start, length): 
	#one track of audio loop
	fitMedia(hiphop, 1,start,start+length)
	
	#set different effects to the track	
	setEffect(1,DISTORTION,DISTO_GAIN,25)
	
	fitMedia(drum,2,start,start+length)
	
	#add rhythmEffects to track 2
	for measure in range(start,start + length + 1):
		rhythmEffects(2, PAN, LEFT_RIGHT, panValues, measure, panString)
	return start + length


def verse2(start, length):
	fitMedia(pad, 1,start,start+length)
	fitMedia(hiphop, 2,start,start+length)
	for measure in range(start,start+length):
		makeBeat(drum,3,measure,beatPattern)
	for measure in range(start,start+length,2):
		makeBeat(bass,4,measure,beatPattern)
	return start + length

		
start = 1 
start = verse1(start, 8)
start = chorus(start, 8)
start = verse2(start, 8)
start = chorus(start, 8)
start = bridge(start, 4)
start = chorus(start, 8)

#finish
finish()
