from urllib import response
import requests
api_url="https://link.infini.fr/stats"
url1="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers"
response=requests.post(api_url,data={'url':url1})
print(response.json())
# response.status_code
# response.Data["url"]