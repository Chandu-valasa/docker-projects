my_list={
    "chandu" : "devops engineer",
    "designation" : "team leader",
    "skills"   : "terraform"    
}

for info in my_list:
    print(info)

    
for info, details in my_list.items():
    print ( f"{info} is {details}")
          