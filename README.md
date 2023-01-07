Polarsteps is an excellent travel / journalling program. What if you want to get your journal entries to run through Word or another wordprocess?

PS will allow you to download all your data, creating a zip file with folders for each of your trips. Once you unpack these, you will find:
1. 'photos' - a folder with all your photos
1. 'videos' - a folder with all your videos
1. 'locations.json' - a file with all your lat/long information in JSON format. 
1. 'trip.json' - a file iwth all your journal / text entries in JSON format.

If you want to get your journal entries into a word processor, the JSON file is a mess. 

This python program focuses on making the journal entries usable by reading the JSON file, extracting the most useful parts, and saving them as a TXT file. This file can be read by any text editor or word processor, for further editing and stylistic improvement.

Usage:

> python3 PolarToTxt.py -infile -outfile

 * -infile (required): the JSON file included in the Polarsteps ZIP file
 * -outfile (optional): the program use the trip name + start date to create a default output file ("Spain_2022-09-07.txt"). You can specify another file name, if you wish to do so.

The .TXT file will be put in the same directory as the JSON file. 