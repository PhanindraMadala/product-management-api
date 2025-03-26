Feature: Product Management

  Scenario: Reading a Product
    Given the database contains the following products
      | name  | category    | availability |
      | Laptop | Electronics | True        |
    When I request the product with id 1
    Then I should receive product details

  Scenario: Updating a Product
    Given the database contains the following products
      | name  | category    | availability |
      | Laptop | Electronics | True        |
    When I update the product with id 1 to name "New Laptop"
    Then the product should be updated successfully

  Scenario: Deleting a Product
    Given the database contains the following products
      | name  | category    | availability |
      | Laptop | Electronics | True        |
    When I delete the product with id 1
    Then the product should be removed from the database

    Scenario: Listing All Products
  Given the database contains multiple products
  When I request the list of all products
  Then I should receive a list of all available products

 
