from pyecharts.charts import Funnel
from pyecharts import options as opts

cate = ['访问','注册','加入购物车','提交订单']
data = [200,230,345,212,113]

import os
filename = "funnel.html"
funnel = (
    Funnel()
    .add(
        "用户数",[list(z) for z in zip(cate,data)]
        ,sort_='ascending',
        label_opts= opts.LabelOpts(position="inside")
    )
    .set_global_opts(title_opts= opts.TitleOpts(title="Funnel-demo"))
    .render(filename)
    )

os.system(filename)
