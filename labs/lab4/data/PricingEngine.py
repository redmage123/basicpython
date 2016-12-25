#!/usr/bin/python3

import urllib3
import re


class PricingEngine(object):
    MAXTICKERS = 200

    def __init__(self,pricingURL='https://finance.yahoo.com/d/quotes.csv'):
        self.pricingURL = pricingURL

    def getStockPrices(self,tickers):
        try:
            formattedURL = self.formatQueryString(tickers)
        except (ValueError,ex):
            print (ex)

        http = urllib3.PoolManager()
        r = http.request('GET',formattedURL)
        print (r.data)
        


    def formatQueryString(self,tickers):
        formattedURL = self.pricingURL
        formattedURL = '?'.join([self.pricingURL,'s='])
        if not type(tickers) is list:
            raise ValueError('Ticker parameter must be a list')
        if len(tickers) > PricingEngine.MAXTICKERS:
            raise ValueError('Ticker list cannot exceed 200 items')
        for ticker in tickers:
            formattedURL =  '+'.join([formattedURL,ticker])
        formattedURL = formattedURL.rstrip()
        formattedURL = '&'.join([formattedURL,'f=nab'])
        formattedURL = formattedURL.replace('=+','=')
        return(formattedURL)




if __name__ == '__main__':
    pEngine = PricingEngine()
    pEngine.getStockPrices(['GOOG','AAPL','MSFT'])





