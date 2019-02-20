# Review and introduction to basic CRUD

Begin by opening the starter project in intelliJ. The starter project has an existing data model with a few instance records that you will use for your project. Start the server and ensure it is working properly by going to http://127.0.0.1:8000/census/admin

### NOTE: It is acceptable to log results to the console. After EVERY operation, print the list of all object instance records in the database.

### Exercise 1:
Create a view and corresponding route for endpoint ```createres/``` that will add a new Respondent to the database. Use the functions provided in ```views.py``` to generate a random name, age, and salary. Print the resulting collection of ALL instance records from the database.

### Exercise 2:
Create a view and corresponding route for endpoint ```readres/``` that will retrieve all of the Respondent instance records and print the result

### Exercise 3:
Create a view and corresponding route for endpoint ```updateres/``` that will update the salary of the Respondent ```Joe Walsh``` and print the his updated record once changes are saved. Use the random salary function to get a new salary.

### Exercise 4:
Create a view and corresponding route for endpoint ```deleteres/``` that will delete a specific Respondent of your choosing. Print all of the Respondent instance records BEFORE *and* AFTER the delete operation. HINT: Use the  ```admin``` web app to add record(s) with a name of your choosing so you will have one to delete http://http://127.0.0.1:8000/admin/

### Challenges:
* Implement a view and corresponding route for endpoint ```richdudes/``` that will return a list of all respondents with a salary over 200000
* Implement a view and corresponding route for endpoint ```olddudes/``` that will return a list of all respondents with an age over 80
* Return a response as HTML to the browser after every operation
* Enhance the code for the ```readres``` view to print each Respondent record individually, one per line
* Enhance the code for the ```readres``` view to return the list of Respodents as pretty printed HTML (HINT: A HTML table is fine)

### NOTE:
superuser user ID and password is ```student``/```C0d3Cr3w```
