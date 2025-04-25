import requests
import re
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = input('website URL: ')

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

link_tag = soup.find('link', rel='stylesheet')

if link_tag:
    css_url = urljoin(url, link_tag['href'])
    css_response = requests.get(css_url)

    with open('style.css', 'wb') as f:
        f.write(css_response.content)
else:
    print('CSS file not found.')

with open('style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

color_pattern = r'(#[0-9a-fA-F]{3,6})|rgba?\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*,\s*(\d{1,3})(?:\s*,\s*(\d?\.?\d+))?\s*\)|hsla?\(\s*(\d{1,3})\s*,\s*(\d{1,3})%\s*,\s*(\d{1,3})%(?:\s*,\s*(\d?\.?\d+))?\s*\)'

matches = re.findall(color_pattern, css_content)
formatted_colors = []

for match in matches:
    if match[0]:
        formatted_colors.append(match[0])
    elif match[1] and match[2] and match[3]:
        rgba = f"rgb({match[1]}, {match[2]}, {match[3]})"
        formatted_colors.append(rgba)
    elif match[5] and match[6] and match[7]:
        hsla = f"hsl({match[5]}, {match[6]}%, {match[7]}%)"
        formatted_colors.append(hsla)

print(set(formatted_colors))

# Удаление файла
if os.path.exists('style.css'):
    os.remove('style.css')
else:
    print("CSS file not found.")
