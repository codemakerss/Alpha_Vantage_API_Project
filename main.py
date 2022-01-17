import API_Data_Retrieve as api 
apikey = "YTK6VG8ZMVOB0Z0H"
alpah_vantage = api.FundamentalData(apikey)
data = alpah_vantage.CompanyInfo("IBM")
print(data)
    