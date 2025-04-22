.PHONY: help install-pre-commit install-hooks pre-commit-version pre-commit-update pre-commit-run

# Default target, display help information
help:
	@echo "Available make commands:"
	@echo "  make install-pre-commit   - Install pre-commit tool"
	@echo "  make install-hooks        - Install git hooks to the current repository"
	@echo "  make pre-commit-version   - Display pre-commit version"
	@echo "  make pre-commit-update    - Update pre-commit hooks to the latest version"
	@echo "  make pre-commit-run       - Run pre-commit checks on all files"
	@echo "  make lint                 - Run all code checking tools"
	@echo "  make help                 - Display this help information"

# Install pre-commit tool
install-pre-commit:
	pip install pre-commit

# Install git hooks to the current repository
install-hooks:
	pre-commit install

# Display pre-commit version
pre-commit-version:
	pre-commit --version

# Update pre-commit hooks to the latest version
pre-commit-update:
	pre-commit autoupdate

# Run pre-commit checks on all files
pre-commit-run:
	pre-commit run --all-files

# Run all code checking tools
lint: pre-commit-run

# Set default target
.DEFAULT_GOAL := help
