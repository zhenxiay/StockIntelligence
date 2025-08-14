'''
This module defines an abstract class for stock data structures.
'''

from abc import ABC, abstractmethod

class StockDataStructure(ABC):
    '''
    Abstract class definition for stock data structures.
    '''
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def read_daily_data(self):
        '''
        Mandatory method to read daily stock data.
        This method should be implemented in the derived classes.
        '''
        pass
