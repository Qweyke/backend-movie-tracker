from src.repository import add_movie, collection


def seed_database():
    # 1. Clear existing data to avoid duplicates during testing
    print("Clearing old data...")
    collection.delete_many({})

    # 2. Define a list of 10 diverse movies
    test_movies = [
        (
            "Inception",
            "Warner Bros",
            2010,
            8.8,
            True,
            ["DiCaprio", "Hardy"],
            "Nolan",
            "Sci-Fi",
        ),
        (
            "Interstellar",
            "Paramount",
            2014,
            8.6,
            True,
            ["McConaughey", "Hathaway"],
            "Nolan",
            "Sci-Fi",
        ),
        (
            "The Dark Knight",
            "Warner Bros",
            2008,
            9.0,
            True,
            ["Bale", "Ledger"],
            "Nolan",
            "Action",
        ),
        (
            "Pulp Fiction",
            "Miramax",
            1994,
            8.9,
            True,
            ["Travolta", "Jackson", "Willis"],
            "Tarantino",
            "Crime",
        ),
        (
            "Django Unchained",
            "Columbia",
            2012,
            8.4,
            False,
            ["Foxx", "Waltz", "DiCaprio"],
            "Tarantino",
            "Western",
        ),
        (
            "The Matrix",
            "Warner Bros",
            1999,
            8.7,
            True,
            ["Reeves", "Fishburne"],
            "Wachowskis",
            "Sci-Fi",
        ),
        (
            "Blade Runner 2049",
            "Warner Bros",
            2017,
            8.0,
            False,
            ["Gosling", "Ford"],
            "Villeneuve",
            "Sci-Fi",
        ),
        (
            "Dune",
            "Warner Bros",
            2021,
            8.1,
            True,
            ["Chalamet", "Ferguson"],
            "Villeneuve",
            "Sci-Fi",
        ),
        (
            "The Grand Budapest Hotel",
            "Fox Searchlight",
            2014,
            8.1,
            True,
            ["Fiennes", "Revolori"],
            "Anderson",
            "Comedy",
        ),
        (
            "Parasite",
            "CJ ENM",
            2019,
            8.6,
            False,
            ["Song Kang-ho", "Lee Sun-kyun"],
            "Bong Joon-ho",
            "Thriller",
        ),
    ]

    # 3. Insert them into the DB
    print(f"Seeding {len(test_movies)} movies into MongoDB...")
    for m in test_movies:
        add_movie(*m)  # Unpack tuple into function arguments

    print("Database successfully seeded!")


if __name__ == "__main__":
    seed_database()
