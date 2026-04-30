class Guest:
    def __init__(self, name, email, diet):
        self.name = name
        self.email = email
        self.diet = diet

    def __str__(self):
      return f"{self.name} - {self.email} - {self.diet}"
    