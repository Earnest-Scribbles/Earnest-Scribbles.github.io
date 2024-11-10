from PIL import Image

# Load the target image
image = Image.open("border_paper.jpg").convert("RGBA")

# Define target and replacement colors
target_color = (26, 26, 26)  # Target color to replace
replacement_color = (197, 184, 177, 255)  # Color to replace with
color_threshold = 90  # Adjust to capture colors close to the target color

# Helper function to check if a color is close to the target color within the threshold
def is_within_threshold(color, target, threshold):
    r_diff = abs(color[0] - target[0])
    g_diff = abs(color[1] - target[1])
    b_diff = abs(color[2] - target[2])
    return r_diff <= threshold and g_diff <= threshold and b_diff <= threshold

# Access pixel data
pixels = image.load()

# Iterate over each pixel and replace colors within the threshold range of the target
for y in range(image.height):
    for x in range(image.width):
        current_color = pixels[x, y][:3]  # Exclude alpha for comparison
        
        # Check if the color is within the threshold of the target color
        if is_within_threshold(current_color, target_color, color_threshold):
            # Replace the pixel with the replacement color, keeping the original alpha
            pixels[x, y] = replacement_color

# Save the resulting image
output_path = "lightened/replaced_border_paper.png"
image.save(output_path)

output_path
