import json
import requests
import xml.etree.ElementTree as  et 


response = requests.get(
    url='https://www.hindustantimes.com/feeds/rss/topnews/rssfeed.xml',
    headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'})
# if response.status_code == 200:
#     with open(file='./xmls/content.xml',mode='w') as file:
#         data_xml = response.text
#         file.write(data_xml)
# else:
#     print('Gửi yêu cầu không thành công!!!')
data_visualization = '''
    <?xml version="1.0" encoding="UTF-8"?>
    <rss xmlns:atom="http://www.w3.org/2005/Atom" xmlns:media="http://search.yahoo.com/mrss/" version="2.0">
        <channel>
            <atom:link href="https://www.hindustantimes.com/feeds/rss/topnews/rssfeed.xml" rel="self" type="application/rss+xml"/>
            <title>null | Hindustan Times</title>
            <link>https://www.hindustantimes.comnull</link>
            <description/><category>topnews</category>
            <ttl>60</ttl>
            <lastBuildDate>Sun, 06 Oct 2024 16:29:37 +0530</lastBuildDate>
            <copyright>Copyright (C) 2019 HT Media Limited. All Rights Reserved.</copyright>
            <language>en-US</language>
            <docs>https://www.hindustantimes.com</docs>
            <image>
                <title>null | Hindustan Times</title>
                <link>https://www.hindustantimes.comnull</link>
                <url>https://www.hindustantimes.com/images/app-images/ht2020/desktop.png</url>
                </image>
        </channel>
    </rss>
'''
tree = et.parse(source='./xmls/content.xml')
root = tree.getroot()
list_childs_channel = root.find('channel')
print('Channel:')
for tag_child in list_childs_channel:
    if tag_child.tag !='image':
        print('{}: {}'.format(tag_child.tag,tag_child.text))
    else:
        print('image:')
        for child in tag_child:
            print('{:>10}: {}'.format((child.tag),child.text))