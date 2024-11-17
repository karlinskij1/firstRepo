import requests
response = requests.get("https://httpbin.org/post")
print(response.content)
# print(type(response.content))
#
# print(response.text)

response2 = requests.post("https://httpbin.org/post",
                          data="Test data",
                          headers={"h1": "Test Title"}
                          )
print(response2.text)