Feature: Tests of the cart button and its functionalities
  As a user
  I want to have my shopping cart in good function
  So i can be able to control easier my list of items to buy

  Scenario: Test to check the number of items displayed on cart button
    Given I am logged in
    And I search a random text on site
    Then I click on first product seen on page
    And I add it to cart as many times as I want
    And I should see the added items number being equivalent with the number from logo cart

  Scenario: Test the limit of possible products in shopping cart #max is 10
    Given I am logged in
    And I search a word on site
    Then I click on first product seen on page
    And I add it to cart multiple times
    And I should see the added items number being equivalent with the number from logo cart

  Scenario: Test the remove button from shopping cart icon
    Given I search a word on site
    Then I click on first product seen on page
    And I add it to cart as many times as I want
    And I go back
    And I click on second product seen on page
    And I add it to cart as many times as I want
    Then I click on cart button
    And I remove an item from cart
    And I should see the added items number being equivalent with the number from logo cart

  Scenario: Test of final price shown on cart icon
    Given I am logged in
    And I search a word on site
    Then I click on first product seen on page
    And I add it to cart as many times as I want
    Then I click on cart button
    And I remove an item from cart
    And I should see the correct price of my items

