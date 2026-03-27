import src.repository as repo
from src.fill_db import seed_database


def print_movies(movies, count):
    """Helper to display search results."""
    print(f"\n--- Found {count} movies ---")
    for m in movies:
        status = "Watched" if m.get("is_watched") else "Not Watched"
        print(
            f"[{status}] {m['title']} ({m['year']}) | Rating: {m['rating']} | Genre: {m['genre']}"
        )
        print(f"    Director: {m['director']} | Cast: {', '.join(m['actors'])}")
    print("-" * 30)


def main():
    seed_database()
    while True:
        print("\n=== MOVIE TRACKER CLI ===")
        print("1. Add new movie")
        print("2. Delete movie")
        print("3. Update movie details (Universal)")
        print("4. Filter & Count movies (Flexible)")
        print("5. Show all movies")
        print("0. Exit")

        choice = input("Select option: ")

        if choice == "1":
            # Collecting data for a new movie
            title = input("Title: ")
            studio = input("Studio: ")
            year = int(input("Year: "))
            rating = float(input("Rating: "))
            is_watched = input("Already watched? (y/n): ").lower() == "y"
            director = input("Director: ")
            genre = input("Genre: ")
            # Actors input: splitting comma-separated string into a list
            actors_raw = input("Actors (comma separated): ")
            actors = [a.strip() for a in actors_raw.split(",")]

            repo.add_movie(
                title, studio, year, rating, is_watched, actors, director, genre
            )
            print("Successfully added!")

        elif choice == "2":
            title = input("Enter title to delete: ")
            res = repo.delete_movie(title)
            print(f"Deleted {res.deleted_count} documents.")

        elif choice == "3":
            title = input("Enter title to update: ")
            print("What to update? (1: Status, 2: Rating, 3: Genre)")
            upd_choice = input("> ")
            if upd_choice == "1":
                val = input("Watched? (y/n): ").lower() == "y"
                repo.update_movie_fields(title, is_watched=val)
            elif upd_choice == "2":
                val = float(input("New rating: "))
                repo.update_movie_fields(title, rating=val)
            elif upd_choice == "3":
                val = input("New genre: ")
                repo.update_movie_fields(title, genre=val)
            print("Updated!")

        elif choice == "4":
            print("\n--- Filter Menu (Leave blank to skip) ---")

            # Filtering logic handles empty inputs
            y_start = input("Year from: ")
            y_end = input("Year to: ")

            min_r = input("Min rating: ")
            act = input("Actor name: ")
            gen = input("Genre: ")

            status_input = input("Watched? (y/n/skip): ").lower()
            is_w = (
                True if status_input == "y" else False if status_input == "n" else None
            )

            # Calling our universal repo function
            movies, count = repo.get_movies_by_criteria(
                year_start=y_start,
                year_end=y_end,
                min_rating=float(min_r) if min_r else None,
                actor=act if act else None,
                genre=gen if gen else None,
                is_watched=is_w,
            )
            print_movies(movies, count)

        elif choice == "5":
            movies, count = repo.get_movies_by_criteria()
            print_movies(movies, count)

        elif choice == "0":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
