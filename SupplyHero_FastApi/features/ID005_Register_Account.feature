Feature: Register Account
As a new SupplyHero user
I want to register for a new SupplyHero account
So that I can login to my SupplyHero account

  Scenario: Registering for an account (Normal Flow)
  
    Given user who does not have an existing account
    When user requests to register with the following information
    |email		   		| password	 |
    |kaldamzxmczk12@hotmail.com	| a!s@d#	 |
    Then a new account is created
    
  Scenario: Registering for an already existing account (Error Flow)
  
    Given user who already have an existing account
    When user requests to register with the following information
    Then user is informed that An account with that email already exists.
  
