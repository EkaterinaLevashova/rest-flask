import requests

# res = requests.delete("http://127.0.0.1:3000/api/courses/1")
# res = requests.post("http://127.0.0.1:3000/api/courses/3", {"name": "Golang", "videos": 5})
# res = requests.post("http://127.0.0.1:3000/api/courses/4", {"name": "PHP", "videos": 15})
res = requests.put("http://127.0.0.1:3000/api/courses/4", {"name": "PHPHPHPHp", "videos": 100})
print(res.json())

