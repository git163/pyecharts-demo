import os,random
from pyecharts import options as  opts
from pyecharts.charts import Scatter3D
from pyecharts.faker import Faker

filename = "scatter-3d.html"


data = [(random.randint(0,100),random.randint(0,100),random.randint(0,100)) for i in range(80)]


scatter = (
    Scatter3D()
    .add("",data)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Scatter-3D"),
        visualmap_opts=opts.VisualMapOpts(range_color=Faker.visual_color)
        
    )
    .render(filename)
)
os.system(filename)