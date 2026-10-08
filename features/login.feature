Feature: Login functionality

  Scenario: Login with valid credentials
    Given I open the AutomationExercise website
    When I navigate to the login page
    And I enter valid login credentials
    And I click the login button
    Then I should be logged in successfully
