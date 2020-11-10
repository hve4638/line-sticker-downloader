import re
import webbrowser
        
def linesticker(number):
    url = r'http://dl.stickershop.line.naver.jp/products/0/0/1/{}/iphone/stickers@2x.zip'
    
    relink = re.compile('https://store.line.me/stickershop/product/(\d*)')
    renum = re.compile(r'(\d*)')

    m = relink.match(number)

    if m is None:
        m = renum.match(number)

        if m is None:
            return False

    webbrowser.open(url.format(m.group(1)))
    return True
        
number = input('link or number >>')

linesticker(number)
