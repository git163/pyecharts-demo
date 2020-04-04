from pyecharts.charts import Geo
from pyecharts import options as opts
from pyecharts.globals import ChartType
import random, os
filename = 'geo.html'
province = ['武汉', '十堰', '鄂州', '宜昌', '荆州', '孝感', '黄石', '咸宁', '仙桃']
data = [(i,random.randint(50,150)) for i in province]

geo = (
    Geo()
    .add_schema(maptype="湖北")
    .add("门店数",data,type_=ChartType.HEATMAP)
    .set_series_opts(
        label_opts= opts.LabelOpts(is_show=True)
    )
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(),
        legend_opts= opts.LegendOpts(is_show=True),
        title_opts=opts.TitleOpts(title="湖北热力图")
    )
    .render(filename)
)
os.system(filename)