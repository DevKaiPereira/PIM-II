.PHONY: run run-txt

run:
	python3 -m prex_triagem

run-txt:
	python3 -m prex_triagem > resultado.txt