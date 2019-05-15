# _*_ coding=utf-8 _*_


from bs4 import BeautifulSoup

html = """
<div class="panel">
    <div class="panel-heading">
        <h4>hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
        
    </div>
</div>
"""
soup = BeautifulSoup(html, 'lxml')
# name查询
# print(soup.find_all(name='ul'))
# print(type(soup.find_all(name='ul')[0]))
#
# for ul in soup.find_all(name='ul'):
#     print(ul.find_all(name='li'))
#     for li in ul.find_all(name='li'):
#         print(li.string)

# attrs查询
# print(soup.find_all(attrs={'id': 'list-1'}))
# print(soup.find_all(attrs={'name': 'elements'}))
# print(soup.find_all(id='list-1'))
# print(soup.find_all(class_='element'))

# text方法
# import re
#
# print(soup.find_all(text=re.compile('F')))

# find()方法
# print(soup.find(name='ul'))
# print(soup.find(class_='list'))

# CSS选择器
# print(soup.select('.panel .panel-heading'))
# print(soup.select('ul li'))
# print(soup.select('#list-2 .element'))
# for ul in soup.select('ul'):
#     print(ul.select('li'))
# 获取属性
# for ul in soup.select('ul'):
#     print(ul['id'])
#     print(ul.attrs['id'])
# 获取文本
for li in soup.select('li'):
    print(li.get_text())
    print(li.string)
