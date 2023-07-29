# makefile

venv:
	python3 -m venv ../venv

init:
	pip install --upgrade pip
	pip install -r requirements.txt
	rm -f db.sqlite3
	make migrate
	make loaddata

loaddata:
	python manage.py loaddata _fixtures/auth_user.json --settings=app.settings
	python manage.py loaddata _fixtures/maestro_institucion.json --settings=app.settings
	python manage.py loaddata _fixtures/maestro_medicamento.json --settings=app.settings
	python manage.py loaddata _fixtures/maestro_item.json --settings=app.settings
	python manage.py loaddata _fixtures/maestro_equipamiento.json --settings=app.settings
	python manage.py loaddata _fixtures/maestro_quiebre.json --settings=app.settings
	python manage.py loaddata _fixtures/stock_lote.json --settings=app.settings

dumpdata:
	python manage.py dumpdata auth.user --indent 2 > _fixtures/auth_user.json --settings=app.settings
	python manage.py dumpdata maestro.institucion --indent 2 > _fixtures/maestro_institucion.json --settings=app.settings
	python manage.py dumpdata maestro.medicamento --indent 2 > _fixtures/maestro_medicamento.json --settings=app.settings
	python manage.py dumpdata maestro.item --indent 2 > _fixtures/maestro_item.json --settings=app.settings
	python manage.py dumpdata maestro.equipamiento --indent 2 > _fixtures/maestro_equipamiento.json --settings=app.settings
	python manage.py dumpdata maestro.quiebre --indent 2 > _fixtures/maestro_quiebre.json --settings=app.settings
	# python manage.py dumpdata stock.lote --indent 2 > _fixtures/stock_lote.json --settings=app.settings

precommit:
	black --line-length=140 .
	flake8 --ignore E501 .

migrations:
	rm -f stock/migrations/000*.py
	python manage.py makemigrations stock --settings=app.settings
	make precommit

migrate:
	rm -f db.sqlite3
	python manage.py migrate --settings=app.settings
	make loaddata

update:
	pur -r requirements.txt

run:
	python manage.py runserver 0.0.0.0:8000 --settings=app.settings

__test_prepare:
	rm -f stock/migrations/000*.py
	python manage.py makemigrations stock --settings=app.settings

run_tests:
	make __test_prepare
	pytest -vv
