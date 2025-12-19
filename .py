import pandas as pd

# Load RGB sensor data from memory card
data = pd.read_csv("rgb_data.csv")

# Calculate average RGB values
avg_red = data["Red"].mean()
avg_green = data["Green"].mean()
avg_blue = data["Blue"].mean()

print("Average RGB values:")
print("Red:", avg_red)
print("Green:", avg_green)
print("Blue:", avg_blue)

# Find dominant color
colors = {
    "Red": avg_red,
    "Green": avg_green,
    "Blue": avg_blue
}

dominant_color = max(colors, key=colors.get)

print("\nDominant color:", dominant_color)

