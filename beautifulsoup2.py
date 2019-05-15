# _*_ coding=utf-8 _*_


from bs4 import BeautifulSoup

html = """
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>The Beautiful Suop</title>
</head>
<body>
<p class="story" >once upon a time there were three title sisters;and their name were

<a href="http://example.com/elsie" class="sister" id="link1">
    <span>Elise</span>
</a>
hello
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.
</p>
"""
soup = BeautifulSoup(html, 'lxml')
# 子节点
# print(soup.p.contents)
# print(soup.p.children)
# for i, child in enumerate(soup.p.children):
#     print(i, child)
# 孙子节点
# print(soup.p.descendants)
# for i, child in enumerate(soup.p.descendants):
#     print(i, child)
# 父节点
# print(soup.a.parent)
# 祖先节点
# print(type(soup.a.parents))
# print(list(enumerate(soup.a.parents)))

# 兄弟节点
print("Next Sibling:", soup.a.next_sibling)
print("Prev Sibling:", soup.a.previous_sibling)
print("Next Siblings:", list(soup.a.next_siblings))
print("Prev Siblings:", list(soup.a.previous_siblings))
