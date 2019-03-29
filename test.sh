pip freeze
nosetests --with-coverage --cover-package pyecharts_extras --cover-package tests tests  docs/source pyecharts_extras && flake8 . --exclude=.moban.d,docs --builtins=unicode,xrange,long
