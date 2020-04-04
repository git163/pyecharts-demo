import os
import sys

from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType

# from pyecharts.render import make_snapshot
# from snapshot_selenium import snapshot
filename = "bar.html"
x = ["衬衫", "羊毛衫", "裤子"]
y1 = [5, 20, 36]
y2 = [10, 25, 8]
bar = (

    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    .add_xaxis(x)
    .add_yaxis("商家A", y1)
    .add_yaxis("商家B", y2)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"),
        toolbox_opts=opts.ToolboxOpts(),
        legend_opts=opts.LegendOpts(is_show=True),
        # visualmap_opts=opts.VisualMapOpts()
    )



    .render(filename)
    # .render_notebook()
)


# bar
# # make_snapshot(snapshot, bar.render(filename), 'bar.png')

os.system(filename)
