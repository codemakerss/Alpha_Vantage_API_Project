from pandas.core.frame import DataFrame
import pandas as pd
import requests
import xlwt
import csv 
class StockTimeSeries(object):

    def __init__(self, apikey : str):
        self.apikey = apikey
    
    # Get Stock Information 
    # daily stock price 
    def GetDailyStockPrice(self, stock_id : str) -> DataFrame:
        """return DataFrame type daily stock price 

        The results will show daily stock price 

        Parameters 
        ----------
        stock_id : str
            Choose the stock you want to get daily data
        """
        base_url = 'https://www.alphavantage.co/query?'
        df = pd.DataFrame()
        df_new = pd.DataFrame()
        params = {"function": "TIME_SERIES_DAILY", "symbol": stock_id, "outputsize": "full","apikey": self.apikey}
        response = requests.get(base_url, params=params)
        data = response.json() # dict
        daily_data = data["Time Series (Daily)"]
    
        for dict in daily_data:
            small_dict = daily_data[dict]
            small_dict["Datetime"] = dict
            df = df.append(pd.DataFrame([small_dict]))
        df_new = df[["Datetime", "1. open", "2. high", "3. low", "4. close", "5. volume"]]
        df_new = df_new.rename(columns = {"1. open" : "Open", "2. high": "High", "3. low" : "Low", "4. close" : "Close", "5. volume" : "Volume"})
        
        col_name = df_new.columns.tolist()
        col_name.insert(0,"Symbol")
        df_new = df_new.reindex(columns=col_name)
        df_new["Symbol"] = stock_id

        return df_new

    # weekly stock price
    def GetWeeklyStockPrice(self, stock_id : str) -> DataFrame:
        """return DataFrame type weekly stock price 

        The results will show weekly stock price 

        Parameters 
        ----------
        stock_id : str
            Choose the stock you want to get weekly data
        """
        # https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol=IBM&apikey=demo
        base_url = 'https://www.alphavantage.co/query?'
        df = pd.DataFrame()
        df_new = pd.DataFrame()
        params = {"function": "TIME_SERIES_WEEKLY_ADJUSTED", "symbol": stock_id,"apikey": self.apikey}
        response = requests.get(base_url, params=params)
        data = response.json() # dict
        daily_data = data["Weekly Adjusted Time Series"]
    
        for dict in daily_data:
            small_dict = daily_data[dict]
            small_dict["Datetime"] = dict
            df = df.append(pd.DataFrame([small_dict]))
        df_new = df[["Datetime", "1. open", "2. high", "3. low", "4. close", "5. adjusted close", "6. volume", "7. dividend amount"]]
        df_new = df_new.rename(columns = {"1. open" : "Open", "2. high": "High", "3. low" : "Low", "4. close" : "Close", "5. adjusted close" : "Adjusted Close", "6. volume" : "Volume", "7. dividend amount" : "Dividend Amount"})
        
        col_name = df_new.columns.tolist()
        col_name.insert(0,"Symbol")
        df_new = df_new.reindex(columns=col_name)
        df_new["Symbol"] = stock_id

        return df_new

    # monthly stock price
    def GetMonthlyStockPrice(self, stock_id : str) -> DataFrame:
        """return DataFrame type monthly stock price 

        The results will show monthly stock price 

        Parameters 
        ----------
        stock_id : str
            Choose the stock you want to get monthly data
        """
        # https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol=IBM&apikey=demo
        base_url = 'https://www.alphavantage.co/query?'
        df = pd.DataFrame()
        df_new = pd.DataFrame()
        params = {"function": "TIME_SERIES_MONTHLY_ADJUSTED", "symbol": stock_id,"apikey": self.apikey}
        response = requests.get(base_url, params=params)
        data = response.json() # dict
        daily_data = data["Monthly Adjusted Time Series"]
    
        for dict in daily_data:
            small_dict = daily_data[dict]
            small_dict["Datetime"] = dict
            df = df.append(pd.DataFrame([small_dict]))
        df_new = df[["Datetime", "1. open", "2. high", "3. low", "4. close", "5. adjusted close", "6. volume", "7. dividend amount"]]
        df_new = df_new.rename(columns = {"1. open" : "Open", "2. high": "High", "3. low" : "Low", "4. close" : "Close", "5. adjusted close" : "Adjusted Close", "6. volume" : "Volume", "7. dividend amount" : "Dividend Amount"})
        
        col_name = df_new.columns.tolist()
        col_name.insert(0,"Symbol")
        df_new = df_new.reindex(columns=col_name)
        df_new["Symbol"] = stock_id

        return df_new

    # intraday stock price - most recent 1 to 2 months data
    def GetIntradayStockPrice(self, stock_id : str, interval : str) -> DataFrame:
        """return DataFrame type intraday stock price 

        The results will show intraday stock price at certain 
        interval you choose 

        Parameters 
        ----------
        stock_id : str
            Choose the stock you want to get intraday data
        interval : str 
            Choose "1min" or "5min" or "15min" or "30min" or "60min" at time interval for intraday data 
        """
        # https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&outputsize=full&apikey=demo
        base_url = 'https://www.alphavantage.co/query?'
        df = pd.DataFrame()
        df_new = pd.DataFrame()
        params = {"function": "TIME_SERIES_INTRADAY", "symbol": stock_id, "interval": interval, "outputsize": "full", "apikey": self.apikey}
        response = requests.get(base_url, params=params)
        data = response.json() # dict
        ts_str = "Time Series (" + interval + ")"
        daily_data = data[ts_str]
    
        for dict in daily_data:
            small_dict = daily_data[dict]
            small_dict["Datetime"] = dict
            df = df.append(pd.DataFrame([small_dict]))
        df_new = df[["Datetime", "1. open", "2. high", "3. low", "4. close", "5. volume"]]
        df_new = df_new.rename(columns = {"1. open" : "Open", "2. high": "High", "3. low" : "Low", "4. close" : "Close", "5. volume" : "Volume"})
        
        col_name = df_new.columns.tolist()
        col_name.insert(0,"Symbol")
        df_new = df_new.reindex(columns=col_name)
        df_new["Symbol"] = stock_id

        return df_new

