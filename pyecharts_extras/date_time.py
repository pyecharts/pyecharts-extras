from datetime import timedelta

import pyecharts.options as opts
from pyecharts import types
from pyecharts.charts.chart import RectChart
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ChartType
from pyecharts.options.series_options import (
    LabelOpts,
    MinorSplitLineOpts,
    MinorTickOpts,
    Numeric,
    Optional,
    SplitAreaOpts,
    SplitLineOpts,
    TextStyleOpts,
    Union,
)

ONE_HOUR = 3600
ONE_DAY = 24 * ONE_HOUR
TIME_AXIS_LABEL_FORMATTER = """
function (value){
    return new Date(value * 1000).toISOString().substr(11, 8);
}
"""
DEFAULT_TIME_AXIS_LABEL = opts.LabelOpts(
    formatter=JsCode(TIME_AXIS_LABEL_FORMATTER)
)
DEFAULT_TIME_AXIS_TICK = opts.AxisTickOpts(is_show=True)
DEFAULT_TIME_AXIS_SPLIT_LINE = opts.SplitLineOpts(is_show=True)


class TimeAxisOpts(opts.AxisOpts):
    def __init__(
        self,
        type_: Optional[str] = "value",
        name: Optional[str] = None,
        is_show: bool = True,
        is_scale: bool = False,
        is_inverse: bool = False,
        name_location: str = "end",
        name_gap: Numeric = 15,
        name_rotate: Optional[Numeric] = None,
        interval: Optional[Numeric] = ONE_HOUR,
        grid_index: Numeric = 0,
        position: Optional[str] = None,
        offset: Numeric = 0,
        split_number: Numeric = 5,
        boundary_gap: Union[str, bool, None] = None,
        min_: Union[Numeric, str, None] = 0,
        max_: Union[Numeric, str, None] = ONE_DAY,
        min_interval: Numeric = 0,
        max_interval: Optional[Numeric] = None,
        axisline_opts: Union[opts.AxisLineOpts, dict, None] = None,
        axistick_opts: Union[
            opts.AxisTickOpts, dict, None
        ] = DEFAULT_TIME_AXIS_TICK,
        axislabel_opts: Union[LabelOpts, dict, None] = DEFAULT_TIME_AXIS_LABEL,
        axispointer_opts: Union[opts.AxisPointerOpts, dict, None] = None,
        name_textstyle_opts: Union[TextStyleOpts, dict, None] = None,
        splitarea_opts: Union[SplitAreaOpts, dict, None] = None,
        splitline_opts: Union[
            SplitLineOpts, dict
        ] = DEFAULT_TIME_AXIS_SPLIT_LINE,
        minor_tick_opts: Union[MinorTickOpts, dict, None] = None,
        minor_split_line_opts: Union[MinorSplitLineOpts, dict, None] = None,
    ):
        super().__init__(
            type_=type_,
            name=name,
            is_show=is_show,
            is_scale=is_scale,
            name_location=name_location,
            name_gap=name_gap,
            name_rotate=name_rotate,
            interval=interval,
            name_textstyle_opts=name_textstyle_opts,
            grid_index=grid_index,
            axisline_opts=axisline_opts,
            axistick_opts=axistick_opts,
            axislabel_opts=axislabel_opts,
            axispointer_opts=axispointer_opts,
            is_inverse=is_inverse,
            position=position,
            offset=offset,
            split_number=split_number,
            boundary_gap=boundary_gap,
            min_=min_,
            max_=max_,
            min_interval=min_interval,
            max_interval=max_interval,
            splitline_opts=splitline_opts,
            splitarea_opts=splitarea_opts,
            minor_tick_opts=minor_tick_opts,
            minor_split_line_opts=minor_split_line_opts,
        )


