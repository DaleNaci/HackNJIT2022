def check_conflict(day1: str, time1: str, day2: str, time2: str) -> bool:
    """Determines whether two sections have conflicting times.

    It first parses the data provided, so you can provide this function the
    strings taken straight from the database.

    Args:
        day1: Day string of first section.
        time1: Time string of first section.
        day2: Day string of second section.
        time2: Time string of second section.
    
    Returns:
        A boolean that is true if there is no conflict, false otherwise.
    
    Raises:
        TypeError: If given strings are not valid.
        Exception: Day or Time strings are not valid parsable strings.
    """