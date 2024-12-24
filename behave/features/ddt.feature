Feature: Showing off behave with Scenario outline

  Scenario Outline: Run a simple test with argument
    Given we have behave installed
    When we say <greeting>
    Then behave should respond with <response>
    Examples:
      | greeting |  | response        |
      | Hello    |  | Hi there!       |
      | Goodbye |  | See you later!  |
      | Thanks   |  | You're welcome! |

