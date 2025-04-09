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