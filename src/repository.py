from src.data_base import get_db


db = get_db()
collection = db.movies


def add_movie(title, studio, year, rating, is_watched, actors, director, genre):
    """Adds a new movie document to the database."""
    movie = {
        "title": title,
        "studio": studio,
        "year": year,
        "rating": rating,
        "is_watched": is_watched,
        "actors": actors,  # Should be a list of strings
        "director": director,
        "genre": genre,
    }
    return collection.insert_one(movie)


def delete_movie(title):
    """Deletes a movie by its exact title."""
    return collection.delete_one({"title": title})


def update_movie_fields(title, **fields_to_update):
    """
    Updates any provided fields for a movie found by title.
    Example: update_movie_fields("Inception", rating=9.5, is_watched=True)
    """
    # We use $set with the entire dictionary of passed arguments
    # MongoDB will only update the fields present in the dictionary
    return collection.update_one({"title": title}, {"$set": fields_to_update})


def get_movies_by_criteria(
    year_start=None,
    year_end=None,
    min_rating=None,  # Expected: float
    actor=None,  # Expected: string
    director=None,  # Expected: string
    genre=None,  # Expected: string
    is_watched=None,  # Expected: boolean
):
    """
    Finds movies and counts them based on multiple criteria.
    All parameters are optional. If none provided, returns all movies.
    """
    query = {}

    # 1. Year range (using $gte and $lte)
    year_filters = {}

    if year_start:
        year_filters["$gte"] = int(year_start)
    if year_end:
        year_filters["$lte"] = int(year_end)

    # If at least one filter was added, attach it to the query
    if year_filters:
        query["year"] = year_filters

    # 2. Minimum rating
    if min_rating is not None:
        query["rating"] = {"$gte": min_rating}

    # 3. Actor (Mongo searches inside the 'actors' array automatically)
    if actor:
        query["actors"] = actor

    # 4. Director
    if director:
        query["director"] = director

    # 5. Genre
    if genre:
        query["genre"] = genre

    # 6. Status
    if is_watched is not None:
        query["is_watched"] = is_watched

    # Execute search
    cursor = collection.find(query)
    movie_list = list(cursor)

    # Count results (using the same query)
    count = collection.count_documents(query)

    return movie_list, count
