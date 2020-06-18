import requests

html1 = '''
<!doctype html>
<html>
<head>
  <title>idli.site</title>
  <style>
    body{
      text-align: center;
    }
    #contents{
      padding: 150px 1rem 80px;
      display: inline-block;
      width: 100%;
      max-width: 720px;
      text-align: left;
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


url = 'https://docs.google.com/document/d/e/2PACX-1vRGa8lluXFb23iFjT6XclRqXarxAIVCdvjg25xaWgTwV0PU8IwWZJUv01yTIVFnmkn1lak7N2obDnEr/pub'
r = requests.get(url)
content = r.text.split('<div id="contents">')[1]
content = content.split('<div id="footer">')[0]
with open('index.html','w') as f:
  f.write(html1+content+html2)
  f.close()
