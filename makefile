
init: main.py
	clear
	python main.py db init

run: main.py
	clear
	python main.py db upgrade
	python main.py runserver

clean:
	rm *.pyc
	clear

