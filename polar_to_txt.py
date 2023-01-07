"""
07 Jan 2023:
    A simple program to help people extract / convert their journal text from the JSON file
    that PolarSteps produces when a user requests a download of their data.

    PolarSteps sends users a ZIP file of their data, that contains folders with their photos and videos.
    It also has a file called 'trip.json' that contains the text of their journal entries,
    along with other data (date/time of the entry, location, weather).

    This progam will process the text.json file and produce a text file that includes 
    1. the trip summary (trip name, start/end dates, total distance, and the device used to record the trip).
    2. journal entries (date/time, location, weather, journal entry text)

    The output file is the name of the trip and the trip start date ('Spain_2022-08-15.txt').
    
"""
import sys
import os.path
import datetime
from dateutil import tz
import json

def get_data(filename= 'trip.json'):
    with open(filename) as f_in:
        data = json.load(f_in)
    return data

def write_data(data,filename=''):
    # Get the intro data
    trip_name = data['name'].strip()
    trip_start_date = datetime.datetime.fromtimestamp(data['start_date']).strftime('%Y-%m-%d')
    trip_end_date = datetime.datetime.fromtimestamp(data['end_date']).strftime('%Y-%m-%d')
    total_distance = data['total_km']
    phone_type = data['travel_tracker_device']['device_name']
    total_entries = data['step_count']

    if filename == '':
        file_out = f"{trip_name}_{trip_start_date}.txt"
    else:
        file_out = filename

    with open(file_out,'w') as f_out:
        f_out.write(f"Trip Name: {trip_name}\nStart Date: {trip_start_date}\nEnd Date: {trip_end_date}\nTotal Distance: {total_distance:,.0f} (km)\nRecording Device: {phone_type}\n\n")
        
        from_zone = tz.gettz('UTC') # PS uses Unix Epoch time, which is UTC 

        for entry in data['all_steps']:
            #location information
            location_name = entry['location']['name']
            location_lat = entry['location']['lat']
            location_lon = entry['location']['lon']

            # journal entry creation information
            to_zone = tz.gettz(entry['timezone_id'])
            creation_time = datetime.datetime.fromtimestamp(entry['creation_time'])
            creation_time = creation_time.replace(tzinfo = from_zone) # mark the TZ as UTC
            adjusted_time = creation_time.astimezone(to_zone)

            # weather info
            weather_condition = entry['weather_condition']
            temperature = entry['weather_temperature']
            
            #journal data
            journal = entry['description']
            
            #write out the current journal entry
            f_out.write(f"Date: {adjusted_time.strftime('%Y-%m-%d %H:%M')}\nLocation: {location_name} ({location_lat},{location_lon})\nWeather: {weather_condition}, Temperature: {temperature} (c)\n\n")
            f_out.write(f"{journal}\n")
            f_out.write(f"______________________________________________________________\n\n")

def printInstructions():
    print("""
Usage: navigate to the directory/folder that has the trip data from the PolarSteps journal
you wish to convert. Run this program:
    python3 (/path_to_program_directory/)polar_to_text.py \n
The program will look for a file named 'trip.json' and convert it to a text file,
with an automatically generated filename based on the name of the trip and 
the start date in that directory ('Spain_2022-09-01.txt')
""")

if len(sys.argv) > 1:
    printInstructions()
else:
    default_file = 'trip.json'
    if os.path.exists(default_file):
        data = get_data(default_file)
        write_data(data)
    else:
        print(f"Input file ({default_file}) not found.")
        printInstructions()
