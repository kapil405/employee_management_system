import uuid

class Employee:
    def __init__(self, name, role):
        self.id = str(uuid.uuid4())[:8] # short unique ID
        self.name = name
        self.role = role
    
    def to_dict(self):
        return{
            'id': self.id,
            'name': self.name,
            'role': self.role
        }

    @classmethod
    def from_dict(cls, data):
        emp = cls(data['name'], data['role'])
        emp.id = data['id'] #preserve the same ID
        return emp
