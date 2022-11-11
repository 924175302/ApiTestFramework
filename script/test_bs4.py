from bs4 import BeautifulSoup


html = ""


soup = BeautifulSoup(html, "html.parser")

# 获取title对象
print(soup.title)

# 获取title的标签名称
print(soup.title.name)

# 获取title的值
print(soup.title.string)

# 获取P对象
print(soup.p)

# 获取所有p对象
print(soup.find_all('p'))

# 获取第一个P标签和对应的ID属性的值
print(soup.p['id'])

for s in soup.find_all('a'):
    print("href={} text={}".format(s['href'], s.string))