class DateAxisOpts(opts.AxisOpts):
    def __init__(
        self,
        type_: Optional[str] = None,
        name: Optional[str] = None,
        is_show: bool = True,
        is_scale: bool = False,
        is_inverse: bool = False,
        name_location: str = "end",
        name_gap: Numeric = 15,
        name_rotate: Optional[Numeric] = None,
        interval: Optional[Numeric] = None,
        grid_index: Numeric = 0,
        position: Optional[str] = None,
        offset: Numeric = 0,
        split_number: Numeric = 5,
        boundary_gap: Union[str, bool, None] = None,
        min_: Union[Numeric, str, None] = None,
        max_: Union[Numeric, str, None] = None,
        min_interval: Numeric = 0,
        max_interval: Optional[Numeric] = None,
        axisline_opts: Union[opts.AxisLineOpts, dict, None] = None,
        axistick_opts: Union[
            opts.AxisTickOpts, dict, None
        ] = opts.AxisTickOpts(is_show=True),
        axislabel_opts: Union[LabelOpts, dict, None] = None,
        axispointer_opts: Union[opts.AxisPointerOpts, dict, None] = None,
        name_textstyle_opts: Union[TextStyleOpts, dict, None] = None,
        splitarea_opts: Union[SplitAreaOpts, dict, None] = None,
        splitline_opts: Union[SplitLineOpts, dict] = SplitLineOpts(),
        minor_tick_opts: Union[MinorTickOpts, dict, None] = None,
        minor_split_line_opts: Union[
            MinorSplitLineOpts, dict, None
        ] = SplitLineOpts(is_show=True),
        axis_data=None,
    ):
        # date_min = time.mktime(min_.timetuple())
        # date_max = time.mktime(max_.timetuple())
        date_min = min_
        date_max = max_
        super().__init__(
            type_=type_,
            name=name,
            is_show=is_show,
            is_scale=is_scale,
            name_location=name_location,
            name_gap=name_gap,
            name_rotate=name_rotate,
            interval=interval,
            name_textstyle_opts=name_textstyle_opts,
            grid_index=grid_index,
            axisline_opts=axisline_opts,
            axistick_opts=axistick_opts,
            axislabel_opts=axislabel_opts,
            axispointer_opts=axispointer_opts,
            is_inverse=is_inverse,
            position=position,
            offset=offset,
            split_number=split_number,
            boundary_gap=boundary_gap,
            min_=date_min,
            max_=date_max,
            min_interval=min_interval,
            max_interval=max_interval,
            splitline_opts=splitline_opts,
            splitarea_opts=splitarea_opts,
            minor_tick_opts=minor_tick_opts,
            minor_split_line_opts=minor_split_line_opts,
        )
        self.opts["data"] = axis_data


class TimeYAxisDateXAxis(RectChart):
    def __init__(self, init_opts: types.Init = opts.InitOpts()):
        super().__init__(init_opts=init_opts)

    def add_data(
        self,
        series_name: str,
        y_axis: list,
        *,
        is_selected: bool = True,
        xaxis_index: types.Optional[types.Numeric] = None,
        yaxis_index: types.Optional[types.Numeric] = None,
        color: types.Optional[str] = None,
        symbol: types.Optional[str] = None,
        symbol_size: types.Union[types.Numeric, types.Sequence] = 10,
        symbol_rotate: types.Optional[types.Numeric] = None,
        label_opts: types.Label = opts.LabelOpts(is_show=False),
        markpoint_opts: types.MarkPoint = None,
        markline_opts: types.MarkLine = None,
        markarea_opts: types.MarkArea = None,
        tooltip_opts: types.Tooltip = None,
        itemstyle_opts: types.ItemStyle = None,
        encode: types.Union[types.JSFunc, dict, None] = None,
    ):
        self._append_color(color)
        self._append_legend(series_name, is_selected)
        pair = [[d.date(), d.time()] for d in y_axis]
        data = [
            (
                str(t[0]),
                timedelta(
                    hours=t[1].hour, minutes=t[1].minute, seconds=t[1].second
                ).total_seconds(),
            )
            for t in pair
        ]

        self.options.get("series").append(
            {
                "type": ChartType.SCATTER,
                "name": series_name,
                "xAxisIndex": xaxis_index,
                "yAxisIndex": yaxis_index,
                "symbol": symbol,
                "symbolSize": symbol_size,
                "symbolRotate": symbol_rotate,
                "data": data,
                "label": label_opts,
                "markPoint": markpoint_opts,
                "markLine": markline_opts,
                "markArea": markarea_opts,
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
                "encode": encode,
            }
        )
        return self
