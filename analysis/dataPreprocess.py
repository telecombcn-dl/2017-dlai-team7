

import time



def main ():
    print ("Hello from data preprocess")

    import csv


    outputFile = open ("outputTrainDST", 'a')
    with open ('/home/team7/Data/project/en_train.csv', 'r') as f:
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
    main ()