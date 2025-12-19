import pandas as pd

# Step 1: Load the CSV data into a pandas DataFrame
# Assuming 'rgb_data.csv' is already uploaded to your Colab environment
data = pd.read_csv('rgb_data.csv')

# Display the first few rows to quickly check the data
print("First 5 rows of the data:")
display(data.head())

# Step 2: Calculate the average value for each color (Red, Green, Blue)
avg_red = data["Red"].mean()
avg_green = data["Green"].mean()
avg_blue = data["Blue"].mean()

print("\nAverage RGB values:")
print(f"Red: {avg_red:.1f}")
print(f"Green: {avg_green:.1f}")
print(f"Blue: {avg_blue:.1f}")

# Step 3: Determine the dominant color by comparing the average values
colors = {
    "Red": avg_red,
    "Green": avg_green,
    "Blue": avg_blue
}

# The 'max' function with 'key=colors.get' finds the key (color name)
# corresponding to the highest value (average color intensity)
dominant_color = max(colors, key=colors.get)

print(f"\nDominant color: {dominant_color}")
