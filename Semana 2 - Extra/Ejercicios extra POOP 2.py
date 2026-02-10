from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self,name):
        self._name=name
    @abstractmethod
    def get_role(self):
        pass
    @abstractmethod
    def has_permission(self,permission):
        pass

class AdminUser(User):
    def get_role(self):
        return "Admin"
    def has_permission(self, permission):
        return True

class RegularUser(User):
    def __init__(self,name):
        super().__init__(name)
        self._permissions=["read"]
    def get_role(self):
        return "Regular user"
    def has_permission(self, permission):
        return permission in self._permissions

user1=AdminUser("Carlos")
user2=RegularUser("Andrea")
print(user1.has_permission("delete"))
print(user2.has_permission("delete"))
print(user2.has_permission("read"))