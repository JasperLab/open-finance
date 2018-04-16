def response():
    import pandas as pd
    import os
    from pandas_datareader import data
    import fix_yahoo_finance as yf
    yf.pdr_override()
    close = pd.DataFrame()
    pct_growth = pd.DataFrame()
    tickers = ['BNS.TO', 'BAM-A.TO', 'CM.TO', 'MFC.TO', 'NA.TO', 'POW.TO', 'RY.TO', 'SLF.TO', 'TD.TO']
    close,pct_growth = load_data(tickers,close,pct_growth,pd.datetime(2011,2,16),pd.datetime(2017,2,16))
    # need a nice graph of
    return pct_growth[['portfolio']]
    # Final payout of $144.90

def load_data(tickers,close,pct_growth,start_date,end_date):
    import pandas as pd
    from pathlib import Path
    import os.path
    from pandas_datareader import data
    import fix_yahoo_finance as yf
    app_root = os.path.dirname(os.path.abspath(__file__))
    # If stock quotes are not stored locally, read from Yahoo/Google and store locally
    for symbol in tickers:
        csv_path = os.path.join(app_root, "../quotes/" + symbol + ".csv")
        if not os.path.exists(csv_path):
            print ("Loading data from Yahoo/Google: " + symbol)
            data_source='google'
            start_date = '1950-01-01'
            end_date = '2049-12-31'
            df = data.get_data_yahoo(symbol, start_date, end_date)
            df.to_csv(csv_path)

    # Combine all necessary quotes in one dataframe
    for symbol in tickers:
        csv_path = os.path.join(app_root, "../quotes/" + symbol + ".csv")
        p = Path(csv_path)
        content = []
        df1 = pd.read_csv(p,index_col="Date",parse_dates=True)
        df1 = df1[['Close']]
        df1.columns=[symbol]
        close = pd.concat([close,df1],axis=1)

    # restrict to proper dates
    filter1 = close.index >= start_date
    filter2 = close.index <= end_date
    close = close[filter1 & filter2]

# percent growth
    pct_growth = close.div(close.iloc[0])

    # maximum/minimum allowed
    pct_growth[pct_growth > 1.6] = 1.6
    pct_growth[pct_growth < 0.65] = 0.65

    # calculate portfolio return
    pct_growth['portfolio'] = pct_growth.mean(axis=1)

    # portfolio calculation is done 3 days prior to maturity
    pct_growth.iloc[-3:,-1] = pct_growth.iloc[-4,-1]

    return close,pct_growth
