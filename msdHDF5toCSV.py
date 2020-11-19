"""
Alexis Greenstreet (October 4, 2015) University of Wisconsin-Madison
This code is designed to convert the HDF5 files of the Million Song Dataset
to a CSV by extracting various song properties.
The script writes to a "SongCSV.csv" in the directory containing this script.
Please note that in the current form, this code only extracts the following
information from the HDF5 files:
AlbumID, AlbumName, ArtistID, ArtistLatitude, ArtistLocation,
ArtistLongitude, ArtistName, Danceability, Duration, KeySignature,
KeySignatureConfidence, SongID, Tempo, TimeSignature,
TimeSignatureConfidence, Title, and Year.
This file also requires the use of "hdf5_getters.py", written by
Thierry Bertin-Mahieux (2010) at Columbia University
Credit:
This HDF5 to CSV code makes use of the following example code provided
at the Million Song Dataset website 
(Home>Tutorial/Iterate Over All Songs, 
http://labrosa.ee.columbia.edu/millionsong/pages/iterate-over-all-songs),
Which gives users the following code to get all song titles:
import os
import glob
import hdf5_getters
def get_all_titles(basedir,ext='.h5') :
    titles = []
    for root, dirs, files in os.walk(basedir):
        files = glob.glob(os.path.join(root,'*'+ext))
        for f in files:
            h5 = hdf5_getters.open_h5_file_read(f)
            titles.append( hdf5_getters.get_title(h5) )
            h5.close()
    return titles
"""

import sys
import os
import glob
import hdf5_getters
import re

class Song:
    songCount = 0
    # songDictionary = {}

    def __init__(self, songID):
        self.id = songID
        Song.songCount += 1
        # Song.songDictionary[songID] = self


        self.duration = None
        self.genreList = []
        self.keySignature = None
        self.keySignatureConfidence = None
        self.lyrics = None
        self.popularity = None
        self.tempo = None
        self.timeSignature = None
        self.timeSignatureConfidence = None
        self.year = None


        #--------------------- Added fields ------------------------#
        self.artistHotttness = None
        self.barsConfidence = None
        self.beatsConfidence = None
        self.loudness = None
        self.mode = None
        self.modeConfidence = None
        self.sectionsConfidence = None
        self.segmentsConfidence = None
        self.segmentsLoudnessMaxTime = None
        self.tatumConfidence = None
        self.startOfFadeOut = None
        self.endOfFadeIn = None
        self.songHotttness = None

        

    def displaySongCount(self):
        print ("Total Song Count %i" % Song.songCount)

    def displaySong(self):
        print ("ID: %s" % self.id)


