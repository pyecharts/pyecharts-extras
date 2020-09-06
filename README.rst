================================================================================
pyecharts-extras
================================================================================

.. image:: https://api.travis-ci.org/pyecharts/pyecharts-extras.svg
   :target: http://travis-ci.org/pyecharts/pyecharts-extras

.. image:: https://codecov.io/github/pyecharts/pyecharts-extras/coverage.png
   :target: https://codecov.io/github/pyecharts/pyecharts-extras
.. image:: https://badge.fury.io/py/pyecharts-extras.svg
   :target: https://pypi.org/project/pyecharts-extras

.. image:: https://pepy.tech/badge/pyecharts-extras/month
   :target: https://pepy.tech/project/pyecharts-extras/month

.. image:: https://img.shields.io/github/stars/pyecharts/pyecharts-extras.svg?style=social&maxAge=3600&label=Star
    :target: https://github.com/pyecharts/pyecharts-extras/stargazers

.. image:: https://mybinder.org/badge_logo.svg
 :target: https://mybinder.org/v2/gh/pyecharts/pyecharts-extras/master?filepath=examples



Latest version works with pyecharts 1.3.1+.

Please launch the binder to get an interactive jupyter notebook running.

1. Time Series Event
-----------------------

Usage of TimeYAxisDateXAxis:

.. code-block:: python

   import pyecharts.options as opts
   from pyecharts_extras.date_time import TimeYAxisDateXAxis
   from datetime import datetime
   
   data = [
      datetime(2020,9,1,3,11,11),
      ...
   ]
   
   data2 = [
       datetime(2020,9,1,1,11,11),
       ...
   ]
   
   chart = TimeYAxisDateXAxis(init_opts=opts.InitOpts(height="1000px"))
   chart.add_data('A', data, symbol_size=10)
   chart.add_data('B', data2, symbol_size=20)
   chart.render_notebook()


.. image:: https://user-images.githubusercontent.com/4280312/92336798-73684880-f09c-11ea-9dee-af30a64c65f4.png


2. ChoroplethMap
----------------

.. image:: https://user-images.githubusercontent.com/4280312/61274388-a0281500-a7a3-11e9-9501-27e8a1659bd0.png



Installation
================================================================================


You can install pyecharts-extras via pip:

.. code-block:: bash

    $ pip install pyecharts-extras


or clone it and install it:

.. code-block:: bash

    $ git clone https://github.com/pyecharts/pyecharts-extras.git
    $ cd pyecharts-extras
    $ python setup.py install
