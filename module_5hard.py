import hashlib
import time


class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = hashlib.sha256(password.encode()).hexdigest()
        self.age = age

    def check_password(self, password: str) -> bool:
        return self.password == hashlib.sha256(password.encode()).hexdigest()

    def __repr__(self):
        return self.nickname  # Возвращаем только никнейм пользователя

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title: str, duration: int, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __repr__(self):
        return f"Video(title='{self.title}', duration={self.duration}, adult_mode={self.adult_mode})"


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname: str, password: str):
        for user in self.users:
            if user.nickname == nickname and user.check_password(password):
                self.current_user = user
                return
        print("Неправильный логин или пароль")

    def register(self, nickname: str, password: str, age: int):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user  # После регистрации сразу авторизуем пользователя

    def log_out(self):
        self.current_user = None

    def add(self, *videos: Video):
        for video in videos:
            if video.title not in [v.title for v in self.videos]:
                self.videos.append(video)

    def get_videos(self, search_word: str):
        search_word_lower = search_word.lower()
        return [video.title for video in self.videos if search_word_lower in video.title.lower()]

    def watch_video(self, title: str):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return

                while video.time_now < video.duration:
                    print(video.time_now + 1, end=' ', flush=True)
                    video.time_now += 1
                    time.sleep(1)
                print("Конец видео")
                video.time_now = 0
                return
        # Удаляем вывод сообщения, если видео не найдено


# Тестирование
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))  # ['Лучший язык программирования 2024 года']
print(ur.get_videos('ПРОГ'))    # ['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?']

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')  # Войдите в аккаунт, чтобы смотреть видео
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')  # Вам нет 18 лет, пожалуйста покиньте страницу
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')  # Воспроизведение видео

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)  # Пользователь vasya_pupkin уже существует
print(ur.current_user)  # urban_pythonist

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')  # Никакого вывода не будет, так как видео не найдено