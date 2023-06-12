.PHONY: clean

clean:
	rm .coverage || true
	rm .coverage.xml || true
	rm .pdm-python || true
	rm -rf docs/build || true
	rm -rf .mypy_cache || true
	rm -rf .nox || true
	rm -rf .pytest_cache || true
	rm -rf .venv || true
