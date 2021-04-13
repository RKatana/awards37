serve:
	python3 manage.py runserver

migration:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

shell:
	python manage.py shell

test:
	coverage run manage.py test && coverage html