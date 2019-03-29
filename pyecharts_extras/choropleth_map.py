# coding=utf-8
from pyecharts.charts.map import Map


class ChoroplethMap(Map):
    def get_series_options(self, index):
        return self._option["series"][index]

    def add(
        self,
        name,
        attr,
        value,
        choropleth_legend,
        maptype="china",
        is_roam=True,
        is_map_symbol_show=False,
        name_map=None,
        **kwargs
    ):
        """
        it must use piece wise's visual map，otherwise visual_range_color takes
        no effect. visual_range_text default ['Legend'] and
        visual_text_color defaults to ['black']

        :param name:
            series name for tooltip and legend
        :param attr:
            attributes
        :param value:
            values for corresponding attributes above
        :param choropleth_legend:
            custom legend names
        :param maptype:
            custom geo shape names.
        :param is_roam:
            mouse control, default true, scale & move
            set 'scale' if zooming, set 'move' if moving
        :param is_map_symbol_show:
            remove red map symbol
        :param name_map:
            custom choropleth name instead of region name in the map.
        :param kwargs:

        """
        _classes = list(set(value))
        _class_indices = []
        for __item__ in value:
            # exchange text value with unique internal index
            __index__ = _classes.index(__item__)
            _class_indices.append(__index__)

        _piece_specs = []
        _piece_colors = []
        for __label__ in choropleth_legend:
            # associate label and color with the
            # unique internal index
            __index__ = _classes.index(__label__["tag"])
            _piece_specs.append(
                {
                    "min": __index__,
                    "max": __index__ + 0.1,
                    "label": __label__["label"],
                }
            )
            _piece_colors.append(__label__["color"])

        # dictate the arguments for Map.add()
        kwargs["is_piecewise"] = True
        kwargs["is_visualmap"] = True
        kwargs["visual_range_color"] = _piece_colors
        if "visual_range_text" not in kwargs:
            kwargs["visual_range_text"] = ["Legend"]
        if "visual_text_color" not in kwargs:
            kwargs["visual_text_color"] = ["black"]

        Map.add(
            self,
            name,
            attr,
            _class_indices,
            maptype=maptype,
            is_roam=is_roam,
            is_map_symbol_show=is_map_symbol_show,
            name_map=name_map,
            pieces=_piece_specs,
            **kwargs
        )
