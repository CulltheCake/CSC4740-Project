def mapper(row):
    """
    Mapper function to extract relevant data from the input row.
    """
    # Extract necessary fields from the input row
    country = row["country"]
    religion = row["religion"]
    population = row["population"]
    region = row["region"]
    
    # Key-value pair: (country, (religion, population, region))
    return (country, (religion, population, region))
