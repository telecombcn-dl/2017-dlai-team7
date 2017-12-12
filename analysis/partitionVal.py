

import time



def main ():
    print ("Hello from data preprocess")


    import numpy as np
    fTrainSource =  open ('./outputTrainSRC', 'r')
    fTrainDST =  open ('./outputTrainDST', 'r')
    fTrainClass =  open ('./outputTrainClass', 'r')


    contentSRC = fTrainSource.readlines()
    contentDST = fTrainDST.readlines()
    contentClass = fTrainClass.readlines()


    print ("Total lenght of the files")
    print (len (contentSRC))
    print (len (contentDST))

    linesTrainSRC = []
    linesTrainDST = []
    linesTrainClass = []


    linesTestSRC = []
    linesTestDST = []
    linesTestClass = []


    for i in range (len (contentSRC)):
        lineSRC = contentSRC[i].strip()
        lineDST = contentDST[i].strip()
        lineClass = contentClass[i].strip()


        randValue = np.random.uniform (0, 1)
        if randValue < 0.2:
            linesTestSRC.append(lineSRC)
            linesTestDST.append(lineDST)
            linesTestClass.append (lineClass)

        else:
            linesTrainSRC.append (lineSRC)
            linesTrainDST.append (lineDST)
            linesTrainClass.append (lineClass)



    print ("Len of trainFiles")
    print (len (linesTrainSRC))
    print (len (linesTrainDST))

    print ("Len of test files")
    print (len (linesTestSRC))
    print (len (linesTestDST))

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
    main ()