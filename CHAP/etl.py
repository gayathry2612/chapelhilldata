# Extraction 
from pandas import read_stata

# Transformation libraries
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler


# Main driver class 
class ETL_Driver(object):
    # Initialise
    def __init__(self,url):
        self.url = url
        self.etl = ETL()

class ETL(object):
    def extract_dataurl(self):
        pass
    def handle_NaN(self):
        pass
    def standard_scale(self):
        pass
    def minmax_scale(self):
        pass
    def store_local(self):
        pass
    def store_remote(self):
        pass



 