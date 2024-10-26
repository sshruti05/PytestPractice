Feature: Bank transactions
  Tests pertaining to banking transactions like withdrawl, deposite

  Scenario: Withdrawl of money
    Given account balance is 100
    When the account holder withdraws 30
    Then the account balance should be 70