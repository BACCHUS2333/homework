import numpy as np
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar, Boxplot, Grid, Line
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType
from pyecharts.options import *


def processit(xt):
    xt_ = [int(i)*0.01-1 for i in xt]
    xt_
    return xt_

x1 = [50,73,73,73,73,73,99]
x2 = [60,100,100,100,100,100,120]
x3 = [i+13 for i in x1]
x4 = [2*j-50 for j in x2]
xtnew = []
for xt in [x1,x2,x3,x4]:
    xtnew.append(processit(xt))
print(xtnew[0])
#v1 =[x1,x2]
#v2 =[x3,x4]
c = Boxplot(init_opts=opts.InitOpts(theme=ThemeType.VINTAGE))
c.add_xaxis(xaxis_data=['Asian','Caucasion','Hispanic','Ethiopian'])
c.extend_axis(yaxis=opts.AxisOpts(type_='value',position='right'))
c.add_yaxis("coefficient", c.prepare_data([xtnew[0],xtnew[2],xtnew[1],xtnew[3]]),itemstyle_opts=ItemStyleOpts(color='rgba(100,100,100,1)'),yaxis_index=0)

#c.add_yaxis("B", c.prepare_data(v2))
c.set_global_opts(title_opts=opts.TitleOpts(title="BoxPlot-基本示例"))


c.render("chart.html")

y_data = [73,100,86,150]
d = Bar()
d.add_xaxis(['Asian','Caucasion','Hispanic','Ethiopian'])
d.add_yaxis(series_name="population",y_axis=y_data,itemstyle_opts=ItemStyleOpts(color='rgba(237,125,49,0.6)'),yaxis_index=1)
#d.add_yaxis(series_name="v2",y_axis=y_data[2:])
d.set_series_opts(label_opts=opts.LabelOpts(position="top",formatter=JsCode(
    "function(x){return Number(x.data).toFixed()+' people/per commu';}"
    )))
d.set_global_opts(
        title_opts=opts.TitleOpts(title="Figure 2. Coefficient of different ethnicity groups"))




o = c.overlap(d)
o.render("coefficient fg2.html")


