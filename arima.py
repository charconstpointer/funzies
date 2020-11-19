import pandas as pd
import matplotlib.pylab as plt
from statsmodels.tsa import arima_model


def main():
    cols = ['<DTYYYYMMDD>', '<CLOSE>']
    df = pd.read_csv('./CDPROJEKT.mst', usecols=cols)
    df['<DTYYYYMMDD>'] = pd.to_datetime(df['<DTYYYYMMDD>'], format="%Y%m%d")
    df.columns = ['Date', 'Price on close']
    df.set_index('Date', inplace=True)
    df.index = pd.DatetimeIndex(df.index).to_period('d')
    print(len(df))
    snap = df[4000:]
    model = arima_model.ARIMA(snap, order=(3, 2, 2)).fit()
    model.plot_predict(start=2156, end=2520)
    plt.show()
    pass


if __name__ == '__main__':
    main()
