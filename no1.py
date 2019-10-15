# global variable define as dictionary
text = {}

def store(a):
    '''
    Store function
    input params: a dict. example {"key1":"value1"}
    Big(O) analysis: O(1) --> its constant
    '''
    text.update(a) # using update funtion to add new dict

def load(a):
    '''
    load function
    params: what object we want to get, in this case is text dict object
    return: string type format
    Big(O) analysis: O(n) --> Runtime grows directly in proportion to n.
    In here n is the lenght of the dictionary
    '''
    new_form = "" # init empty string
    for k,v in a.items(): # unpackage the tuple to have the key and value
        new_form += k +"="+v+";\n" # append string
    print(new_form) # printing out
    return new_form