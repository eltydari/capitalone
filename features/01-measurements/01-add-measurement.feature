Feature: Add a measurement
  In order to have source information to examine later
  I want to be able to capture a measurement of several metrics at a specific time

  Scenario: Add a measurement with valid (numeric) values
    # POST /measurements
    When I submit a new measurement as follows:
      | timestamp                  | temperature | dewPoint | precipitation |
      | "2015-09-01T16:00:00.000Z" | 27.1        | 16.7     | 0             |
    Then the response has a status code of 201
    And the Location header has the path "/measurements/2015-09-01T16:00:00.000Z"

  @new
  Scenario: Add a measurement with no values
    # POST /measurements
    When I submit a new measurement as follows:
      | timestamp                  |
      | "2015-09-01T16:00:00.000Z" |
    Then the response has a status code of 201
    And the Location header has the path "/measurements/2015-09-01T16:00:00.000Z"
    
  @new
  Scenario: Add a measurement with string numerics
    # POST /measurements
    When I submit a new measurement as follows:
      | timestamp                  | temperature | dewPoint | precipitation |
      | "2015-09-01T16:00:00.000Z" | "27.1"      | "16.7"   | "0"           |
    Then the response has a status code of 201
    And the Location header has the path "/measurements/2015-09-01T16:00:00.000Z"

  Scenario: Cannot add a measurement without a timestamp
    # POST /measurements
    When I submit a new measurement as follows:
      | temperature | dewPoint | precipitation |
      | 27.1        | 20       | 0             |
    Then the response has a status code of 400

  @new
  Scenario: Cannot add a measurement with arbitrary arithmetic to support string values
    # POST /measurements
    When I submit a new measurement as follows:
      | timestamp                  | temperature | dewPoint | precipitation |
      | "2015-09-01T16:00:00.000Z" | "15.0+12.0" | "16.7/0" | 0             |
    Then the response has a status code of 400