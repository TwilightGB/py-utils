

import pandas as pd
import matplotlib.pyplot as plt


if __name__ == '__main__':
    frame=pd.read_csv('../412.csv',engine='python')
    complaint_counts = frame["entityid"].value_counts()
    complaint_counts[:20].plot(kind='bar')
    plt.show()
    print(complaint_counts[:10])
    # data = frame.drop_duplicates(subset=None, keep='first', inplace=False)
    # data.to_csv('../d.csv', encoding='utf8')

