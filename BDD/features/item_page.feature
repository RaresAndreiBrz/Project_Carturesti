#Feature: Tests of item page functionalities
#  As a user
#  I want to see details of the products
#  So I can see the characteristics of my purchases
#
#  Scenario: Test to see the details of the product displayed on item page
#    Given I search a product on site
#    Then I click on first product seen on page
#    Then I should see the box that contains the informations about the product
#
#  Scenario: Test to if a product can be added to wishlist
#    Given I am logged in
#    And I search a random word on site
#    When I cancel cookie section
#    Then I click on first product seen on page
#    And I add it to my wishlist
#    And I click on my account button
#    And I click on wishlist button
#    And I check the presence of my product in wishlist
#    And I remove it from wishlist