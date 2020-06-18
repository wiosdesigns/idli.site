import requests
url = 'https://docs.google.com/document/d/e/2PACX-1vRGa8lluXFb23iFjT6XclRqXarxAIVCdvjg25xaWgTwV0PU8IwWZJUv01yTIVFnmkn1lak7N2obDnEr/pub'

html1 = '''
<!doctype html>
<html lang="en">
<head>
  <title>idli.site</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    *{
      box-sizing: border-box;
    }
    body{
      text-align: center;
      padding:0;
      margin:0;
    }
    #contents{
      padding: 40px 1rem;
      display: inline-block;
      max-width: 720px;
      text-align: left;
      margin:0;
    }
  </style>
</head>
<body>
<div id="contents">
'''

html2 = '''
</body>
</html>
'''


r = requests.get(url)
content = r.text.split('<div id="contents">')[1]
content = content.split('<div id="footer">')[0] + content.split('<div id="footer">')[1].split("</div>")[1].split("</body>")[0]
with open('index.html','w') as f:
  f.write(html1+content+html2)
  f.close()
