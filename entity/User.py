class User:
    def __init__(self, id, username, role, email, register_date):
        self.id = id
        self.username = username
        self.role = role
        self.email = email
        self.register_date = register_date

    def __str__(self):
        print("id:", self.id)
        print("username:", self.username)
        print("role:", self.role)
        print("email:", self.email)
        print("register_date:", self.register_date)
        return ""

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'role': self.role,
            'email': self.email,
            'register_date': self.register_date
        }
