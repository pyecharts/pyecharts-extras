# coding=utf-8
from __future__ import unicode_literals

import codecs
import os

from pyecharts import options as opts

from pyecharts_extras import ChoroplethMap


def test_choropleth_map():
    # show label
    value = ["A", "B", "C", "THIS_KEY_IS_NOT_IN_HTML", "A"]
    attr = ["福建", "山东", "北京", "上海", "西藏"]
    legends = [
        {"tag": "A", "label": "test a", "color": "blue"},
        {"tag": "B", "label": "test b", "color": "yellow"},
        {"tag": "C", "label": "test c", "color": "green"},
        {"tag": "THIS_KEY_IS_NOT_IN_HTML", "label": "test d", "color": "red"},
    ]
    map = ChoroplethMap(
        init_opts=opts.InitOpts(width="1200px", height="600px")
    )
    map.set_global_opts(
        title_opts=opts.TitleOpts(title="Choropleth map - 等值区域图示例")
    )
    map.add(
        "",
        data_pair=zip(attr, value),
        choropleth_legend=legends,
        maptype="china",
        is_map_symbol_show=False,
        label_opts=opts.LabelOpts(is_show=False),
    )
    map.render()
    content = get_default_rendering_file_content()
    assert "piecewise" in content
    assert "test a" in content
    assert "2.1" in content
    assert "THIS_KEY_IS_NOT_IN_HTML" not in content
    os.unlink("render.html")


def get_default_rendering_file_content(file_name="render.html"):
    """
    Simply returns the content render.html
    """
    with codecs.open(file_name, "r", "utf-8") as f:
        return f.read()
