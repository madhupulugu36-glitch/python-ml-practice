import pandas as pd

# Sample Data
data = {
    "City": ["Hyderabad", "Chennai", "Bangalore", "Chennai", "Hyderabad"],
    "Education": ["Degree", "Masters", "PhD", "Degree", "Masters"]
}

df = pd.DataFrame(data)

print(df)