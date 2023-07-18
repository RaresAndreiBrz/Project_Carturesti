# **Carturesti Project**
## *TEST PLAN*
</br>


### 1. <ins>Introduction<ins>
        I recently finished an Automation Testing course. This project is my first individual job where i decided to 
      implement my knowledge and gain more experience along the way.I chose this site because it has a lot of functionalities
      and helps me go beyond simple and usual things. I thought that complexity and dimension of the site will help me improve
      and provoke me to make steps forward.
### 2. <ins>Project details<ins>
   #### 2.1 How i started
        I started by making a list of tests that I saw as important. As a user, I am interested in being able to move around
      easily and have all the functionalities of the site working correctly. From login situations where my personal data is
      involved to the steps of purchasing, I want everything to function properly.
   #### 2.2 First steps
        I created a page and wrote the basis for tests. It's a page where the setup is initiated, including driver selection, 
      instance creation for every class and page I worked on, and opening and closing of the browser. The next file was 
      the base page, which contains a few general functions called multiple times during tests. The purpose of this is to 
      make the code simpler, well-structured, and easier to use by calling these functions whenever necessary.
   #### 2.3 Second part
        Creating a file for each page and its html locators. Each page has functions taht plays a role in defined tests
      The locators page also have the role of structuring the code and tests giving the chance to refactor at any given time.
      Files with the pages and locators are situated in separtely directories.
   #### 2.4 Writing the tests.
        At this point i started working on my lists of tests. One by one I implemented all. After each test passed/failed i went
      working on next one. Giving me the possibility to have them all correctly done at the end.
      Base test file along with the written tests and report runner file were put in 'Tests' directory of the project.
   #### 2.5 End point
        After all files were done a refactoring process was done for the entire project.
      At the end of it I ran the report in html format to have the tests results and bugs found in a readable format.
   #### 2.6 Tests results
        All tests passed,
        One test having an issue
   #### 2.7 Bugs report
        The test that confirms if a specific category selected by the user only shows the requested products has failed.
      The category in question is 'IN STOC' (In Stock) products. When the user selects this category, the site automatically 
      selects the 'Stoc Limitat' (Limited Stock) option as well. However, the user did not request this category for their 
      product search, and not only is the option automatically selected, but the user is also unable to deselect the category. 
      As a user, I find this inconvenient because I am forced to see and obtain products that I did not ask for,although i find logical
      presence of limited available products.
        The last aspect observed during testing was related to the order shipping options. The website offers multiple 
      possibilities for customers to receive their orders, but not all options are available and visible at all times. 
      Depending on the time of day when the order is placed, different options are available, while others are not even visible. 
      As a user (possibly a new user), I would like to know that there are other possibilities besides the ones currently 
      offered, even if they are unavailable for selection. Providing me with these options would be much more beneficial 
      for me when it comes to placing an order.



</br>
</br>

  
## 3. <ins>Test Implementation<ins>
   As an environment, IDE PyCharm has been chosen, with Python3.
   Chrome was the main used browser.
   During the project I used libraries as unittest, Selenium, ActionChains, time, BDD,  HtmlRunner.
   While entire programs and all the libraries are installed and working on computer system, this project can function.
   
#### 4.Other Mentions   
### Target
   The tested were done on 'https://carturesti.ro/' website.

### Risks
   This project is for learning only. Lack of experience, individual work, limited scalability and complexity of tests management 
might unbalance the quality of this project.


### CONCLUSIONS
   As the test results indicate, all the functionalities work in different situations, except for the category that can 
be interpreted as both helpful and inconvenient. The only advice I have is regarding the transportation options for client 
orders, which I strongly recommend. Providing multiple choices to the client makes it easier for them to make a decision 
based on their current situation, even if those options are available or not.

---------------------------------------------------------
### Tests used
   
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
   

   ### 3.3 Link of GitHub where this project is located

 https://github.com/RaresAndreiBrz/Project_Carturesti
