Feature: Loging in situations
  As a user
  I want to login on this site
  So that i can be able to purchase products

  Scenario: Test valid login using valid credentials
    When I am on the homepage of the site
    Given I enter valid mail and valid password
    Then I should be able to see that i am logged in
    
#  Scenario: Test invalid login with no password
#    When I am on the homepage of the site
#    Given I enter valid mail and no password
#    Then I should be able to see an error on password section
#
#  Scenario: Test invalid login with no mail
#    When I am on the homepage of the site
#    Given I enter valid password and no mail
#    Then I should be able to see an error on mail section
#
#  Scenario: Test invalid login with invalid password
#    When I am on the homepage of the site
#    Given I enter invalid password and valid mail
#    Then I should be able to see an error on password section
#
#  Scenario: Test invalid login with invalid mail
#    When I am on the homepage of the site
#    Given I enter invalid mail and valid password
#    Then I should be able to see an error on mail section
#
#  Scenario: Test invalid login with invalid mail and invalid password
#    When I am on the homepage of the site
#    Given I enter invalid mail and invalid password
#    Then I should be able to see an error on mail and password section
#
#  Scenario: Test invalid login with invalid mail and valid password
#    When I am on the homepage of the site
#    Given I enter invalid mail and valid password
#    Then I should be able to see an error on mail section
#
#  Scenario: Test invalid login with valid mail and invalid password
#    When I am on the homepage of the site
#    Given I enter valid mail and invalid password
#    Then I should be able to see an error on mail section