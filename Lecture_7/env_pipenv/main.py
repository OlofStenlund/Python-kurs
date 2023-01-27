import os
import csv
from gtts import gTTS


def main():
    with open("data.csvt", encoding="utf-8") as file:
        csvreader = csv.reader(file)
        headings = next(csvreader) # saves the first row in a variable
        # print(headings)
        data = []
        for row in csvreader:
            data_object = {headings[i]: col for i, col in enumerate(row)}
            data.append(data_object)
        print(data[0])

        # row1 = next(csvreader) # saves the next row that has not allready been saved
        # # Points to the next row each time
        # print(row1)

    searchword = input("search word: ")    
    for obj in data: # Loops through each instance in data
        if searchword in obj["anforandetext"]: # Looks for the searchword in the value 'anförandetext', which is the trascription of the speech
            print(f"Rubrik: {obj['avsnittsrubrik']}") # Goes to the object and gets the header
            print(f"Talare: {obj['talare']}") # goes to the object and gets the speaker
            sound = gTTS(text=obj['anforandetext'], lang='sv', slow=False) # Makes a sound file named 'sound' out of the text
            filename = f"{obj['avsnittsrubrik']}.mp3" # creates a filename based on the header
            sound.save(filename) # Saves the soundfile with the filename as name






main()
