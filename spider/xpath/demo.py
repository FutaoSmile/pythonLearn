from lxml import etree

text = """
<div>
    <ul>
         <li class="item-0 li-first" name='item-0-name'><a href="https://ask.hellobi.com/link1.html">first item</a></li>
         <li class="item-1"><a href="https://ask.hellobi.com/link2.html">second item</a></li>
         <li class="item-inactive"><a href="https://ask.hellobi.com/link3.html">third item</a></li>
         <li class="item-1"><a href="https://ask.hellobi.com/link4.html">fourth item</a></li>
         <li class="item-0"><a href="https://ask.hellobi.com/link5.html">fifth item</a>
     </ul>
 </div>
"""
# 将字符串转为html，并会修复
html = etree.HTML(text)
# print(etree.parse(html).xpath('//*'))
result = etree.tostring(html)
# 获取内容
print(etree.fromstring(etree.tostring(html)).xpath("//li/a/text()"))
# 获取属性
print(etree.fromstring(etree.tostring(html)).xpath("//li/a/@href"))
# 属性多值匹配，如：class有多个，但是通过单个class是获取不到的，单个class只能获取到只有单个class的元素
print(etree.fromstring(etree.tostring(html)).xpath("//li[@class='item-0']/a/text()"))
print(etree.fromstring(etree.tostring(html)).xpath("//li[contains(@class,'item-0')]/a/text()"))
# 多属性匹配，需要匹配多个属性
print(
    etree.fromstring(etree.tostring(html)).xpath("//li[contains(@class,'li-first') and @name='item-0-name']/a/text()"))
# print(result)
# print(result.decode('utf-8'))
