# Core libraries
import logging
import os

# External libraries 
import pandas as pd 


# Local folders
from CHAP.etl import ETL_Driver
from CHAP.DimReduction import DimensionalityRedn
from CHAP.Plotresult import PlotResults
from setup import config

# Docstring
doc_string="""The driver program to execute the program.""" 

# Set logging configurations
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)
logging.info('Initiating main sequence')
logging.info('Downloading files from location')


# Test 
expert_data_obj= ETL_Driver('https://www.chesdata.eu/s/CHES2019_experts.dta')

#Run Steps in Sequence 
expert_data_obj.etl.extract_dataurl()
expert_data_obj.etl.handle_NaN()
expert_data_obj.etl.minmax_scale()
expert_data_obj.etl.store_local()
print("Ran successfully , Process complete !")

"""
e = pd.read_stata('https://www.chesdata.eu/s/CHES2019_experts.dta')
a = pd.read_stata('https://www.chesdata.eu/s/CHES2019V3.dta')
"""
