class Playlist:
    #магические методы, dunder - doule underscore
    def __init__(self, name, song=None):
        self.name = name
        self.song = song

    def __str__(self):
        return f"<Playlist object, name: {self.name}>"

    def __len__(self):
        return len(self.song)

    def __contains__(self, item):
        print("items in contains", item)
        return item in self.song

    def __bool__(self):
        return bool(self.song) > 0

pop = Playlist("pop playlist", song=["shape of my heart", ])
print(pop)
print(len(pop))
print("billy Jines" in pop)
print("Shape of my eart"in pop)
if pop:
    print("Playlist is not empty")
else:
    print("Playlist is empty")