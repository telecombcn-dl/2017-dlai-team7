

import time



def main (db_file,):
    print ("Hello from data preprocess")

    import csv

    db_file_out = db_file.replace(".csv","_"++".txt")
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
                phraseString += row[4] + ' '
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
    parser.add_argument('', help='')

    args = parser.parse_args()
    
    main ()
