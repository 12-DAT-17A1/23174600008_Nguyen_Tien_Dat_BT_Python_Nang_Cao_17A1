import requests
import json



response = requests.get(url='https://jsonplaceholder.typicode.com/posts',headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'})
if response.status_code == 200:
    list_data_json = response.json()
print(f'Tổng số bài post:{len(list_data_json)}')
print('-'*50)
for dct in list_data_json:
    print(f"UserID: {dct['userId']}")
    print(f"ID: {dct['id']}")
    print(f"Title: {dct['title']}")
    print(f"Body: {dct['body']}")
    print('-'*50)