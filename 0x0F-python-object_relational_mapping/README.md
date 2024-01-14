# **0x0F. Python - Object-relational mapping**

+ Python
+ OOP
+ SQL
+ MySQL
+ ORM
+ SQLAlchemy
+ use the module MySQLdb to connect to a MySQL database and execute your SQL queries.
+ In the second part, you will use the module SQLAlchemy  an Object Relational Mapper (ORM).

# **Requirements:**

+ All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
+ Your files will be executed with MySQLdb version 2.0.x
+ Your files will be executed with SQLAlchemy version 1.4.x
+ All your files should end with a new line
+ The first line of all your files should be exactly #!/usr/bin/python3
+ Your code should use the pycodestyle (version 2.8.*)
+ All your files must be executable
+ The length of your files will be tested using wc
+ All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
+ All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
+ All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
+ A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
You are not allowed to use execute with sqlalchemy

# **More Info:**

+ **Install and activate venv**
+ To create a Python Virtual Environment, allowing you to install specific dependencies for this python project, we will install venv:

+ $ sudo apt-get install python3.8-venv
+ $ python3 -m venv venv
+ $ source venv/bin/activate

+ **Install SQLAlchemy module version 1.4.x**

+ $ sudo pip3 install SQLAlchemy
...
+ $ python3
+ >>> import sqlalchemy
+ >>> sqlalchemy.__version__ 
+ '1.4.22'

+ Also, you can have this warning message:

+ /usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be re
+ moved in a future release.")                                                                                                                    
+  cursor.execute(statement, parameters) 
