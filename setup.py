from setuptools import setup, find_packages

setup(
    name='StockIntelligence',
    version='0.1.2',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'pyarrow',
        'numpy<2',
        'yfinance==0.2.54',
        'google',
        'google-cloud',
        'google-cloud-bigquery',
        'ta',
        'lxml'
    ],
    author="zhenxiay",
    author_email="yu.zhenxiao.yz@gmail.com",
    url="https://github.com/zhenxiay/StockIntelligence"
)
