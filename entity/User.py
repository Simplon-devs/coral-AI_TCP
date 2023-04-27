class User:
    def __init__(self, id, username, role, email):
        self.id = id
        self.username = username
        self.role = role 
        self.email = email

    def __str__(self):
        print("id:", self.id)
        print("username:", self.username)
        print("role:", self.role)
        print("email:", self.email)

        return ""
