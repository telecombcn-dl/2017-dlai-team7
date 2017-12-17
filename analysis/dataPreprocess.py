

import time
import argparse



def main (db_file,r_index):
    print ("Hello from data preprocess")

    import csv
    import numpy as np

    if r_index == 2:
        db_file_out = db_file.replace(".csv",".txt")
    elif r_index == 3:
        db_file_out = db_file.replace(".csv","_SRC.txt")
    elif r_index == 4:
        db_file_out = db_file.replace(".csv","_DST.txt")
    else:
        print("Error! The extraction part should either 2, 3 or 4")
        
    outputFile = open (db_file_out, 'a')
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
                phraseString += row[r_index] + ' '

                counter += 1
                if counter == 20000:
                    break

            pastPhrase = int (row[0])


        print (counter)


    fTrain =  open (fb_file_out, 'r')



    content = fTrain.readlines()

    print ("Total lenght of the files")
    print (len (content))

    linesTrain = []

    linesTest = []

    for i in range (len (content)):
        line = content[i].strip()


        randValue = np.random.uniform (0, 1)
        if randValue < 0.2:
            linesTest.append(line)

        else:
            linesTrain.append(line)


    print ("Len of trainFiles")
    print (len (linesTrain))

    print ("Len of test files")
    print (len (linesTest))

    with open ('./linesTrainSRC', 'a') as f:
        for line in linesTrainSRC:
            print(line, file=f)

    with open ('./linesTrainDST', 'a') as f:
        for line in linesTrainDST:
            print(line, file=f)

    with open ('./linesTrainClass', 'a') as f:
        for line in linesTrainClass:
            print(line, file=f)

    with open ('./linesValSRC', 'a') as f:
        for line in linesTestSRC:
            print(line, file=f)

    with open ('./linesValDST', 'a') as f:
        for line in linesTestDST:
            print(line, file=f)

    with open ('./linesValClass', 'a') as f:
        for line in linesTestClass:
            print(line, file=f)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Estimate the errors between two midis')

    parser.add_argument('database_file', help='the path of the database file to convert in a list of sentences')
    parser.add_argument('extraction_part', type=int, help='the word you need, the SRC(2 for Test / 3 for Train) or the DST(4)')

    args = parser.parse_args()
    
    main (args.database_file, args.extraction_part)
