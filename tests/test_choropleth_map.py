# coding=utf-8
from __future__ import unicode_literals
import os
import codecs

from pyecharts_extras import ChoroplethMap


def test_choropleth_map():
    # show label
    value = ['A', 'B', 'C', 'THIS_KEY_IS_NOT_IN_HTML', 'A']
    attr = ["福建", "山东", "北京", "上海", "西藏"]
    legends = [
        {'tag': 'A', 'label': 'test a', 'color': 'blue'},
        {'tag': 'B', 'label': 'test b', 'color': 'yellow'},
        {'tag': 'C', 'label': 'test c', 'color': 'green'},
        {'tag': 'THIS_KEY_IS_NOT_IN_HTML', 'label': 'test d', 'color': 'red'}
    ]
    map = ChoroplethMap("Choropleth map - 等值区域图示例", width=1200, height=600)
    map.add("", attr, value, legends, maptype='china',
            is_label_show=True)
    map.render()
    content = get_default_rendering_file_content()
    assert 'piecewise' in content
    assert 'test a' in content
    assert '2.1' in content
    assert 'THIS_KEY_IS_NOT_IN_HTML' not in content
    os.unlink('render.html')


def get_default_rendering_file_content(file_name="render.html"):
    """
    Simply returns the content render.html
    """
    with codecs.open(file_name, "r", "utf-8") as f:
        return f.read()
