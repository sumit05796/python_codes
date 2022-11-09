class Vector:
    """reprsent vector in multi dimension space"""
    def __init__(self, d):
        """create d dimensional vector of zeros"""
        self.__coords = [0]*d
        
    def __len__(self):
        """return the dimension of vector"""
        return len(self._coords)
    
    def __getitem__(self, j):
        """return jth coordinate of vector"""
        return self._coords[j]
    
    def __setitem__(self, j, val):
        """set jth coordinate of vector to given value"""
        self._coords[j] = val
        
    def __add__(self, other):
        """return sum of two vectors"""
        if len(self) != len(other):
            raise ValueError
        result = Vector(len(self))
        
        for j in range (len(self)):
            result[j] = self[j] + other[j]
        return result
    
    def __eq__(self, other):
        """return true if vector has same coordinates as other"""
        return self.__coords == other._coords
    
    def __ne__(self, other):
        """return true if vector differs from other"""
        return not self == other 
    
    def __str__(self):
        """produce string representation of vector"""
        return '<' + str(self._coords)[1:-1] + '>' 

    
