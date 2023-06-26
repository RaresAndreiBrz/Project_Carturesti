# **Carturesti Project**
## *TEST PLAN*
</br>

### Revision History

|    Date    | Description |       Author        |              Comments               |
|:----------:| :-------------:|:-------------------:|:-----------------------------------:|
| 01.06.2023 | v1.0 | Brinza Rares Andrei |             Draft Plan              |
| 03.06.2023 | v1.1  |   Brinza Rares Andrei     |        Tests implementation         |
| 25.06.2023 | v1.2 |   Brinza Rares Andrei     | Test Results for Functional Testing | 
</br>
</br>

#### 1. <ins>Introduction<ins>
   #### 1.1 Project objective
   #### 1.2 Functionalities in scope
   #### 1.3 Functionalities and tests out of scope
#### 2. <ins>Test Process<ins>
   #### 2.1 Test Planning
   #### 2.2 Test Analysis
   #### 2.3 Test Design
   #### 2.4 Test Implementation
   #### 2.5 Test Execution
   #### 2.6 Test Completion
   #### 2.7 Test Monitoring and Control
#### 3.<ins> Test Deliverables<ins> 
   #### 3.1 Test plan
   #### 3.2 Test cases
   #### 3.3 Traceability matrix
   #### 3.4 Test case results
   #### 3.5 Bugs report
</br>
</br>
   
## 1. <ins>Introduction<ins>
   This test plan describes the strategies, process, workflows and methodologies used to plan, organize, execute and manage testing process for Carturesti browser application.
### 1.1 Project objective
   The scope of this project is to use knowledge gained through the recently finished course and apply them in practice using a live application. 
   
   [Application under test](https://carturesti.ro/)
   
   **Tools**: Selenium, BDD Behavior_driven_development
</br>  
   
### 1.2 Functionalities in scope
   All features of the target website's user module need to be covered by automated tests using Selenium and BDD (Behavior-Driven Development) framework./
The objective of the automated tests is to ensure the proper functioning and behavior of the website's user module. The tests should cover functional scenarios, GUI interactions, and API integrations, as specified in the requirements.

The Selenium-based automated tests will simulate user actions and interactions with the website's interface. The BDD framework will provide a structured approach to define test scenarios in a human-readable format and facilitate collaboration between technical and non-technical stakeholders.

The automated tests will validate the functionality of each feature, ensuring that the expected results are obtained, the GUI elements are displayed correctly, and the API integrations work as intended.
   

### 1.3 Functionalities and tests out of scope
  - All functionalities that the web aplication offers to users.
  - Non-functional testing like stress, performance is beyond scope of this project.
  - No QA support for mobile application developed. Only web application will be tested.
  
## 2. <ins>Test Process<ins>
  ### 2.1 Test Planning 
   
#### Roles and responsabilities:
| **Role** | **Name** |
| :-------------: | :-------------:| 
| Software Developer | Brinza Rares Andrei |
| Project Manager| Brinza Rares Andrei |

   
#### Entry criteria :
   - Functional specification defined
#### Exit criteria : 
   - All test cases have been executed
   - The number of unresolved bugs is insignificant or have low priority
   - All resolved bugs have been re-tested  
   - Deadline was reached
   - No detected major risks remained unresolved
   
#### Risks :
   ***Project risks***:
   - Lack of experience of the developer
   - Only one person responsabile for the project
   - Complexity of test management
   - Test environment instability
   - Limited test scalability
   
   ***Product risks***:
   - Confusing user interface.
   - Poor performance or slow response time. 
   - Unstable software or frequent errors. 
   - Compatibility issues with platforms and browsers. 
   - Security vulnerabilities.
   
### 2.2 Test Analysis
   - analyze business requirements to make sure that we have all information for creating the test condition
   - write test conditions that will be tested out in test process
   
   ***Test Conditions:***
   
   1. Test that user can create an account
   2. Test the sign-in functionality by completing the login process with valid credentials.
   3. Test the case where the password field is left empty during the sign-in process.
   4. Test the case where the email field is left empty during the sign-in process.
   5. Test the case where an incorrect password is entered during the sign-in process.
   6. Test the case where an incorrect email is entered during the sign-in process.
   7. Test the scenario where both email and password are incorrect on the second login page.
   8. Test the scenario where the email is incorrect but the password is correct on the second login page.
   9. Test the scenario where both the email and password are correct on the second login page.
   10. Test the scenario where a search for an unavailable product is performed, and checks if the appropriate error message is displayed.
   11. Test the sorting of products by price in ascending order.
   12. Test the sorting of products by price in descending order.
   13. Test the sorting of products alphabetically in ascending order that are in stock.
   14. Test the sorting of products alphabetically in descending order that are in stock.
   15. Test the sorting of products by discount in descending order.
   16. Test the sorting of products by discount in ascending order.
   17. Test the number of elements shown on the page and verifies if it matches the expected value.
   18. Test if the number of items in the cart matches the expected value.
   19. Test if the "Only in stoc" button is active when filtering products. 
   20. Test the relevance of products received based on the author's name.
   21. Test the relevance of products received based on the product name.
   22. Test if the limit of 10 products in the cart is enforced.
   23. Test the removal of items from the cart.
   24. Test if the final price is correctly displayed in the cart button.
   25. Test if the details are correctly displayed on the item page.
   26. Test adding a product to the wishlist and checks if it appears in the wishlist.
   27. Test the removal of items from the checkout page.
   28. Test the scenario where incorrect delivery inputs are inserted
   29. Test for finishing an order at the specified address.
   30. Test for checking the display of the return policy.
   31. Test for checking the items in the music category.
   32. Test for checking the items in the Disney category.
   33. Test for checking the display of button information.
   34. Test for checking the display of the categories list.
  
   
### 2.3 Test Design
   - functional test cases will be created in PyCharm 
   - test cases using the Selenium WebDriver in Python
   - Chrome Driver used for the automated tests


### 2.4 Test Implementation
   Verify that the following elements are ready before the test execution phase: 
   - test environment is up and running:  https://carturesti.ro/ (acces not required for the current situation)
   - Python v3.1 along with PyCharm installed.
   
### 2.5 Test Execution
   - bug reports were created based on the failed test cases. 
   - test cases were executed 

### 2.6 Test Completion
   This project was created for personal porposes only. 
   
### 2.7 Test Monitoring and Control   
   Generate periodic reports to check the project status: status for the test cases executed.

repooooooooooooooooort ###########################

## 3.<ins> Test Deliverables<ins> 
   ### 3.1 Test plan
   No further plans.
   
   ### 3.2 Tests cases

 [Test cases](https://github.com/RaresAndreiBrz/Project_Carturesti/tree/main/Tests)

   

   ### 3.3 Traceability matrix

![Traceability matrix](https://github.com/RaresAndreiBrz/Project_Carturesti/)


   ### 3.4 Test case results

[Test Cases Results](repoooort link git)

   ### 3.5 Bugs report
   
[Bugs](report BUUUGS)


