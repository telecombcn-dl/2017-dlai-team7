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


plot_metric('./logNormal_tgt.txt.train.log', 3)
plot_metric('./logNormal_tgt.txt.valid.log', 3)

plt.legend(['TrainAcc', 'ValAcc'])

plt.savefig ('plt.png')