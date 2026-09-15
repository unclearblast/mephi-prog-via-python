"""Анализ каталога фильмов стримингового сервиса.

Сквозной мини-проект: от переменных и чисел до множеств,
словарей, итераторов и генераторов.
"""

import math

# ---------------------------------------------------------------------------
# Исходные данные
# ---------------------------------------------------------------------------
movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155,
     "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

# --- END STAGE 1 ---

# ---------------------------------------------------------------------------
# Этап 1. Переменные, числа, math
# ---------------------------------------------------------------------------
def average_rating(movies):
    """Средняя оценка по каталогу, округлённая до одного знака."""
    return round(sum(m["rating"] for m in movies) / len(movies), 1)


def catalog_age_stats(movies, current_year=2026):
    """Кортеж (самый старый, самый новый, средний возраст)."""
    ages = [current_year - m["year"] for m in movies]
    return (max(ages), min(ages), math.ceil(sum(ages) / len(ages)))


def duration_in_hours(minutes):
    """Переводит минуты в формат '2ч 35м'."""
    return f"{minutes // 60}ч {minutes % 60}м"

# --- END STAGE 2 ---

# ---------------------------------------------------------------------------
# Этап 2. Условия и match
# ---------------------------------------------------------------------------
def rating_tier(rating):
    """Категория фильма по рейтингу (if/elif + тернарный оператор)."""
    if rating >= 9:
        tier = "шедевр"
    elif rating >= 7:
        tier = "хорошо"
    elif rating >= 5:
        tier = "средне"
    else:
        tier = "слабо"
    return tier if rating >= 0 else "слабо"


def decade_label(year):
    """Метка десятилетия через match с guard-условиями."""
    match year:
        case y if y > 2020:
            return "новые"
        case y if y >= 2015:
            return "недавние"
        case _:
            return "старые"

# --- END STAGE 3 ---

# ---------------------------------------------------------------------------
# Этап 3. Циклы
# ---------------------------------------------------------------------------
def print_non_comedy(movies):
    """Выводит названия фильмов, НЕ относящихся к жанру 'comedy'."""
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])


def find_first_high_rated(movies):
    """Ищет первый фильм с рейтингом > 9.0 (while + break + else)."""
    index = 0
    while index < len(movies):
        if movies[index]["rating"] > 9.0:
            print(f"Первый шедевр: {movies[index]['title']} "
                  f"({movies[index]['rating']})")
            break
        index += 1
    else:
        print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    """Считает фильмы длиннее threshold минут (for + накопление)."""
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count

# --- END STAGE 4 ---

# ---------------------------------------------------------------------------
# Этап 4. Строки
# ---------------------------------------------------------------------------
def normalize_title(title):
    """Ручной Title Case: без str.title(), через срезы."""
    return " ".join(w[0].upper() + w[1:] for w in title.split())


def make_slug(title):
    """Слаг вида the-quiet-algorithm."""
    return normalize_title(title).lower().replace(" ", "-")


def format_report_line(movie):
    """Единая строка описания фильма."""
    return (
        f'"{normalize_title(movie["title"])}" ({movie["year"]}) — '
        f'{movie["rating"]}/10, {duration_in_hours(movie["duration_min"])}, '
        f'жанры: {", ".join(sorted(movie["genres"]))}'
    )

# --- END STAGE 5 ---

# ---------------------------------------------------------------------------
# Этап 5. Списки
# ---------------------------------------------------------------------------
def titles_sorted_by_rating(movies):
    """Список названий, отсортированных по убыванию рейтинга."""
    return [m["title"] for m in
            sorted(movies, key=lambda x: x["rating"], reverse=True)]


def top_n_by_rating(movies, n=3):
    """Топ-n фильмов как список кортежей (title, rating)."""
    return [(m["title"], m["rating"]) for m in
            sorted(movies, key=lambda x: x["rating"], reverse=True)[:n]]

# --- END STAGE 6 ---
