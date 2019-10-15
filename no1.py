# global variable define as dictionary
text = {}

def store(a):
    '''
    Store function
    input params: a dict. example {"key1":"value1"}
    Big(O) analysis: O(1) --> its constant
    '''
    text.update(a) # using update funtion to add new dict