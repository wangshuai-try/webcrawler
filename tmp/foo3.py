from lxml import etree

html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <!--网页头部信息-->
    <title>网页名</title>
</head>
<body>
    <!--下面是网页正文-->
    <div class="two">id-text</div>
    <div class="one two">class-text</div>
    <div class="one">class-span</div>
    <div class="three">three</div>
</body>
</html>
'''

html =etree.HTML(html)

content1 = html.xpath("//div[position()>2]") #取div位置大于2的 并且类包含three的

for c in content1:
    print(c.text)