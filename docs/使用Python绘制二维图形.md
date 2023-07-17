
一些表达几何图形的Python类，可用于draw函数

| 类       | 构造示例                        | 说明                                          |
|---------|-----------------------------|---------------------------------------------|
| Polygon | Polygon(*vector)            | 用于绘制一个多边形，其顶点(顶角)坐标用一组向量表示                  |
| Points  | Points(*vector)             | 用于绘制多个点，每个点对应一个输入向量                         |
| Arrow   | Arrow(tip) Arrow(tip, tail) | 从原点向tip绘制箭头.如果指定了第二个参数tail,则从tip向tail绘制一个箭头 |
| Segment | Segement(start, end)        | 从start到end绘制一条线段                            |
