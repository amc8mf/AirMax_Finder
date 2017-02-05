Author = 'Alex Colegrove'

import urllib.request

def get_airmax_picture():
    url = "http://store.nike.com/us/en_us/pw/mens-air-max-shoes/7puZb8dZoi3?sortOrder=finalprice&ipp=84"
    keyword = '"http://images.nike.com/is/image/DotCom/pwp_sheet2?$NIKE_PWPx3$&$img0='
    stream = urllib.request.urlopen(url)
    link_list = []
    for line in stream:
        decoded = str(line.decode("UTF-8"))
        if keyword in decoded:
            keyword_position = decoded.rfind(keyword)
            end_of_link_position = decoded.rfind('>')
            link = decoded[keyword_position:end_of_link_position]
            if link not in link_list:
                link_list.append(link)
    return link_list

def airmax_nike_finder():
    url = "http://store.nike.com/us/en_us/pw/mens-air-max-shoes/7puZb8dZoi3?sortOrder=finalprice&ipp=84"
    keyword = '<span class=\"local nsg-font-family--base\">$'
    stream = urllib.request.urlopen(url)
    price_list = []
    for line in stream:
        decoded = str(line.decode("UTF-8"))
        if keyword in decoded:
            price = []
            money_sign = decoded.find('$')
            for i in range(money_sign + 1,len(decoded)):
                if decoded[i].isdigit() or decoded[i]=='.':
                    price.append(decoded[i])
                else:
                    break
            price_list.append(''.join(price))
    link_list = get_airmax_picture()
    print(link_list)
    for i in range(0, len(price_list)):
        if float(price_list[i]) < 55:
            print("Shoe Image:" + link_list[i] +'\n' + '\n' + "Shoe Price:" + price_list[i] + '\n')


airmax_nike_finder()


