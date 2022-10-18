from yahoo_fin.stock_info import get_data
from datetime import date
import datetime

class Data():

    def __init__(self):
        self.today = date.today()
        self.last_year =  date.today() - datetime.timedelta(days=365)
        self.last_fifty = date.today() - datetime.timedelta(days=50)
        
    def year_data(self): 
        data_m= get_data("ibm", start_date=self.last_year, end_date=self.today, index_as_date = False, interval="1d")
        return data_m

    def day_data(self):
        data_t= get_data("ibm", start_date=self.last_fifty, end_date=self.today, index_as_date = False, interval="1mo")
        return data_t[-1:]
    
    def model_data(self):
        data= get_data("ibm", start_date=self.last_fifty, end_date=self.today, index_as_date = False, interval="1d")
        return data
        