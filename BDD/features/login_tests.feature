Feature: Loging in situations
  As a user
  I want to login on this site
  So that i can be able to purchase products

  Scenario: Test valid login using valid credentials
    Given I click on login button
    And I select existing user
    And I enter a valid mail
    And I enter a valid password
    And I click on authentication button
    Then I should be able to see that i am logged in

  Scenario: Test invalid login with valid mail and no password
    Given I click on login button
    And I select existing user
    And I enter a valid mail
    And I enter no password
    And I click on authentication button
    Then I should be able to see an error message

  Scenario: Test invalid login with no mail and valid password
    Given I click on login button
    And I select existing user
    And I enter no mail
    And I enter a valid password
    And I click on authentication button
    Then I should be able to see an error message

  Scenario: Test invalid login with valid mail and invalid password
    Given I click on login button
    And I select existing user
    And I enter a valid mail
    And I enter an invalid password
    And I click on authentication button
    Then I should be redirected to login form page

  Scenario: Test invalid login with invalid mail and valid password
    Given I click on login button
    And I select existing user
    And I enter an invalid mail
    And I enter a valid password
    And I click on authentication button
    Then I should be redirected to login form page

  Scenario: Test login on SecondLoginPage with invalid credentials
    Given I click on login button
    And I select existing user
    And I enter an invalid mail
    And I enter an invalid password
    And I click on authentication button
    And I send invalid credentials on the login form
    And I click on authentication button from LoginForm
    Then I should be on the same page

  Scenario: Test login on SecondLoginPage with invalid mail and valid password
    Given I click on login button
    And I select existing user
    And I enter a valid mail
    And I enter an invalid password
    And I click on authentication button
    And I enter invalid mail and valid password
    And I click on authentication button from LoginForm
    Then I should be on the same page

  Scenario: Test login on SecondLoginPage with valid mail and invalid password
    Given I click on login button
    And I select existing user
    And I enter a valid mail
    And I enter an invalid password
    And I click on authentication button
    And I enter valid mail and invalid password
    And I click on authentication button from LoginForm
    Then I should be on the same page

  Scenario: Test login on SecondLoginPage with valid credentials
    Given I click on login button
    And I select existing user
    And I enter a valid mail
    And I enter an invalid password
    And I click on authentication button
    And I enter valid credentials
    And I click on authentication button from LoginForm
    Then I should be able to see that i am logged in