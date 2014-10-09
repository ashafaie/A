
init: main.py
	clear
	python main.py db init

run: main.py
	clear
	python main.py db upgrade
	python main.py runserver -h 0.0.0.0

clean:
	rm -f *.pyc
	clear

cleanall:
	rm -f *.pyc
	rm -f -r data.sqlite migrations
	clear

