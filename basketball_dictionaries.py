class Player:

    def __init__(self, player_data):
        self.name = player_data['name']
        self.age = player_data['age']
        self.position = player_data['position']
        self.team = player_data['team']

    def display(self):
        print(f"{self.name}, Age: {self.age}. Plays {self.position} on the {self.team}.")
        return self

kevin = {
    "name": "Kevin Durant",
    "age": 34,
    "position": "small forward",
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum",
    "age": 24,
    "position": "small forward",
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving",
    "age": 32, "position": "Point Guard",
    "team": "Brooklyn Nets"
}

# Create your Player instances here!
# player_jason = ???


player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

player_kevin.display()
player_jason.display()
player_kyrie.display()

