

import time
import argparse



def main (db_file,r_index):
    print ("Hello from data preprocess")

    import csv

    if r_index == 3:

        db_file_out = db_file.replace(".csv","_SRC.txt")
    elif r_index == 4:
        db_file_out = db_file.replace(".csv","_DST.txt")
    else:
        print("Error! The extraction part should or 3 or 4")
        
    outputFile = open ("outputTrainDST", 'a')
    with open (db_file, 'r') as f:
        reader = csv.reader(f)

        counter = 0
        pastPhrase = 0
        reader.__next__()
        phraseString = ''
        for row in reader:
            if pastPhrase == int (row[0]):
                #We are still on the current phrase
                phraseString += row[r_index] + ' '
            else:
                print (phraseString, file = outputFile)
                phraseString = ""
                phraseString += row[4] + ' '

                counter += 1
                if counter == 20000:
                    break

            pastPhrase = int (row[0])


        print (counter)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Estimate the errors between two midis')

    parser.add_argument('database_file', help='the path of the database file to convert in a list of sentences')
    parser.add_argument('extraction_part', type=int, help='the word you need the SRC(3) or the DST(4)')

    args = parser.parse_args()
    
    main (args.database_file, args.extraction_part)
