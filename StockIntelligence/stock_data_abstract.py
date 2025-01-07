from abc import ABC, abstractmethod

#Abstract class definition
class StockDataStructure(ABC):
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def to_percentage(x):
        pass
    
    @abstractmethod
    def read_daily_data(self):
        pass
