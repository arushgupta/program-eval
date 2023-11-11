# Program Evaluation
CS 7330 - Group Project

Refer to ProjectInstructions.pdf for project details and breakdown.

### Project Setup:
1. Install Python3<br/>

2. Install MySQL<br/>

3. Create Database called `programeval`<br/>

4. Create a user with `username` and `password` as mentioned in the `.env` file<br/>

5. Setup a virtual environment:<br/>
`python3 -m venv env`

6. Activate the virtual environment:<br/>
`source env/bin/activate`

7. Install all packages:<br/>
`pip install -r requirements.txt`

8. Make Migrations:<br/>
`python3 manage.py makemigrations`

9. Run Migrations:<br/>
`python3 manage.py migrate`

10. Create superuser:<br/>
`python3 manage.py createsuperuser`

11. Load Data: <br/>


12. Run Server:<br/>
`python3 manage.py runserver`
