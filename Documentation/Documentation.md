# <font size="7"> <span style="color: #1387df;">Documentation</font> 

# <span style="color:#9fc5e8;">Preview</span> 

Alpha-Vantage-API-Data is a package for collecting stocks price and 
their related information.

Notice : Please go visit [https://www.alphavantage.co/support/#api-key](https://www.alphavantage.co/support/#api-key) to get your own free API key. 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Alpha-Vantage-API-Data.

```bash
pip install Alpha-Vantage-API-Data
```

## Update

Use the package manager [pip](https://pip.pypa.io/en/stable/) to upgrade Alpha-Vantage-API-Data.

```bash
pip install --upgrade Alpha-Vantage-API-Data
```

# <span style="color:#9fc5e8;">Contents</span>

* <font size="4">StockTimeSeries</font>

```python
from Alpha_Vantage_API_Data import API_Data_Retrieves

# returns stock daily result 
StockTimeSeries = API_Data_Retrieves.StockTimeSeries(apikey)
daily_data = StockTimeSeries.GetDailyStockPrice("IBM")
print(daily_data)

# returns stock weekly result 
StockTimeSeries = API_Data_Retrieves.StockTimeSeries(apikey)
weekly_data = StockTimeSeries.GetWeeklyStockPrice("IBM")
print(weekly_data)

# returns stock monthly result 
StockTimeSeries = API_Data_Retrieves.StockTimeSeries(apikey)
monthly_data = StockTimeSeries.GetMonthlyStockPrice("IBM")
print(monthly_data)

# returns stock Intraday result 
# Choose "1min" or "5min" or "15min" or "30min" or "60min" at time interval for intraday data
StockTimeSeries = API_Data_Retrieves.StockTimeSeries(apikey)
intraday_data = StockTimeSeries.GetIntradayStockPrice("IBM", "1min")
print(intraday_data)

# returns most likely symbols user inputs
StockTimeSeries = API_Data_Retrieves.StockTimeSeries(apikey)
search_data = StockTimeSeries.GetSearchEndpoint("IBM")
print(search_data)
```

* <font size="4">FundamentalData</font>
```python
# returns company income statements
# default annual reports 
FundamentalData = API_Data_Retrieves.FundamentalData(apikey)
incomestatement_info = FundamentalData.GetIncomeStatement("AAPL")
print(incomestatement_info)

# returns company overview
FundamentalData = API_Data_Retrieves.FundamentalData(apikey)
companyoverview_info = FundamentalData.GetCompanyOverview("AAPL")
print(companyoverview_info)

# returns listing and delisting status
FundamentalData = API_Data_Retrieves.FundamentalData(apikey)
listingdelistingstatus_info = FundamentalData.GetListingDelistingStatus()
print(listingdelistingstatus_info)

# returns incoming ipo stocks information
FundamentalData = API_Data_Retrieves.FundamentalData(apikey)
ipocalender_info = FundamentalData.FindIPOCalender()
print(ipocalender_info)

# returns company information
FundamentalData = API_Data_Retrieves.FundamentalData(apikey)
stock_company_info = FundamentalData.CompanyInfo("AAPL")
print(stock_company_info)
```

Go to [Alpha_Vantage_API_Project Issues Page](https://github.com/codemakerss/Alpha_Vantage_API_Project/issues) to report any issues.

# <span style="color:#9fc5e8;">Other</span>

For more information, please visit [Alpha Vantage Official Page](https://www.alphavantage.co) and their 
[documents](https://www.alphavantage.co/documentation/).

# <span style="color:#9fc5e8;">License</span>
[MIT](https://choosealicense.com/licenses/mit/)