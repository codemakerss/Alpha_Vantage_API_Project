# Alpha_Vantage_API_Data - Financial Data Retrieving

Alpha_Vantage_API_Data is a package for collecting stocks price and 
their related information.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Alpha_Vantage_API_Data.

```bash
pip install Alpha_Vantage_API_Data
```

## Example

```python
from Alpha_Vantage_API_Data import API_Data_Retrieves

# returns stock daily result 
StockTimeSeries = API_Data_Retrieves.StockTimeSeries(apikey)
daily_data = StockTimeSeries.GetDailyStockPrice("IBM")
print(daily_data)

# returns company information
FundamentalData = API_Data_Retrieves.FundamentalData(apikey)
stock_company_info = FundamentalData.CompanyInfo("AAPL")
print(stock_company_info)
```

Go to [Alpha_Vantage_API_Project Issues Page](https://github.com/codemakerss/Alpha_Vantage_API_Project/issues) to report any issues.

## License
[MIT](https://choosealicense.com/licenses/mit/)