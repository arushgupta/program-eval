# Program Evaluation
CS 7330 - Group Project

Refer to ProjectInstructions.pdf for project details and breakdown.

### Project Setup:
1. Install Python3<br/>

2. Install PostgreSQL<br/>

3. Create Database called `programeval`<br/>

4. Create a user with `username` and `password` and grant it privileges to the database.<br/>

5. Setup a virtual environment:<br/>
`python3 -m venv env`

6. Activate the virtual environment:<br/>
`source env/bin/activate`

7. Create a .env file within the program (file should be located next to this README.md).<br/>

8. Update the database environment variables with your username, password, and port.<br/>

9. Install all packages:<br/>
`pip install -r requirements.txt`

10. Make Migrations:<br/>
`python3 manage.py makemigrations`

11. Run Migrations:<br/>
`python3 manage.py migrate`

12. Load Data: <br/>
`python3 manage.py loaddata university/fixtures/*.json`

13. Run Server:<br/>
`python3 manage.py runserver`
