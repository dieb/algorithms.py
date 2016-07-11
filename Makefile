install:
	@pip install -r requirements.txt

check_syntax:
	@pep8 algorithms/

test:
	@py.test -vvv algorithms/