class FundamentalData(object):

    def __init__(self, apikey : str):
        self.apikey = apikey
        
    # Company Information 
    # Currency, GrossProfit in last 5 years - from 2016/12/31 to 2020/12/31, Total Revenue, NetIncome
    def GetIncomeStatement(self, stock_id : str) -> DataFrame:
        """return DataFrame type stock income statement

        The results will show stock annual and quarterly income statement 

        Parameters 
        ----------
        stock_id : str
            Choose the stock you want to get income statement
        """
        base_url = 'https://www.alphavantage.co/query?'
        df = pd.DataFrame()
        df_new = pd.DataFrame()
        params = {'function': 'INCOME_STATEMENT', 'symbol': stock_id, 'apikey': self.apikey}
        response = requests.get(base_url, params=params)
        data = response.json() # dict
        data_annual = data['annualReports']
        
        for dict in data_annual:
            df = df.append(pd.DataFrame([dict]))
        df_new = df.loc[:,['fiscalDateEnding','reportedCurrency','grossProfit', 'totalRevenue', 'netIncome']]
        
        col_name = df_new.columns.tolist()
        col_name.insert(0,'Symbol')
        df_new = df_new.reindex(columns=col_name)
        df_new['Symbol'] = stock_id

        return df_new

    def GetIncomeStatement_Original(self, stock_id : str) -> DataFrame:
        """return DataFrame type stock income statement

        The results will show stock annual and quarterly income statement 

        Parameters 
        ----------
        stock_id : str
            Choose the stock you want to get income statement
        """
        base_url = 'https://www.alphavantage.co/query?'
        df_annual = pd.DataFrame()
        df_quarterly = pd.DataFrame()
        params = {'function': 'INCOME_STATEMENT', 'symbol': stock_id, 'apikey': self.apikey}
        response = requests.get(base_url, params=params)
        data = response.json() # dict
        data_annual = data['annualReports']
        data_quarterly = data['quarterlyReports']
        
        for dict_1 in data_annual:
            df_annual = df_annual.append(pd.DataFrame([dict_1]))
        
        col_name = df_annual.columns.tolist()
        col_name.insert(0,'Symbol')
        df_annual = df_annual.reindex(columns=col_name)
        df_annual['Symbol'] = stock_id
        
        for dict_2 in data_quarterly:
            df_quarterly = df_quarterly.append(pd.DataFrame([dict_2]))
        
        col_name = df_quarterly.columns.tolist()
        col_name.insert(0,'Symbol')
        df_quarterly = df_quarterly.reindex(columns=col_name)
        df_quarterly['Symbol'] = stock_id

        return df_annual, df_quarterly

    # Symbol, Name, Exchange, Country, Sector, Industry, Fiscal year end, 52 Week high, 52 Week low, 50DayMovingAverage, 200DayMovingAverage, 
    def GetCompanyOverview(self, stock_id : str) -> DataFrame:
        """return DataFrame type stock company overview 

        The results will show stock company overview

        Parameters 
        ----------
        stock_id : str
            Choose the stock you want to get company overview 
        """
        base_url = 'https://www.alphavantage.co/query?'
        df_new = pd.DataFrame()
        params = {'function': 'OVERVIEW', 'symbol': stock_id, 'apikey': self.apikey}
        response = requests.get(base_url, params=params)
        data = response.json() # dict

        df = pd.DataFrame([data])
        df_new = df.loc[:,['Symbol', 'Name','Exchange','Country', 'Sector', 'Industry', 'FiscalYearEnd', '52WeekHigh', '52WeekLow','50DayMovingAverage', '200DayMovingAverage']]
        
        return df_new

    def GetCompanyOverview_Original(self, stock_id : str) -> DataFrame:
        base_url = 'https://www.alphavantage.co/query?'
        df_new = pd.DataFrame()
        params = {'function': 'OVERVIEW', 'symbol': stock_id, 'apikey': self.apikey}
        response = requests.get(base_url, params=params)
        data = response.json() # dict

        df = pd.DataFrame([data])
        
        return df
    
    # Symbol, Name, Exchange, AssetType, IPO Date, Delisting Date, Status
    # This is the new version of function
    def GetListingDelistingStatus(self) -> DataFrame:
        CSV_URL ='https://www.alphavantage.co/query?function=LISTING_STATUS&apikey=' + self.apikey
        r = requests.get(CSV_URL)
        decoded_content = r.content.decode('utf-8')

        df = pd.DataFrame()
        for i in decoded_content.splitlines():
            data_list = i.split(',')
            df = df.append(pd.DataFrame(data_list).T, ignore_index=True)
        df = df.rename(columns=df.iloc[0])
        df = df.drop(df.index[0])
        df.loc[(df["delistingDate"] == "null"), "delistingDate"] = "1970-01-01"
        return df 

    # Symbol, Name, Exchange, AssetType, IPO Date, Delisting Date, Status
    # This is the old version of function
    def GetListingDelistingStatus_Original(self) -> DataFrame:
        CSV_URL ='https://www.alphavantage.co/query?function=LISTING_STATUS&apikey=' + self.apikey
        data_lst = []
        with requests.Session() as s:
            download = s.get(CSV_URL)
            decoded_content = download.content.decode('utf-8')
            cr = csv.reader(decoded_content.splitlines(), delimiter=',')
            my_list = list(cr)
        
        for row in my_list:
            data_lst.append(row)
        df = pd.DataFrame(columns=data_lst[0], data = data_lst[1:])

        return df 

    
    # Symbol, Name, Type, Region, MarketOpen, MarketClose, Timezone, Currency, MatchScore 
    def GetSearchEndpoint(self, find_stock : str) -> DataFrame:
        ts = TimeSeries( key = self.apikey )
        data = ts.get_symbol_search(find_stock)
        data = data[0]

        df = pd.DataFrame()
        for dict in data:
            df = df.append(pd.DataFrame([dict]))
        df.columns = ['Symbol', 'Name', 'Type', 'Region', 'MarketOpen', 'MarketClose', 'Timezone', 'Currency', 'MatchScore']
        return df 
   
    # 'symbol', 'name', 'ipoDate', 'priceRangeLow', 'priceRangeHigh', 'currency', 'exchange'
    # This is the new version
    def FindIPOCalender(self) -> DataFrame:
        CSV_URL = 'https://www.alphavantage.co/query?function=IPO_CALENDAR&apikey=' + self.apikey
        r = requests.get(CSV_URL)
        decoded_content = r.content.decode('utf-8')

        df = pd.DataFrame()
        for i in decoded_content.splitlines():
            data_list = i.split(',')
            df = df.append(pd.DataFrame(data_list).T, ignore_index=True)
        df = df.rename(columns=df.iloc[0])
        df = df.drop(df.index[0])

        return df

    # Find IPO companies in the next three months
    # 'symbol', 'name', 'ipoDate', 'priceRangeLow', 'priceRangeHigh', 'currency', 'exchange'
    # This is the old version
    def FindIPOCalender_Original(self) -> DataFrame:
        CSV_URL = 'https://www.alphavantage.co/query?function=IPO_CALENDAR&apikey=' + self.apikey
        data_lst = []
        with requests.Session() as s:
            download = s.get(CSV_URL)
            decoded_content = download.content.decode('utf-8')
            cr = csv.reader(decoded_content.splitlines(), delimiter=',')
            my_list = list(cr)
                
        for row in my_list:
            data_lst.append(row)
        df = pd.DataFrame(columns=data_lst[0], data = data_lst[1:])

        return df

    # Company overview combine with the IPO date information in the listing&delisting data 
    def CompanyInfo(self, stock_id : str) -> DataFrame:
        df_income_statement = self.GetListingDelistingStatus()
        df_company_overview = self.GetCompanyOverview_Original(stock_id)
        df_company_overview = df_company_overview.loc[:,['Symbol', 'AssetType', 'Name', 'Exchange','Country', 'Sector', 'Industry']]
        df_company_IPO_date = df_income_statement.loc[df_income_statement['symbol'] == stock_id]

        df_company_overview['IpoDate'] = str(df_company_IPO_date['ipoDate'].values[0])
        df_company_overview['DelistingDate'] = str(df_company_IPO_date['delistingDate'].values[0])
        df_company_overview.loc[(df_company_overview["DelistingDate"] == "null"), "DelistingDate"] = "1970-01-01"
        df_company_overview['Status'] = str(df_company_IPO_date['status'].values[0])

        return df_company_overview

