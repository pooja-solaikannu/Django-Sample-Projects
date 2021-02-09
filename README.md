# Django-Sample-Projects


Curation of sample django projects.

Django is a server side web development framework driven by python. Enables quick and easy development. Fast growing.


Installation Steps

1. create a virtual environment 

	$virtualenv -p <python_path> <environment_name>

2. activate virtual environment
	
	$source <environment_name>/bin/activate

3. django package installation inside virtual environment
	
	$python -m pip install Django

4. check whether django is installed correctly

	$python -m django --version


Any Project Usage Steps

1. Navigate into masterfolder directory

	$cd masterfolder

2. Perform Migration for database initilization

	$python manage.py makemigrations
	$python manage.py migrate

2. create superuser

	$python manage.py createsuperuser

3. For Execution, use the following command
	
	$python manage.py runserver




	
	


