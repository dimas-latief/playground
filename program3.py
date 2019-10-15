from no3.customer import Customer
from no3.transaction import Transaction

def main():
    ## test case 1 ##
    print("test case 1")
    print("------------------------------------------")
    employee_test = Customer("employee_test", "Employee")
    discount_rules = employee_test.check_discount_rules()
    employee_test_transaction = Transaction(1000, discount_rules)
    employee_test_transaction.total_payable()
    print("------------------------------------------")

    ## test case 2 ##
    print("test case 2")
    print("------------------------------------------")
    affiliate_test = Customer("affiliate_test", "affiliate")
    discount_rules = affiliate_test.check_discount_rules()
    affiliate_test_transaction = Transaction(1000, discount_rules)
    affiliate_test_transaction.total_payable()
    print("------------------------------------------")

    ## test case 3 ##
    print("test case 3")
    print("------------------------------------------")
    customer_test_minimum_2_years = Customer("customer_test_minimum_2_years", "customer")
    discount_rules = customer_test_minimum_2_years.check_discount_rules()
    customer_test_minimum_2_years_transaction = Transaction(1000, discount_rules)
    customer_test_minimum_2_years_transaction.total_payable()
    print("------------------------------------------")

    ## test case 4 ##
    print("test case 4")
    print("------------------------------------------")
    customer_test_minimum_1_year = Customer("customer_test_minimum_1_year", "customer", 1)
    discount_rules = customer_test_minimum_1_year.check_discount_rules()
    customer_test_minimum_1_year_transaction = Transaction(1000, discount_rules)
    customer_test_minimum_1_year_transaction.total_payable()
    print("------------------------------------------")

    ## test case 5 ##
    print("test case 5")
    print("------------------------------------------")
    employee_groceries_test = Customer("employee_groceries_test", "employee", 1)
    discount_rules = employee_groceries_test.check_discount_rules()
    employee_groceries_test_transaction = Transaction(1000, discount_rules,"Groceries")
    employee_groceries_test_transaction.total_payable()
    print("------------------------------------------")

    ## testing the function ##
    print("test case 5 Function Test")
    print("------------------------------------------")
    test_deduction = Transaction(990)
    print("assert function total_price_deduction_rules()")
    assert test_deduction.total_price_deduction_rules() == 45, "Should be 45"
    print("assert finish. if no error, meaning testing pass")

main()