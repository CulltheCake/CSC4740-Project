from pyspark import SparkContext

# Initialize SparkContext
sc = SparkContext("local", "Global Religious Landscape Analysis")

# Load the dataset (replace 'dataset_path' with the actual path to your dataset)
dataset_path = "path_to_your_dataset"
data = sc.textFile(dataset_path)

# Parse the dataset and apply the mapper function
parsed_data = data.map(lambda line: line.split(",")) \
                  .map(lambda row: {"country": row[0], "religion": row[1], "population": int(row[2]), "region": row[3]})
mapped_data = parsed_data.map(mapper)

# Reduce data by country
reduced_data = mapped_data.reduceByKey(reducer)

# Output the result
output = reduced_data.collect()
for country, data in output:
    print(f"Country: {country}")
    for religion, population, region in data:
        print(f"\tReligion: {religion}, Population: {population}, Region: {region}")

# Stop SparkContext
sc.stop()
