
init: main.py
	clear
	python main.py db init

run: main.py
	clear
	python main.py db upgrade
	python main.py runserver

cleardata:
	rm -r data.sqlite migrations

clean:
	rm *.pyc
	clear

