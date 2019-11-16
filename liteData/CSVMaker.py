import numpy as np
import pandas as pd
import sys
def run():
    train = pd.read_csv("../data/" + sys.argv[1])
    df = pd.DataFrame(columns=['url', 'label'])

    for i in range(len(train)):
        if i%9 == 0:
            df = df.append(train[i:i+1][['url', 'label']], ignore_index=True, sort=False)

    df.to_csv(sys.argv[1]+'.csv')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: python3 CSVMaker.py train.csv')
        exit(1)
    else:
        run()