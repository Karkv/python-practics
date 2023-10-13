import qrcode

url = qrcode.create('https://www.example.com')
url.svg('example.svg', scale=8)