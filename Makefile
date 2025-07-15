# Python variables
VENV = .venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip
ACTIVATE = . $(VENV)/bin/activate

TEX_FILES = $(shell find . -name '*.tex')
DOC_FILES = $(shell find . -name '*.md') $(shell find . -name '*.rst') $(TEX_FILES) _static/css/style.css

.PHONY: docs clean venv view



docs: html

clean:
	@echo "Removing files"
	@rm html/ -r main.aux main.fdb_latexmk main.fls main.log main.out 2>>/dev/null || true


venv: $(VENV)/bin/activate 


view: docs
	@xdg-open html/index.html 2>>/dev/null& disown|| open html/index.html 2>>/dev/null

html: $(VENV)/bin/activate conf.py index.rst $(DOC_FILES)
	$(ACTIVATE) && sphinx-build . html

# Create virtual environment
$(VENV)/bin/activate: requirements.txt
	@echo "Creating a new virtual environment..."
	@python3 -m venv $(VENV)
	@echo "Installing dependencies..."
	@$(PIP) install -r requirements.txt
	@touch $(VENV)/bin/activate
	@echo "Dependencies installed."
