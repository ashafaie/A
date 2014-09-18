
init: main.py
	clear
	python main.py db init

run: main.py
	clear
	python main.py db upgrade
	python main.py runserver -h 0.0.0.0

clean:
	rm *.pyc
	clear

cleanall:
	rm *.pyc
	rm -r data.sqlite migrations
	clear

