from lxml import etree

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
          <a href="/app 444" target="_blank">
            <span class="iphone-icon"></span>
            <span class="apptext">APP下载</span>
            <span class="caret"></span>
            <div class="download-icon">
                <p class="down-title test">扫码下载APP</p>
                <p class='down-content'>选座更优惠</p>
            </div>
          </a>
        </div>

  </div>
</div>
<div class="header-placeholder"></div>
'''


html = etree.HTML(text)

result = html.xpath('//p[@class="test"]/text()')
# 选择节点属性含有多个值，当只选择一个属性值时，获取不到
print(result)

result2 = html.xpath('//p[@class="down-title test"]/text()')
print(result2)
# ['扫码下载APP']


# contains(@属性名，属性值)
# 可获取含有多个属性值的节点文本
result3 = html.xpath('//p[contains(@class,"test")]/text()')
print(result3)
# ['扫码下载APP']

# 多属性匹配
result4 = html.xpath('//a[contains(@href,"/app") and @target="_blank"]//span/text()')
print(result4)

#节点轴选择
result5 = html.xpath('//a/attribute::*')

print(result5)
