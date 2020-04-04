#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-04 10:21:16
# @Author  : tsinghua (${email})
# @Link    : ${link}
# @Version : $Id$

from pyecharts.charts import Pie
import os
from pyecharts import options as opts


cate = ["Apple", "Huawei", "Xiaomi", "Vivo"]
data1 = [123, 153, 89, 23]
data2 = [93, 63, 49, 45]
filename = 'pie.html'
bar = (
    Pie()
    .add("",
         [list(z) for z in zip(cate, data1)],
         # radius=["30%", "70%"],
         # rosetype="radius",
         )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Pie demo")
    )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{d}%"))
    .render(filename)

)
os.system(filename)
