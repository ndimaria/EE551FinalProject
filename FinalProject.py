from lxml import html
import requests

page = requests.get('https://markets.businessinsider.com/stocks')
tree = html.fromstring(page.content)

name = tree.xpath('//*[@id="marketsnow_section_module_container"]/div[2]/div[1]/div[1]/div/div[1]/a/text()')
price = tree.xpath('/html/body/div[2]/div[6]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div/div[2]/div/span/text()')
print("The price of {0} is {1}".format(name[0],price[0]))
