Feature: Search Google

  Scenario: Search for a term
    Given I am on the Google homepage
    When I enter "hello world" in the search box
    And I click the "Search" button
    Then I should see search results for "hello world"