# class FileOutputCSV(object):

#     def __init__(self, apikey: str, StockTimeSeries : classmethod, FundamentalData : classmethod) -> None:
#         self.apikey = apikey
#         self.StockTimeSeries = StockTimeSeries(self.apikey)
#         self.FundamentalData = FundamentalData(self.apikey)
        
#     def CSV_Output_Original(self, stock_id : str) -> DataFrame:
#         workbook = xlwt.Workbook()
#         workbook.add_sheet('Daily Price')
#         workbook.add_sheet('Weekly Price')
#         workbook.add_sheet('Monthly Price')
#         workbook.add_sheet('Intraday Price')
#         workbook.add_sheet('Income Statement Annual')
#         workbook.add_sheet('Income Statement Quarterly')
#         workbook.add_sheet('Company Overview')
#         workbook.add_sheet('Search Endpoint Results')
#         workbook.add_sheet('US ListingDelisting Status')
#         workbook.add_sheet('IPO Calender')
#         workbook.save('Original_Data.xlsx')
#         df = self.GetIncomeStatement_Original(stock_id)
#         writer = pd.ExcelWriter('Original_Data.xlsx', engine='xlsxwriter')
#         self.GetDailyStockPrice_Original(stock_id).to_excel(writer, sheet_name='Daily Price')
#         self.GetWeeklyStockPrice(stock_id).to_excel(writer, sheet_name='Weekly Price')
#         self.GetMonthlyStockPrice(stock_id).to_excel(writer, sheet_name='Monthly Price')
#         self.GetIntradayStockPrice(stock_id).to_excel(writer, sheet_name='Intraday Price')
#         df[0].to_excel(writer, sheet_name='Income Statement Annual')
#         df[1].to_excel(writer, sheet_name='Income Statement Quarterly')
#         self.GetCompanyOverview_Original(stock_id).to_excel(writer, sheet_name='Company Overview')
#         self.GetSearchEndpoint(stock_id).to_excel(writer, sheet_name='Search Endpoint Results')
#         self.GetListingDelistingStatus().to_excel(writer, sheet_name='US ListingDelisting Status')
#         self.FindIPOCalender().to_excel(writer, sheet_name='IPO Calender')
#         writer.save()
    
