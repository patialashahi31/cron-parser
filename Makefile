test:
	pytest -s

coverage-html:
	pytest --cov=cron_parser --cov-report=html

coverage-terminal:
	pytest --cov=cron_parser --cov-report=term

run-sample:
	python main.py '*/15 0 1,15 * 1-5 /usr/bin/find'