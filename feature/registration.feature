Feature: Registration
  Scenario: Registration with valid data
    Given I open the website
    And click on Sign button
    And enter email click on Sign up
    When Registration page opens
    And I enter firstname <john>
    Then Verify home page opened