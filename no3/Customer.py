class Customer():
    '''this is where we create new customer created'''
    def __init__(self, name, group, created_since_in_years = 2):
        '''the constructor when creating the customer
        something like the minimum requirement of creating
        the customer'''

        self.name = name
        self.group = group.lower()
        self.created_since_in_years = created_since_in_years
        # we need to throw error if not match with the list of the customer group
        print(f"Customer object created with name {self.name} within group {self.group} and join since {self.created_since_in_years} years ago.")
        
        list_group = ("employee", "affiliate", "customer")
        if (self.group not in list_group):
            raise Exception('I am sorry, the group is not in the list.')

