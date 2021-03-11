from CHAP.etl import ETL_Driver
from CHAP.DimReduction import DimensionalityRedn
from CHAP.Plotresult import PlotResults 

"""
The driver program to execute the steps. 

""" 

# Test 
expert_data_obj= ETL_Driver('https://www.chesdata.eu/s/CHES2019_experts.dta')
#Steps in Sequence 
expert_data_obj.etl.extract_dataurl()
expert_data_obj.etl.handle_NaN()
expert_data_obj.etl.minmax_scale()
expert_data_obj.etl.store_local()
print("Ran successfully , Done !")

"""
e = pd.read_stata('https://www.chesdata.eu/s/CHES2019_experts.dta')
a = pd.read_stata('https://www.chesdata.eu/s/CHES2019V3.dta')
"""
