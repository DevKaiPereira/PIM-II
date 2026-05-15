PYTHON ?= python3

.PHONY: run run-txt

run:
	$(PYTHON) -m prex_triagem

run-txt:
	$(PYTHON) -m prex_triagem > resultado.txt
