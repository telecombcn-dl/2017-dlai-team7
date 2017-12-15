import numpy as np
import matplotlib
matplotlib.use('Agg')


import matplotlib.pyplot as plt


def plot_metric(path, col):
    with open(path) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip().split(',') for x in content]
    content = np.array(content)[1:].astype(float)

    plt.plot(content[:,col][:-1])


plot_metric('../attention_original/logNormal_tgt.txt.valid.log', 3)
plot_metric('./logNew.txt.valid.log', 2)

plt.legend(['ValidAccOrig', 'ValidAccNew'])

plt.savefig ('plt.png')