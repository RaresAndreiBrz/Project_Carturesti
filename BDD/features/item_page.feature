Feature: Tests of item page functionalities
  As a user
  I want to see details of the products
  So i can see the caracteristics of my purchases

  Scenario: Test to see the details displayed on item page
    When I search an usual text
    And I put the cursor on music category
    Then I should see the list of categories of music section