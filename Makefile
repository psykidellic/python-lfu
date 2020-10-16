.PHONY: all test clean_coverage clean pep8 mypy check

all:
	@echo 'test           run the unit tests'
	@echo 'coverage       generate coverage statistics'
	@echo 'pep8           check pep8 compliance'
	@echo 'mypy       	  check typing compliance'
	@echo 'check          make sure you are ready to commit'
	@echo 'clean          cleanup the source tree'

test: clean_coverage
	@echo 'Running all tests...'
	coverage run --source=lfu_cache --module pytest
	coverage report

clean_coverage:
	@rm -f .coverage

clean:
	@rm -f python_lfu/*.pyc

pep8:
	@echo 'Checking pep8 compliance...'
	@pycodestyle --max-line-length 90 lfu_cache/

mypy:
	@echo 'Running mypy...'
	@mypy lfu_cache

check: clean pep8 mypy test
