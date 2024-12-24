Feature: Showing off behave with Scenario outline

  Scenario Outline: Run a DDT on app.vwo.com
    Given open the app.vwo.com
    When I enter <username> and <password>
    And I click the sign-in button
    Then I get this <message>
    Examples:
      | username |  | password | message                                                    |
      | admin    |  | admin    | Your email, password, IP address or location did not match |
      | admin    |  | admin123 | Your email, password, IP address or location did not match |
      | admin    |  | password | Your email, password, IP address or location did not match |
