from PIL import Image

# Load the target image
image = Image.open("./border_paper.jpg").convert("RGBA")

# Define the color you want to lighten and the threshold for similarity
target_color = (26, 26, 26)  # RGB for #a9b5b5
lighten_factor = 100  # Increase brightness by this factor
color_threshold = 10  # Adjust to capture colors close to target color

# Function to check if a color is within the threshold range of the target color
def is_close_to_target(color, target_color, threshold):
    return all(abs(color[i] - target_color[i]) <= threshold for i in range(3))

# Function to lighten a color by a given factor
def lighten_color(color, factor):
    return tuple(min(255, color[i] + factor) for i in range(3)) + (color[3],)  # Maintain alpha

# Access pixel data
pixels = image.load()

# Iterate over pixels to lighten colors close to the target color
for y in range(image.height):
    for x in range(image.width):
        current_color = pixels[x, y]
        
        # Lighten only if within the target color range
        if is_close_to_target(current_color, target_color, color_threshold):
            pixels[x, y] = lighten_color(current_color, lighten_factor)

# Save the final image with the lightened effect
output_path = "./lightened/border_paper.png"
image.save(output_path)

output_path
