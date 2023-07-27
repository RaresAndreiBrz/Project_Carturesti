Feature: Tests of check out page functionalities
  As a user
  I want to be able to reconsider my purchases
  So I can decide easier if I am not happy with my choice

  Scenario: Test the button that removes a product from the page
    Given I am logged in
    And I search a new word on site
    Then I click on first product seen on page
    And I add it to cart as many times as I want
    And I go back
    And I click on second product seen on page
    And I add it to cart as many times as I want
    And I click on cart button
    And I go to checkout page
    And I check the price of my products
    When I random remove a product from list
    Then I should have the total price of my products correctly displayed
