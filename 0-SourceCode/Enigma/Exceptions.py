
"""
Enigma Exceptions
"""

class InvalidPlugError(Exception):
    """Invalid Plug Exception"""
    def __init__(self, value):
        super(self.__class__, self).__init__()
        self.value = value
    def __str__(self):
        return repr(self.value)
        
class PlugBoardFullError(Exception):
    """PlugBoard Full Exception"""
    def __init__(self, value):
        super(self.__class__, self).__init__()
        self.value = value
    def __str__(self):
        return repr(self.value)
        
class InvalidRotorError(Exception):
    """Invalid Rotor Exception"""
    def __init__(self, value):
        super(self.__class__, self).__init__()
        self.value = value
    def __str__(self):
        return repr(self.value)
        
class InvalidReflectorError(Exception):
    """Invalid Reflector Exception"""
    def __init__(self, value):
        super(self.__class__, self).__init__()
        self.value = value
    def __str__(self):
        return repr(self.value)
        
class RotorLocationException(Exception):
    """Invalid Rotor Location Exception"""
    def __init__(self, value):
        super(self.__class__, self).__init__()
        self.value = value
    def __str__(self):
        return repr(self.value)
        
class PlugBoardNotSupported(Exception):
    """"""
    def __init__(self, value):
        super(self.__class__, self).__init__()
        self.value = value
    def __str__(self):
        return repr(self.value)
