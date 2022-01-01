Information={
    "name":"Md. Zahidur Rahman",
    "program":"Post Graduate Diploma in Information and Communication Technology",
    "id":"PGD1727",
    "campus":"Bangladesh Agriculture University",
    "department":"Computer Science & Mathmetics",
    "faculty": "Engineering & Technology"
}

print(Information['name'])
print(Information.get("id"))
print(Information.get("roll","Roll is not present"))