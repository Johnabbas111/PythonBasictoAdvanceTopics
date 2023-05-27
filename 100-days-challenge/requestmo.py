import request 
#simple get request 
#response=request.get("https://www.codewithharry.com")
#print(response.text)
#post request  just for trial for some url 
url="https://jsonplaceholder.tyicode.com/posts"
data={
  "title":'harry',
  "body":'bhai'
  "userId":12,
  
}
headers={
  'content-type':'application/json; charset=utf-8',
  
  
}
response=request.post(url,header=headers, json=data)
print(response.text)