def main():
    outputFile1 = open('SongCSV.csv', 'w')
    csvRowString = ""

    #################################################
    #if you want to prompt the user for the order of attributes in the csv,
    #leave the prompt boolean set to True
    #else, set 'prompt' to False and set the order of attributes in the 'else'
    #clause
    prompt = False
    #################################################
    if prompt == True:
        while prompt:

            prompt = False

            csvAttributeString = input("\n\nIn what order would you like the colums of the CSV file?\n" +
                "Please delineate with commas. The options are: " +
                "Duration, KeySignature, KeySignatureConfidence, Tempo," +
                " TimeSignature, TimeSignatureConfidence, Year," +
                " ArtistHotttness, Loudness, Mode, ModeConfidence," +
                " StartOfFadeOut, EndOfFadeIn, and SongHotttness.\n\n" +
                "For example, you may write \"Title, Tempo, Duration\"...\n\n" +
                "...or exit by typing 'exit'.\n\n")

            csvAttributeList = re.split('\W+', csvAttributeString)
            for i, v in enumerate(csvAttributeList):
                csvAttributeList[i] = csvAttributeList[i].lower()

            for attribute in csvAttributeList:
                # print "Here is the attribute: " + attribute + " \n"



                if attribute == 'Duration'.lower():
                    csvRowString += 'Duration'
                elif attribute == 'KeySignature'.lower():
                    csvRowString += 'KeySignature'
                elif attribute == 'KeySignatureConfidence'.lower():
                    csvRowString += 'KeySignatureConfidence'
                elif attribute == 'Tempo'.lower():
                    csvRowString += 'Tempo'
                elif attribute == 'TimeSignature'.lower():
                    csvRowString += 'TimeSignature'
                elif attribute == 'TimeSignatureConfidence'.lower():
                    csvRowString += 'TimeSignatureConfidence'
                elif attribute == 'Year'.lower():
                    csvRowString += 'Year'

                elif attribute == 'ArtistHotttness'.lower():
                    csvRowString += 'ArtistHotttness'
                elif attribute == 'BarsConfidence'.lower():
                    csvRowString += 'BarsConfidence'
                elif attribute == 'BeatsConfidence'.lower():
                    csvRowString += 'BeatsConfidence'
                elif attribute == 'Loudness'.lower():
                    csvRowString += 'Loudness'
                elif attribute == 'Mode'.lower():
                    csvRowString += 'Mode'
                elif attribute == 'ModeConfidence'.lower():
                    csvRowString += 'ModeConfidence'
                elif attribute == 'SectionsConfidence'.lower():
                    csvRowString += 'SectionsConfidence'
                elif attribute == 'SegmentsConfidence'.lower():
                    csvRowString += 'SegmentsConfidence'
                elif attribute == 'SegmentsLoudnessMaxTime'.lower():
                    csvRowString += 'SegmentsLoudnessMaxTime'
                elif attribute == 'TatumConfidence'.lower():
                    csvRowString += 'TatumConfidence'
                elif attribute == 'StartOfFadeOut'.lower():
                    csvRowString += 'StartOfFadeOut'
                elif attribute == 'EndOfFadeIn'.lower():
                    csvRowString += 'EndOfFadeIn'
                elif attribute == 'SongHotttness'.lower():
                    csvRowString += 'SongHotttness'
                elif attribute == 'Exit'.lower():
                    sys.exit()
                else:
                    prompt = True
                    print ("==============")
                    print ("I believe there has been an error with the input.")
                    print ("==============")
                    break

                csvRowString += ","

            lastIndex = len(csvRowString)
            csvRowString = csvRowString[0:lastIndex-1]
            csvRowString += "\n"
            outputFile1.write(csvRowString)
            csvRowString = ""
    #else, if you want to hard code the order of the csv file and not prompt
    #the user, 
    else:
        #################################################
        #change the order of the csv file here
        #Default is to list all available attributes (in alphabetical order)
        csvRowString = (
            "Duration,KeySignature,"+
            "KeySignatureConfidence,Tempo,TimeSignature,TimeSignatureConfidence,"+
            "Year," + "ArtistHotttness,Loudness,Mode,ModeConfidence," +
                "StartOfFadeOut,EndOfFadeIn,SongHotttness")
        #################################################

        csvAttributeList = re.split('\W+', csvRowString)
        for i, v in enumerate(csvAttributeList):
            csvAttributeList[i] = csvAttributeList[i].lower()
        outputFile1.write("SongNumber,")
        outputFile1.write(csvRowString + "\n")
        csvRowString = ""  

    #################################################


    #Set the basedir here, the root directory from which the search
    #for files stored in a (hierarchical data structure) will originate
    basedir = "." # "." As the default means the current directory
    ext = ".h5" #Set the extension here. H5 is the extension for HDF5 files.
    #################################################

    #FOR LOOP
    for root, dirs, files in os.walk(basedir):        
        files = glob.glob(os.path.join(root,'*'+ext))
        for f in files:
            print (f)

            songH5File = hdf5_getters.open_h5_file_read(f)
            song = Song(str(hdf5_getters.get_song_id(songH5File)))

            testDanceability = hdf5_getters.get_danceability(songH5File)
            # print type(testDanceability)
            # print ("Here is the danceability: ") + str(testDanceability)

            
            song.duration = str(hdf5_getters.get_duration(songH5File))
            # song.setGenreList()
            song.keySignature = str(hdf5_getters.get_key(songH5File))
            song.keySignatureConfidence = str(hdf5_getters.get_key_confidence(songH5File))
            # song.lyrics = None
            # song.popularity = None
            song.tempo = str(hdf5_getters.get_tempo(songH5File))
            song.timeSignature = str(hdf5_getters.get_time_signature(songH5File))
            song.timeSignatureConfidence = str(hdf5_getters.get_time_signature_confidence(songH5File))
            song.year = str(hdf5_getters.get_year(songH5File))


            song.artistHotttness = str(hdf5_getters.get_artist_hotttnesss(songH5File))
            #song.barsConfidence = str(hdf5_getters.get_bars_confidence(songH5File))
            #song.beatsConfidence = str(hdf5_getters.get_beats_confidence(songH5File))
            song.loudness = str(hdf5_getters.get_loudness(songH5File))
            song.mode = str(hdf5_getters.get_mode(songH5File))
            song.modeConfidence = str(hdf5_getters.get_mode_confidence(songH5File))
            #song.sectionsConfidence = str(hdf5_getters.get_sections_confidence(songH5File))
            #song.segmentsConfidence = str(hdf5_getters.get_segments_confidence(songH5File))
            #song.segmentsLoudnessMaxTime = str(hdf5_getters.get_segments_loudness_max_time(songH5File))
            #song.tatumConfidence = str(hdf5_getters.get_tatums_confidence(songH5File))
            song.startOfFadeOut = str(hdf5_getters.get_start_of_fade_out(songH5File))
            song.endOfFadeIn = str(hdf5_getters.get_end_of_fade_in(songH5File))

            song.songHotttness = str(hdf5_getters.get_song_hotttnesss(songH5File))

            #print song count
            csvRowString += str(song.songCount) + ","

            for attribute in csvAttributeList:
                # print "Here is the attribute: " + attribute + " \n"

                
                if attribute == 'Duration'.lower():
                    csvRowString += song.duration
                elif attribute == 'KeySignature'.lower():
                    csvRowString += song.keySignature
                elif attribute == 'KeySignatureConfidence'.lower():
                    # print "key sig conf: " + song.timeSignatureConfidence                                 
                    csvRowString += song.keySignatureConfidence
                elif attribute == 'Tempo'.lower():
                    # print "Tempo: " + song.tempo
                    csvRowString += song.tempo
                elif attribute == 'TimeSignature'.lower():
                    csvRowString += song.timeSignature
                elif attribute == 'TimeSignatureConfidence'.lower():
                    # print "time sig conf: " + song.timeSignatureConfidence                                   
                    csvRowString += song.timeSignatureConfidence
                elif attribute == 'Year'.lower():
                    csvRowString += song.year

                #" ArtistHotttness, BarsConfidence, BeatsConfidence, Loudness, Mode, ModeConfidence, Key, KeyConfidence," +
                #" SectionsConfidence, SegmentsConfidence, SegmentsLoudnessMaxTime, TatumConfidence, StartOfFadeOut, SongHotttness,"
                elif attribute == 'ArtistHotttness'.lower():
                    csvRowString += song.artistHotttness
                #elif attribute == 'BarsConfidence'.lower():
                    #csvRowString += song.barsConfidence
                #elif attribute == 'BeatsConfidence'.lower():
                    #csvRowString += song.beatsConfidence
                elif attribute == 'Loudness'.lower():
                    csvRowString += song.loudness
                elif attribute == 'Mode'.lower():
                    csvRowString += song.mode
                elif attribute == 'ModeConfidence'.lower():
                    csvRowString += song.modeConfidence
                #elif attribute == 'SectionsConfidence'.lower():
                    #csvRowString += song.sectionsConfidence
                #elif attribute == 'SegmentsConfidence'.lower():
                    #csvRowString += song.segmentsConfidence
                #elif attribute == 'SegmentsLoudnessMaxTime'.lower():
                    #csvRowString += song.segmentsLoudnessMaxTime
                #elif attribute == 'TatumConfidence'.lower():
                    #csvRowString += song.tatumConfidence
                elif attribute == 'StartOfFadeOut'.lower():
                    csvRowString += song.startOfFadeOut
                elif attribute == 'EndOfFadeIn'.lower():
                    csvRowString += song.endOfFadeIn
                elif attribute == 'SongHotttness'.lower():
                    csvRowString += song.songHotttness


                else:
                    csvRowString += "Erm. This didn't work. Error. :( :(\n"

                csvRowString += ","

            #Remove the final comma from each row in the csv
            lastIndex = len(csvRowString)
            csvRowString = csvRowString[0:lastIndex-1]
            csvRowString += "\n"
            outputFile1.write(csvRowString)
            csvRowString = ""

            songH5File.close()

    outputFile1.close()
	
main()