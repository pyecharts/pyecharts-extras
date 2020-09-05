isort $(find pyecharts_extras -name "*.py"|xargs echo) $(find tests -name "*.py"|xargs echo)
black -l 79 pyecharts_extras
black -l 79 tests
