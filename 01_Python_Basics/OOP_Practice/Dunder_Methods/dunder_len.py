class Team:
    def __init__(self, members):
        self.members = members
    def __len__(self):
        return len(self.members)
team = Team(["Madhu", "Ravi", "John"])
print(len(team))