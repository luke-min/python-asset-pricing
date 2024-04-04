import pandas as pd
import numpy as np
import yfinance as yf
from common_utils import enforce_list



class PPSDataProvider(object):

    def __init__(self, logger):
        self.logger = logger

    def get_price_data(self, tickers, start_date, end_date):
        tickers = enforce_list(tickers)
        self.logger.info("Getting price for tickers: {}".format(tickers))

        df_concat = pd.DataFrame()

        for ticker in tickers:
            df = yf.download(ticker, start=start_date, end=end_date)
            df.reset_index(inplace=True)
            df = pd.melt(df, id_vars="Date", var_name="field", value_name="value")
            df['TICKER'] = ticker
            # Concatenate dataframe for each ticker to the overall dataframe
            df_concat = pd.concat([df_concat, df], ignore_index=True)

        # Output formatting
        upcase_map = {col : col.upper() for col in df_concat.columns}
        df_concat = df_concat.rename(columns=upcase_map)
        df_concat["DATE"] = pd.to_datetime(df_concat["DATE"])

        if df_concat.empty:
            self.logger.warn("Empty dataframe - no data was pulled. Please check!")

        return df_concat



