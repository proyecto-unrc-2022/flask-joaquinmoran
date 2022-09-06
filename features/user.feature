Feature: Handle storing, retrieving and deleting customer details # test/features/user.feature:1

  Scenario: Retrieve a customers details
    Given some users are in the system
    When I retrieve the customer 'jasonb'
    Then I should get a '200' response
    And the following user details are returned:
      | name         |
      | Jason Bourne |

  Scenario: Add a new user
    Given a user that is not in the system
    When add the new user 'John Lennon'
    Then get a '200' response
    And the following user are returned:
      | new user       |
      | John Lennon    |
 
    Scenario: Update a user from USERS
      Given users stored in the system
      When retrieve the customer 'Paul McCartney'
      Then get '200' as response
      And the following info. should be returned:
        | old name           | new name                     |
        | Paul McCartney | James Paul McCartney         |

    Scenario: Delete a user form USERS
      Given users in the system
      When retrieve the customer 'Peter Best'
      Then obtain a '200' response
      And the following information:
        | delete       |
        | Peter Best   |
    
    Scenario: List all the users from USERS
      Given a list of customers stored in the system
      When i want to show them 
      Then i want a '200' response
      And the following list:
        | names                  |
        | Jason Bourne           |
        | John Lennon            |
        | James Paul McCartney   |
   