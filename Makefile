quality_checks:
	isort .
	black .
	pylint --recursive=y .

setup:
	pip install -r requirements.txt .

