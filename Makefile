PROJECT_NAME := mlflow-demo

.PHONY: install-kernel

install-kernel:
	poetry run python -m ipykernel install --user --name $(PROJECT_NAME) --display-name "Python ($(PROJECT_NAME))"
