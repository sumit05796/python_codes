from xyz import XYZMeta, abstractmethod

class Sequence(metaclass = XYZMeta):
    """version of collections.Sequence abstract base class"""
    
    def __len__(self):
        """return the length of the sequence"""
        
    def __getitem__(self, j):
        """return element at index j of sequence"""
        
    def __contains__(self, val):
        """return True if val found in sequence otherwise False"""
        
        for j in range(len(self)):
            if self[j] == val:
                return True
        return False
        
    def index(self, val):
        """return leftmost index at which val is found(or raise ValueError)"""
        
        for j in range(len(self)):
            if self[j] == val:
                return j
        raise ValueError('value not in sequence')
        
    def count(self, val):
        """return no of elements equal to given value"""
        k = 0
        for j in range(len(self)):
            if self[j] == val:
                k += 1
        return k        
        