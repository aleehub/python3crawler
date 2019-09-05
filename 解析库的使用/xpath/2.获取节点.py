from lxml import etree



html = etree.parse('./index.html', etree.HTMLParser())

# result = etree.tostring(html)
# print(result)

# 所有节点
# eleList1 = html.xpath('//*')
# print(eleList1)

# 所有li节点
eleList2 = html.xpath('//li')
# print(eleList2)

eleList3_ = html.xpath('//a')
# print(eleList3_)


# li节点下的所有直接a节点
eleList3 = html.xpath('//li/a')
# print(eleList3)

# ul节点下的所有子孙a节点
eleList4_ = html.xpath('//ul/a')
print(eleList4_)
# 一般没有直接子节点 []
eleList4 = html.xpath('//ul//a')
print(eleList4)


# 父节点

text = '''
        <div class="user-info">
            <div class="user-avatar J-login">
              <img src="https://p0.meituan.net/movie/7dd82a16316ab32c8359debdb04396ef2897.png">
              <span class="caret"></span>
              <ul class="user-menu">
                <li><a href="javascript:void 0">登录</a></li>
              </ul>
            </div>
        </div>

        <form action="/query" target="_blank" class="search-form" data-actform="search-click">
            <input name="kw" class="search" type="search" maxlength="32" placeholder="找影视剧、影人、影院" autocomplete="off">
            <input class="submit" type="submit" value="">
        </form>

        <div class="app-download">
          <a href="/app" target="_blank">
            <span class="iphone-icon"></span>
            <span class="apptext">APP下载</span>
            <span class="caret"></span>
            <div class="download-icon">
                <p class="down-title">扫码下载APP</p>
                <p class='down-content'>选座更优惠</p>
            </div>
          </a>
        </div>

  </div>
</div>
<div class="header-placeholder"></div>
'''

html = etree.HTML(text)

# 属性匹配
# 选出classs属性值为down-title的p节点的父节点
result1 = html.xpath('//p[@class="down-title"]/..')
# [<Element div at 0x2bd8848>]
print(result1)


# 查出classs属性值为down-title的p节点的父节点属性class的值
result2 = html.xpath('//p[@class="down-title"]/../@class')

print(result2)
