from pyecharts.charts import Map
from pyecharts import options as opts
from pyecharts.globals import ThemeType
import random ,os
filename = 'map.html'
provice = ['湖南', '四川', '重庆', '黑龙江', '浙江', '山西', '河北', '安徽', '河南', '山东', '西藏']
data = [(i,random.randint(50,100)) for i in provice]

map_ = (
    Map()
    .add("销售额",data , "china")
    .set_global_opts(
        title_opts= opts.TitleOpts(title="Map-demo"),
        legend_opts=opts.LegendOpts(is_show=False),
        visualmap_opts=opts.VisualMapOpts(max_=200,is_piecewise= True),
    )
    .render(filename)
)
os.system(filename)