import codecs
import os
from datetime import datetime

from pyecharts import options as opts

from pyecharts_extras import TimeYAxisDateXAxis


def test_time_vs_date():
    # show label
    data = [
        datetime(2020, 9, 1, 11, 11, 11),
        datetime(2020, 9, 1, 9, 11, 11),
        datetime(2020, 9, 2, 12, 11, 11),
        datetime(2020, 9, 3, 13, 11, 11),
        datetime(2020, 9, 4, 14, 11, 11),
        datetime(2020, 9, 5, 15, 11, 11),
        datetime(2020, 9, 6, 16, 11, 11),
        datetime(2020, 9, 1, 1, 11, 11),
        datetime(2020, 9, 2, 2, 11, 11),
        datetime(2020, 9, 3, 3, 11, 11),
        datetime(2020, 9, 4, 4, 11, 11),
        datetime(2020, 9, 5, 5, 11, 11),
        datetime(2020, 9, 6, 6, 11, 11),
    ]

    data2 = [
        datetime(2020, 8, 1, 19, 11, 11),
        datetime(2020, 8, 2, 13, 19, 11),
        datetime(2020, 8, 3, 13, 19, 11),
        datetime(2020, 8, 4, 13, 19, 11),
        datetime(2020, 8, 5, 13, 19, 11),
        datetime(2020, 9, 6, 21, 19, 11),
        datetime(2020, 9, 3, 13, 25, 11),
        datetime(2020, 9, 4, 14, 19, 11),
        datetime(2020, 9, 5, 17, 19, 11),
        datetime(2020, 9, 6, 23, 19, 11),
    ]
    c = TimeYAxisDateXAxis(init_opts=opts.InitOpts(height="1000px"))
    c.add_data("A", data, symbol_size=10)
    c.add_data("B", data2, symbol_size=10)
    c.render()
    content = get_default_rendering_file_content()
    assert "2020-08-01" in content
    assert "69071.0" in content
    os.unlink("render.html")


def get_default_rendering_file_content(file_name="render.html"):
    """
    Simply returns the content render.html
    """
    with codecs.open(file_name, "r", "utf-8") as f:
        return f.read()
