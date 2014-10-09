
init: main.py
	clear
	python main.py db init

run: main.py
	clear
	python main.py db upgrade
	python main.py runserver -h 0.0.0.0

clean:
	find . -name "*.pyc" -exec rm -f {} \;
	clear

cleanall:
	find . -name "*.pyc" -exec rm -f {} \;
	rm -f -r data.sqlite migrations
	clear

