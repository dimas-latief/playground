class Customer():
    '''this is where we create new customer created'''
    def __init__(self, name, group, created_since_in_years = 2):
        '''the constructor when creating the customer
        something like the minimum requirement of creating
        the customer'''

        self.name = name
        self.group = group.lower()
        self.created_since_in_years = created_since_in_years
        
        list_group = ("employee", "affiliate", "customer")

        # we need to throw error if not match with the list of the customer group
        if (self.group not in list_group):
            raise Exception('I am sorry, the group is not in the list.')

        print("Customer object created with name {} within group {} and join since {} years ago".format(self.name, self.group, self.created_since_in_years))


    def check_discount_rules(self):
        '''every group have different discount'''
        if self.group == "employee":
            return 0.3
        elif self.group == "affiliate":
            return 0.1
        elif self.group == "customer" and self.created_since_in_years >= 2:
            return 0.05
        else:
            return 1

