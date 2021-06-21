## Summary:
The REST APIs are built using Python Django framework and Mysql database.

It contains the below mentioned endpoints:
- a GET '/math'
- a GET '/func-logs'

The `math` service is a scalable service that can handles n number of mathematical functions. It calculates the results of the mathematical algorithms and save the computation time in the database. For now, it includes only Fibonacci, Ackermann and Factorial algorithms. 

The `func-logs` service displays the summary of the function logs. It uses simple page number based style that helps you manage the paginated data using page numbers in the request query parameters. It is also capable of filtering the data based on some filters.


## Project Structure (App Based):
```bash
KLARNA-TASK/
├── README.md
├── hours.txt
├── .gitignore
└── klarnatask
    ├── Makefile
    ├── apps
    │   ├── __init__.py
    │   ├── api
    │   │   ├── __init__.py
    │   │   ├── apps.py
    │   │   ├── exceptions.py
    │   │   ├── filters.py
    │   │   ├── migrations
    │   │   │   ├── 0001_initial.py
    │   │   │   └── __init__.py
    │   │   ├── models.py
    │   │   ├── serializers.py
    │   │   ├── tests
    │   │   │   ├── __init__.py
    │   │   │   └── test_views.py
    │   │   ├── urls.py
    │   │   ├── utils.py
    │   │   └── views.py
    │   ├── pagination.py
    │   └── utils.py
    ├── conf
    │   └── init.sql
    ├── klarnatask
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── manage.py
    └── requirements.txt
```

### Python Libraries/Frameworks used:
-  **django** - This is a Python-based open-source web framework that follows the model-template-view
architectural pattern.
-  **djangorestframework** - This is a powerful and flexible toolkit built on top of the Django web framework
for building REST APIs.
-  **django-filter** - This is a reusable Django application for allowing users to filter querysets
dynamically from URL parameters.
-  **mysqlclient** - MySQL database connector for Python.
-  **drf-yasg** - This is a Swagger generation tool provided by Django Rest Framework that allow you
to build API documentation.
-  **ddt** - Data-driven testing (DDT) is a parameterized testing that allow you to multiply one test case
by running it with different test data, and make it appear as multiple test cases.
-  **black** - This is Python code formatter that formats code adhering to PEP8 standards.

### Prerequisite
- Make sure you have Python and Mysql installed in your system :)

**Note:** Python 3.6.0 is used for the task.

### How to start application (using Virtual Environment)
Please follow the below steps to start the application:

- Navigate to the project directory: ```cd Klarna-Task```
- Create the virtual environment: ```python3 -m venv env```
- Activate the virtual environment: ```source env/bin/activate```
- Setup mysql database (mac OS):
```
mysql -u root -p (login into mysql server)
password is root
create databases and database user
mysql> source /Users/rabia/Downloads/Klarna-Task/klarnatask/conf/init.sql (absolute path to init.sql file)
```
- Go into the directory:  ```cd klarnatask```
- Install project requirements:  ```make install-requirements```
- Create database tables:  ```make migrate```
- Run the application by the following command:  ```make start-server```
- Show database migrations (if you want to see):  ```make showmigrations```

### How to run application unittests
- Run the command to run the all unittests of the application: ```make tests```

**Note:** The tests command uses the --keepdb option. It preserves the test database between test runs. It skips the create and destroy actions which can greatly decrease the time to run tests.
  
### Different ways to test the API
- How to test using Swagger UI:
	- Hit the url in the browser:
		```
		localhost:8080/api-docs/
		```

- How to test using CURL:
	- Math API
		```
		curl -X GET "http://localhost:8080/api/math/?function=fibonacci&n=5" -H  "accept: application/json"
		```
	- Function Logs API 
		```
		curl -X GET "http://localhost:8080/api/func-logs/?function=factorial" -H  "accept: application/json"
		```

#### Mysql other commands that might be helpful
```
mysql -V (check version)
mysql.server status (check the mysql status)
mysql.server start (run the mysql server)
mysql.server stop (stop the mysql server)
mysql> show databases;
mysql> select Host, User from mysql.user;
mysql> use klarnadb;
mysql> show tables;
```
#### Things that are not included in the task due to time constraints and make the task easy to review from reviewer's perspective:
- Didn’t include Docker to setup the application because it requires more time to configure things.
- API authentication is not added. The API endpoints are public.
- Database credentials are directly added in the settings.py file. It should be confidential from a security perspective.
- Using DEBUG=TRUE for debugging purpose. It shows the whole traceback of the exception. For development purpose it's fine but on production, its value should be FALSE.
- Python logs are being displayed on the console instead of file for the sake of simplicity.
- There is no maximum limit for the input values in all the functions. You may see the inconsistent behavior for the larger inputs.
- Caching is not added for now. It's a best option to cache the calculations of functions for the certain amount of time to save the computation cost and increase the api response time. For example, Ackermann function recurrsive calls can be reduced with caching.

#### A brief description to setup the project on AWS
The end goal is to connect the Django Web Server Gateway Interface (WSGI) to Apache/Ngnix server to execute python code in Django application, in a production environment using AWS as a cloud service.

Steps:
- CLI for AWS Elastic Beanstalk
- Configure EB
    - Initialize the App
    - Create an Environment
- Customizing the Deployment Process
    - Installing packages
    - Configuring our Python environment
- Configuring a Database
    - Database setup
    - Handling database migrations
- Configure Apache/Ngnix to point to our django application

**Note**: Elastic Beanstalk is a service that streamlines the setup, deployment, and maintenance of the app on Amazon AWS. It’s a managed service, coupling the server (EC2), database (RDS), and your static files (S3). It allows us to quickly deploy and manage our application, which automatically scales as our site grows.
