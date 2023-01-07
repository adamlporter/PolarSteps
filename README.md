__[Polarsteps](https://www.polarsteps.com)__ is an excellent travel / journalling program. It includes a solid app and excellent website, where you can share your travel photos/journa with your friends, family, and other followers.

Polarsteps has a great utility that will take your online data and covert it into a book.

But what if you want to get your journal entries to run through Word or another wordprocess?

PS has __[clear directions](https://support.polarsteps.com/article/124-how-can-i-export-a-copy-of-my-data)__ about how to download all your data. This will create a zip file with folders for each of your trips. Once you unpack these, you will find:
1. 'photos' - a folder with all your photos
1. 'videos' - a folder with all your videos
1. 'locations.json' - a file with all your lat/long information in JSON format. 
1. 'trip.json' - a file with all your journal / text entries in JSON format.

If you want to get your journal entries into a word processor, the JSON file is a mess. 

This python program focuses on making the journal entries usable by reading the JSON file, extracting the most useful parts, and saving them as a TXT file. This file can be read by any text editor or word processor, for further editing and stylistic improvement.

How to use:
1. download the program (polar_to_txt.py).
1. use your file explorer to find the folder with the Polarsteps files (where you extracted the folders from the ZIP file you downloaded from Polarsteps).
1. start a terminal / powershell in your file explorer so that the terminal directory is where the `trip.json` file is located.
1. run the program
 * you can do this by copying the `polar_to_txt.py` program to the same folder where the `trip.json` file is located. If you do this, you would run the program by
  > python3 polar_to_txt.py <enter>

  * OR you can provide the path to the download folder where the `polar_to_text.py` was saved. If you do this, you wold run the program by 
  > python3 \user\username\downloads\polar_to_txt.py <enter>


The program will create an output file with a filename based on the trip name and start date ("Spain_2021-09-01.txt"). The output file will be saved in the same directory as the input file.
