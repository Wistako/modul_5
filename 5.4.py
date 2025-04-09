import random
from datetime import datetime
from faker import Faker

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


class VideoData():
    films_serials = []    

    def generate_fake_movie(self, count):
        for i in range(count):
            film = Film(
                title=fake.catch_phrase(), 
                year= random.randint(1950, 2025),
                genre= random.choice(['Drama', 'Comedy', 'Action', 'Sci-Fi', "Romance", "Thriller"]),
                display_count= random.randint(0, 10)
                )
            self.films_serials.append(film)

    def generate_fake_serial(self, count):
        for i in range(count):
            serial = Serial(
                title=fake.catch_phrase(), 
                year= random.randint(1950, 2025),
                genre= random.choice(['Drama', 'Comedy', 'Action', 'Sci-Fi', "Romance", "Thriller"]),
                display_count= random.randint(0, 10),
                episode= random.randint(8,12),
                sezon=1
                )
            self.films_serials.append(serial)



    def get_movies(self):
        result = [item for item in self.films_serials if not isinstance(item, Serial)]
        result = sorted(result, key=lambda film: film.title)
        return result

    def get_serials(self):
        result = [item for item in self.films_serials if isinstance(item, Serial)]
        result = sorted(result, key=lambda serial: serial.title)
        return result

    def search_by_title(self, search_phrase):
        return [item for item in self.films_serials if search_phrase.lower() in item.title.lower()]


    def generate_views(self):
        length = len(self.films_serials)
        index = random.randint(0, length - 1)
        self.films_serials[index].display_count += random.randint(1,100)

    def generate_many_views(self, count = 10):
        for i in range(count):
            self.generate_views()

    def top_titles(self, content_type = None):
        if content_type is None:
            sort = sorted(self.films_serials, key=lambda vid: vid.display_count, reverse=True)
            return sort[:3]
        elif content_type == 'movie':
            filtered = self.get_movies()
            sort = sorted(filtered, key=lambda vid: vid.display_count, reverse=True)
            return sort[:3]
        elif content_type == 'serial':
            filtered = self.get_serials()
            sort = sorted(filtered, key=lambda vid: vid.display_count, reverse=True)
            return sort[:3]
        else:
            print('Nieobsługiwany typ video')
            return []


def main():
    print('Biblioteka filmów')
    base = VideoData()
    base.generate_fake_movie(10)
    base.generate_fake_serial(10)
    base.generate_many_views()
    

    top = base.top_titles()
    today = datetime.now()
    print(f'Najpopularniejsze filmy i seriale dnia {today.strftime("%d.%m.%Y")} ')
    for t in top:
        print(t.display_count, t)





if __name__ == "__main__":
    main()