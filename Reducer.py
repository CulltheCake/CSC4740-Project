from operator import add

def reducer(x, y):
    """
    Reducer function to aggregate data by country.
    """
    # Merge data for the same country
    merged_data = x + y
    return merged_data
