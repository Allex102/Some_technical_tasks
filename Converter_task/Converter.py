import urllib.request
import xml.dom.minidom as minidom

url = 'http://www.cbr.ru/scripts/XML_daily.asp'


def get_data(url):
    try:
        web_file = urllib.request.urlopen(url)
        return web_file.read()
    except:
        pass


def get_currencies_dict(xml_content):
    global value
    dom = minidom.parseString(xml_content)
    dom.normalize()

    elements = dom.getElementsByTagName("Valute")
    currency_dict = {}

    for node in elements:
        for child in node.childNodes:
            if child.nodeType == 1:
                if child.tagName == 'Value':
                    if child.firstChild.nodeType == 3:
                        value = float(child.firstChild.data.replace(',', '.'))
                if child.tagName == 'CharCode':
                    if child.firstChild.nodeType == 3:
                        char_code = child.firstChild.data
        currency_dict[char_code] = value
    return currency_dict


def print_dict(dict):
    for key in dict.items():
        print(round(dict['NOK'] / dict['HUF'], 2))
        break


if __name__ == '__main__':
    currency_dict = get_currencies_dict(get_data(url=url))
    print('Текущий курс норвежской кроны к венгерскому форинту :')
    print_dict(dict=currency_dict)
