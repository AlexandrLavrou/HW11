
class Candidates:

    def __init__(self, ident, name, picture, position, skills):
        self.ident = ident
        self.name = name
        self.picture = picture
        self.position = position
        self.skills = skills

    def __repr__(self):
        return f"{self.name}\n{self.position}\n{self.skills}\n\n"

