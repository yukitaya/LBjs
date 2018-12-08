import urllib.request, urllib.parse
import json

# Get the contents from sansan

url = 'https://api.sansan.com/v2.0/bizCards/search?email=EMAIL'
API_Key = 'API_KEY'

req = urllib.request.Request(url)
req.add_header('X-Sansan-Api-Key', API_Key)
with urllib.request.urlopen(req) as res:
    body = json.loads(res.read().decode('utf-8'))
print(body)


# Get the access token from LBjs
LBjs = 'https://[hostname]/api/users/login' 
lb_params = {
    'email': 'USERID',
    'password': 'PASSWORD'
}
lb_params = urllib.parse.urlencode(lb_params).encode("utf-8")

with urllib.request.urlopen(url=LBjs, data=lb_params) as lb_res:
   lb_access_token = json.loads(lb_res.read().decode("utf-8"))
   lb_id = lb_access_token['id']


#Post the contents from sansan with access token
post_url = 'https://[hostname]/api/messages?' + 'access_token=' + lb_id
post_params = {
    'roomId': '[roomid]]',
    'text': body
}

post_params = urllib.parse.urlencode(post_params).encode("utf-8")
urllib.request.urlopen(url=post_url, data=post_params)
