from requests_html import HTMLSession
s = HTMLSession()

query = 'youngstown'
url = f'https://www.google.com/search?q=weather+{query}'

r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'})

temp = r.html.find('div.gNCp2e span.wob_t', first=True).text
unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
desc = r.html.find('div.VQF4g', first=True).find('span#wob_dc', first=True).text
[1]
print(query, temp, unit, desc)

('too hot = 90>')
('just right = 65-90')
('too cold = 65<')

print ('too cold')