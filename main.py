# main.py
from datacraft import remove_nulls, mean, simple_bar_chart, load_config

config = load_config("config.json")
raw_data = config.get("data", {})

cleaned = remove_nulls(raw_data)
print("Cleaned Data:", cleaned)

numbers = list(cleaned.values())
print("Mean:", mean(numbers))

print("\nVisualization:")
simple_bar_chart(cleaned)