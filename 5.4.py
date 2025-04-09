from faker import Faker
import random

fake = Faker()

class Film():
    def __init__(self, title, year, genre, display_count):
        self.title = title
        self.year = year
        self.genre = genre
        self.display_count = display_count
        pass
    
    def __str__(self):
        return f'{self.title} ({self.year})'

    def play(self):
        self.display_count += 1


class Serial(Film):
    def __init__(self, episode, sezon, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.sezon = sezon

    def __str__(self):
        return f'{self.title} S{self.sezon:02}E{self.episode:02}'

films_serials = []    

def generate_fake_movie(count):
    arr = []
    for i in range(count):
        film = Film(
            title=fake.catch_phrase(), 
            year= random.randint(1950, 2025),
            genre= random.choice(['Drama', 'Comedy', 'Action', 'Sci-Fi', "Romance", "Thriller"]),
            display_count= random.randint(0, 10)
            )
        arr.append(film)
    return arr

def generate_fake_serial(count):
    arr = []
    for i in range(count):
        film = Serial(
            title=fake.catch_phrase(), 
            year= random.randint(1950, 2025),
            genre= random.choice(['Drama', 'Comedy', 'Action', 'Sci-Fi', "Romance", "Thriller"]),
            display_count= random.randint(0, 10),
            episode= random.randint(8,12),
            sezon=1
            )
        arr.append(film)
    return arr


films_serials = films_serials + generate_fake_movie(5) + generate_fake_serial(5)

print(films_serials)