#     # CSV file - Filter data 
#     def CSV_Output(self, stock_id : str) -> DataFrame:
#         workbook = xlwt.Workbook()
#         workbook.add_sheet('Daily Price')
#         workbook.add_sheet('Weekly Price')
#         workbook.add_sheet('Monthly Price')
#         workbook.add_sheet('Intraday Price')
#         workbook.add_sheet('Income Statement Annual Reports')
#         workbook.add_sheet('Company Overview')
#         workbook.add_sheet('Search Endpoint Results')
#         workbook.add_sheet('US ListingDelisting Status')
#         workbook.add_sheet('IPO Calender')
#         workbook.save('Filter_Data.xlsx')
#         writer = pd.ExcelWriter('Filter_Data.xlsx', engine='xlsxwriter')
#         self.GetDailyStockPrice(stock_id).to_excel(writer, sheet_name='Daily Price')
#         self.GetWeeklyStockPrice(stock_id).to_excel(writer, sheet_name='Weekly Price')
#         self.GetMonthlyStockPrice(stock_id).to_excel(writer, sheet_name='Monthly Price')
#         self.GetIntradayStockPrice(stock_id).to_excel(writer, sheet_name='Intraday Price')
#         self.GetIncomeStatement(stock_id).to_excel(writer, sheet_name='Income Statement Annual Reports')
#         self.GetCompanyOverview(stock_id).to_excel(writer, sheet_name='Company Overview')
#         self.GetSearchEndpoint(stock_id).to_excel(writer, sheet_name='Search Endpoint Results')
#         self.GetListingDelistingStatus().to_excel(writer, sheet_name='US ListingDelisting Status')
#         self.FindIPOCalender().to_excel(writer, sheet_name='IPO Calender')
#         writer.save()

   