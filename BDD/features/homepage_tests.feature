#Feature: Tests of homepage functionalities
#  As a user
#  I want to go through homepage functions
#  So i can see how its working and what its offering

#  Scenario: Test to see if products of category lists shows up - Music
#    When I click on products inventory
#    And I put the cursor on music category
#    Then I should see the list of categories of music section
#
#  Scenario: Test to see if products of category lists shows up - Disney
#    When I click on products inventory
#    And I put the cursor on disney category
#    Then I should see the list of categories of disney section
#
#  Scenario: Test to see if section of policy is displayed
#    When I cancel cookie section
#    And I go to policy section
#    Then I should see text displayed regarding policy
#
#  Scenario: Test the availability of assistance section
#    When I cancel cookie section
#    And I go to assistance section
#    Then I should see buttons displayed and their informations displayed
#
#  Scenario: Test of a full product purchase process
#    Given I am logged in
#    And I search another random text on site
#    Then I click on first product seen on page
#    And I add it to cart as many times as I want
#    And I click on cart button
#    And I go to checkout page
#    When I cancel cookie section
#    And I go to delivery page
#    Then I am adding an address
#    And I click on individual option
#    And I send valid inputs
#    And I go towards payment page
#    And I select to pay with cash
#    And I go to summary page
#    And I select items as gifts
#    And I fill the observations box
#    Then I finish the purchase
#
#  Scenario: Test which proves that the policy page is displayed
#    When I cancel cookie section
#    And I go to return policy
#    Then I should be able to see the tile
#    And I should be able to see the text
#