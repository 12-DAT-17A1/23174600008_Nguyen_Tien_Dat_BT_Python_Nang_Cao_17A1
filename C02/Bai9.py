import json


data = {
    "employees": [
      {
        "id": 1,
        "name": "John Doe",
        "position": "Software Engineer",
        "salary": 75000,
        "skills": ["Python", "Java", "SQL"]
      },
      {
        "id": 2,
        "name": "Jane Smith",
        "position": "Data Scientist",
        "salary": 85000,
        "skills": ["Machine Learning", "R", "Data Visualization"]
      }
    ],
    "company": {
      "name": "Tech Solutions",
      "location": "Hanoi, Vietnam",
      "founded": 2010
    }
  }

#Chuyển đổi đối tượng python sang dữ liệu json, sắp xếp  theo từ khóa.
json_sort =  json.dumps(obj=data,sort_keys=True,ensure_ascii=False,indent= 4)
#In dữ liệu json.
print(json_sort) 
#Kiểm tra kiểu dữ liệu.
print(type(json_sort))