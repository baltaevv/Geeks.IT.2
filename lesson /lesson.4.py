class User:
    user_count = 0
    default_password = "123456789"

    def __init__(self, name, phone_number):
        self.name = name
        self.phone = phone_number
        self.role = "user"
        self.password = User.default_password
        User.user_count += 1

    @classmethod
    def create_admin(cls, name, phone_number):
        new_admin = cls(name, phone_number)
        new_admin.role = "admin"
        return new_admin

    @classmethod
    def get_create_user(cls):
        return cls.user_count

    @staticmethod
    def validate_password(password):
        if len(password) < 8:
            return False
        else:
            return True

        # return len(password) >= 8

    def check_password(self, new_password):
        if self.validate_password(new_password):
            self.password = new_password
        else:
            raise ValueError(f"Password too short for {self.name}")

print("Количество user:", User.user_count)
user_1 = User("Timur", "996506706710")
print("Количество user:", User.user_count)
print(User.default_password)
admin_1 = User.create_admin("Artur", "996506506506")
print("User 2 role", admin_1.role)
print("Количество user:", User.user_coun())
admin_1.check_password("123456789")
