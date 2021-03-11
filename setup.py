"""
Might not be needed with docker setup. Will take that decision later

"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = [
    'description': 'Chapel Hill Expert survey data analysis 2019',
    'author': 'Gayathry Dasika',
    'github': 'gayathry2612',
    'email':'gayathrydasika@gmail.com'
    'data citation':'Ryan Bakker, Liesbet Hooghe, Seth Jolly, Gary Marks, Jonathan Polk, Jan Rovny, Marco Steenbergen, and Milada Anna Vachudova. 2020. “2019 Chapel Hill Expert Survey.” Version 2019.1. Available on chesdata.eu. Chapel Hill, NC: University of North Carolina, Chapel Hill.',
    'download_url':'https://www.chesdata.eu/2019-chapel-hill-expert-survey',
    'Expert_stata_url':'https://www.chesdata.eu/s/CHES2019_experts.dta',
    'Average_stata_url':'https://www.chesdata.eu/s/CHES2019V3.dta',
    'version':'0.1',
    'install_requires':['nose'],
    'packages':['CHAP'],
    'scripts':[],
    'name':'Chapel_hill_analysis',
]
setup(**config)
