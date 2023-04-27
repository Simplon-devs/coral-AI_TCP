class User:
    def __init__(self, id, username, role, email, fragment_id):
        self.id = id
        self.username = username
        self.role = role 
        self.email = email
        self.fragment_id = fragment_id

    def __str__(self):
        print("id:", self.id)
        print("username:", self.username)
        print("role:", self.role)
        print("email:", self.email)
        print("fragment_id:", self.fragment_id)
        return ""
