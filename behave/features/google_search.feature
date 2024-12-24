 Feature: Google Search for the Testing Academy
   Scenario: Search for TTA on Google
     Given I am on the Google Home Page
     When I search for "The Testing Academy"
     Then I should see the "The Testing Academy" in the results

   Scenario: Search for TTAH on Google
     Given I am on the Google Home Page
     When I search for "The Testing Academy Hindi"
     Then I should see the "The Testing Academy Hindi" in the results


