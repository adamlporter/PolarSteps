__[Polarsteps](https://www.polarsteps.com)__ is an excellent travel / journalling program. It includes a solid app and excellent website, where you can share your travel photos / journal with your friends, family, and other followers.

Polarsteps has a great utility that will take your online data and covert it into a book.

But what if you want to get your journal entries to run through a wordprocessor?

PS has __[clear directions](https://support.polarsteps.com/article/124-how-can-i-export-a-copy-of-my-data)__ about how to download all your data. Following their directions will create a zip file with folders for each of your trips. Download and open the zip file. Inside, you will find a `user` folder and a `trip` folder. In the `trip` folder, you will find folders for each trip you have logged with PolarSteps. Each folder contains: 

1. one or more folders for each location you log; each contains folders for photos and/or videos.
1. `locations.json` - a file with all your lat/lon information in JSON format. 
1. **`trip.json`** - a file with all your journal / text entries in JSON format. This is the file this program will process!

Unfortunately, if you open the `trip.json` file with a word processor or text editor, the result is VERY confusing and hard to work with (as is typical for JSON files!).

This program makes the journal entries usable by reading the JSON file, extracting the most useful parts, and saving them as a TXT file. This file can be read by any  word processor, for further editing and stylistic improvement.

There are two ways to run this program.
1. **The easiest way is to run it in Google's Colab.** 
    1. Click on the `Process PolarSteps JSON in Colab.ipynb` file to open it in GitHub.
    1. Look in the address bar. It should say `https://github.com/adamlporter/PolarSteps/blob. . . `. Change `github.com` to `githubtocolab.com` and press  \<enter\>. This will open the notebook in Colab.
    1. Additional directions for using the program are in the Colab notebook.
1. The other way is to download the `polar_to_txt.py` program and run it on your local system. The rest of this document explains how to do this.

If you choose the latter option, you will need to have the [dateutil](https://github.com/dateutil/dateutil) library installed on your system (this allows the program to adjust the date-time stamps on the journal entries from Universal time to local time).

Instructions on how to run the file locally are below.

How to use:
1. download the program (`polar_to_txt.py`) from this github repo.
1. follow the link above to request your data archive from Polarsteps and download it to your computer.
1. open the ZIP file and extract the folders.
1. use your file explorer to find the folder where you extracted the folders in the prior step. You are looking for the folder with the `trip.json` file.
1. start a terminal / powershell in this folder.
1. run the program. The easiest way to do this is to specify the path to download folder where you saved the program. To run the program this way, in your terminal type:
```
    python3 \path_to_the_folder\polar_to_txt.py <enter>
```
* On a Windows computer, the **path_to_the_folder** might look like this:
```
    python3 \Users\<user_id>\Download\polar_to_txt.py <enter>
```
* Alternately, you could copy the program into the same directory as `trip.json` file is loaded. After copying the program into the folder, you would run it by typing:
```
    python3 polar_to_txt.py <enter>
```
The program will create an output file with a filename based on the trip name and start date ("Spain_2021-09-01.txt"). The output file will be saved in the same directory as the input file.

Known Issues:
* There is something wrong with the date-time stamp conversion. (I didn't do any journal entries at 3am!) I'm trying to figure this out and will update the program when I do. If you have ideas, please let me know!

