#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-04 10:33:54
# @Author  : tsinghua (${email})
# @Link    : ${link}
# @Version : $Id$

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-04 10:21:16
# @Author  : tsinghua (${email})
# @Link    : ${link}
# @Version : $Id$

import os
from pyecharts.charts import Line
from pyecharts import options as opts
cate = ["Apple", "Huawei", "Xiaomi", "Vivo", "Oppo", "Meizu"]
data1 = [123, 153, 89, 23, 23, 10]
data2 = [93, 63, 49, 45, 45, 23]
filename = 'pie.html'
bar = (
    Line()
    .add_xaxis(cate)
    .add_yaxis("线上销售",
               data1, markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")])
               )
    .add_yaxis("线下销售", data2,
               is_smooth=True,
               markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(name="自定义标记", coord=[cate[2], data2[2]], value=data2[2])]))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Pie demo")
    )

    .render(filename)

)

os.system(filename)
