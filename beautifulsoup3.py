# _*_ coding=utf-8 _*_


from bs4 import BeautifulSoup

html = """
<html lang="en">
<body>
<p class="story" >once upon a time there were three title sisters;and their name were
    <a href="http://example.com/elsie" class="sister" id="link1">
        <span>Elise</span>
    </a>
</p>
"""
soup = BeautifulSoup(html, 'lxml')

print(soup.a.next_sibling.string)
print(list(soup.a.parents)[0])
print(list(soup.a.parents)[0].attrs['class'])

