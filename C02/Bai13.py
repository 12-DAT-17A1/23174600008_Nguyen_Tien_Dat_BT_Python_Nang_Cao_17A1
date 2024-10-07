import requests
import json



response = requests.get(url='https://jsonplaceholder.typicode.com/comments?postId=1',headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'})
if response.status_code == 200:
    list_data_jsons = response.json()
print('Danh sách các bài post nổi bật:')
print('-'*50)
for dct in list_data_jsons[:3]:
    print(f"PostId: {dct['postId']}")
    print(f"ID: {dct['id']}")
    print(f"Name: {dct['name']}")
    print(f"Email: {dct['email']}")
    print(f"Body: {dct['body']}")
    print('-'*50)