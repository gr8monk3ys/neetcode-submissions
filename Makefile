# Interview practice helpers.
# Run `make help` to see available targets.

.PHONY: help install test test-fast new clean

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'

install: ## Install dev dependencies (pytest)
	pip install -r requirements-dev.txt

test: ## Run the full test suite
	pytest

test-fast: ## Run tests, stop at first failure
	pytest -x

# Scaffold a new LeetCode problem:
#   make new TOPIC=arrays_hashing NAME=two_sum
new: ## Scaffold a new problem (TOPIC=<topic> NAME=<snake_name>)
	@if [ -z "$(TOPIC)" ] || [ -z "$(NAME)" ]; then \
		echo "Usage: make new TOPIC=<topic> NAME=<snake_name>"; \
		echo "Example: make new TOPIC=arrays_hashing NAME=two_sum"; \
		exit 1; \
	fi
	python3 tools/new_problem.py $(TOPIC) $(NAME)

clean: ## Remove Python/test caches
	find . -type d -name '__pycache__' -prune -exec rm -rf {} +
	rm -rf .pytest_cache
