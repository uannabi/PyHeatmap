from autoviz.AutoViz_Class import AutoViz_Class

AV = AutoViz_Class()
filename = "sample.csv"
sep = ","
dft = AV.AutoViz(
    filename,
    sep=",",
    depVar="",
    dfte=None,
    header=0,
    verbose=0,
    lowess=False,
    chart_format="svg",
    max_rows_analyzed=150,
    max_cols_analyzed=30,
)