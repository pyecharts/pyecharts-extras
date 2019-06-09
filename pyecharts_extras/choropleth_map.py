# coding=utf-8
from pyecharts import options as opts
from pyecharts.commons.types import Union, Optional, Sequence, Numeric
from pyecharts.charts import Map


class ChoroplethMap(Map):

    def add(
        self,
        series_name: str,
        data_pair: Sequence,
        maptype: str = "china",
        *,
        choropleth_legend: Sequence = None,
        **kwds
    ):
        _piece_specs = []
        _piece_colors = []
        _classes = []
        for __index, __label in enumerate(choropleth_legend):
            # associate label and color with the
            # unique internal index
            _classes.append(__label["tag"])
            _piece_specs.append(
                {
                    "min": __index,
                    "max": __index + 0.1,
                    "label": __label["label"],
                }
            )
            _piece_colors.append(__label["color"])

        _old_data_pair = list(data_pair)
        _new_data_pair = []
        for key, value in _old_data_pair:
            # exchange text value with unique internal index
            __index__ = _classes.index(value)
            _new_data_pair.append([key, __index__])

        # dictate the arguments for Map.add()
        custom = opts.VisualMapOpts(
            is_piecewise=True,
            range_text=["Legend"],
            range_color=_piece_colors,
            pieces=_piece_specs
        )
        self.options.update(visualMap=custom)

        super(ChoroplethMap, self).add(
            series_name,
            _new_data_pair,
            maptype,
            **kwds
        )
        return self
