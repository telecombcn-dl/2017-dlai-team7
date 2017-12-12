import pandas as pd
import matplotlib
from collections import Counter

matplotlib.use('Agg')

import matplotlib.pyplot as plt

def make_hist (num_values, name):
    plt.clf()

    plt.figure(figsize=(20, 20))
    plt.bar(range(len(num_values)), list(num_values.values()), align='center')
    plt.xticks(range(len(num_values)), list(num_values.keys()))

    plt.savefig(name + '.png')

def main():
    print ("Hello from data analysis main")

    df = pd.read_csv('/home/team7/Data/project/en_train.csv')

    columns = df['class'].value_counts()


    num_values = {}
    percentage_modif = {}

    for column in columns.keys():
        df_aux = df.loc[df['class'] == column]
        df_dif = df_aux.loc[df_aux['before'] != df_aux['after']]

        num_values[column] = len(df_aux)
        percentage_modif[column] = len (df_dif) / len(df_aux)


    make_hist(num_values, 'hist')
    make_hist(percentage_modif, 'hist_modif')


def main4():
    print("Hello from data analysis main")

    df = pd.read_csv('/home/team7/Data/project/en_train.csv')

    columns = df['class'].value_counts()

    num_values = {}
    percentage_modif = {}

    for column in columns.keys():
        df_aux = df.loc[df['class'] == column]
        df_dif = df_aux.loc[df_aux['before'] != df_aux['after']]

        num_values[column] = len(df_aux)
        percentage_modif[column] = len(df_dif) / len(df_aux)

    make_hist(num_values, 'hist')
    make_hist(percentage_modif, 'hist_modif')

def main2 ():
    print ("Hello from data analysis main2")

    df = pd.read_csv('/home/team7/Data/project/en_train.csv')

    df = df.loc[df['class'] == 'VERBATIM']

    print (df.head())

    import sys
    sys.exit()

    df['before'] = df ['before'].apply (str)
    df['beforeCount'] = df ['before'].apply (lambda x: len (x.split(' ')))

    df['after'] = df['after'].apply(str)
    df['afterCount'] = df ['after'].apply (lambda x: len (x.split(' ')))

    columns = df['beforeCount'].value_counts()

    print (df.loc[df['beforeCount'] == 2].head())

    columns.plot.bar (figsize = (20, 20))

    plt.savefig ("hist_lenPLAIN_DST.png")
def main3():
    dictionary = {1: 8957502, 2: 134575, 3: 177305, 4: 68841, 5: 30799, 6: 28000, 7: 23914, 8: 9018, 9: 1567, 10: 921, 11: 1100, 12: 544, 13: 1864, 14: 487, 15: 323, 16: 338, 17: 816, 18: 241, 19: 224, 20: 175, 21: 92, 22: 76, 23: 85, 24: 64, 25: 59, 26: 31, 27: 28, 28: 22, 29: 17, 30: 15, 31: 15, 32: 21, 33: 19, 34: 12, 35: 12, 36: 10, 37: 5, 38: 6, 39: 7, 40: 18, 41: 7, 42: 12, 43: 6, 44: 4, 45: 4, 46: 16, 47: 7, 48: 15, 49: 6, 50: 8, 51: 6, 52: 11, 53: 12, 54: 8, 55: 8, 56: 9, 57: 7, 58: 7, 59: 7, 60: 12, 61: 12, 62: 3, 63: 7, 64: 9, 65: 10, 66: 10, 67: 7, 68: 14, 69: 5, 70: 7, 71: 8, 72: 9, 73: 10, 74: 5, 75: 4, 76: 8, 77: 2, 78: 3, 79: 6, 80: 6, 81: 7, 82: 10, 83: 5, 84: 1, 85: 5, 86: 10, 87: 4, 88: 6, 89: 7, 90: 11, 91: 3, 92: 3, 93: 7, 94: 7, 95: 3, 96: 4, 97: 4, 98: 6, 99: 1, 100: 3, 101: 4, 102: 4, 103: 7, 104: 5, 105: 4, 106: 4, 107: 6, 108: 5, 109: 1, 110: 4, 111: 5, 112: 4, 113: 2, 114: 3, 115: 2, 116: 3, 117: 2, 118: 4, 119: 3, 120: 5, 121: 4, 122: 6, 123: 3, 124: 2, 125: 3, 126: 3, 127: 2, 128: 6, 129: 4, 130: 4, 131: 3, 132: 3, 133: 2, 134: 1, 137: 3, 138: 1, 139: 1, 652: 1, 141: 1, 142: 2, 143: 1, 145: 1, 146: 2, 147: 4, 150: 4, 151: 1, 152: 1, 153: 1, 154: 2, 155: 2, 156: 3, 157: 1, 158: 1, 159: 1, 160: 3, 673: 1, 162: 1, 163: 1, 164: 3, 165: 3, 167: 2, 168: 1, 169: 1, 170: 2, 171: 3, 173: 1, 174: 1, 689: 1, 180: 1, 182: 1, 183: 1, 186: 2, 187: 1, 190: 1, 196: 1, 197: 1, 199: 2, 201: 3, 202: 1, 206: 1, 207: 1, 221: 1, 223: 1, 229: 1, 230: 1, 241: 2, 252: 1, 766: 1, 261: 1, 284: 1, 291: 1, 303: 1, 1846: 1, 311: 1, 315: 1, 320: 1, 343: 1, 536: 1, 360: 1, 363: 1, 409: 1, 161: 1, 177: 1}

    make_hist(dictionary, "numWordsDST")
if __name__ == "__main__":
    main2()
