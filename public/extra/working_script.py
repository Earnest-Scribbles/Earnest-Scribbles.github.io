from PIL import Image

# Load the original image and the white paper texture image
yellow_img = Image.open("latest/yellow.jpg").convert("RGBA")
white_img = Image.open("latest/white.jpg").resize(yellow_img.size).convert("RGBA")

# Access pixel data
pixels_yellow = yellow_img.load()
pixels_white = white_img.load()

# Define the original beige base color and a threshold for detecting shadows
original_beige = (255, 235, 202)
shadow_threshold = 30  # Adjust this to widen or narrow the shadow range

# Function to check if a color is within the shadow range of the original beige
def is_within_shadow_range(color, base_color, threshold):
    r_diff = abs(base_color[0] - color[0])
    g_diff = abs(base_color[1] - color[1])
    b_diff = abs(base_color[2] - color[2])
    return r_diff <= threshold and g_diff <= threshold and b_diff <= threshold

# Function to calculate the shadow difference dynamically
def calculate_shadow_adjustment(current_color, base_color):
    diff_r = base_color[0] - current_color[0]
    diff_g = base_color[1] - current_color[1]
    diff_b = base_color[2] - current_color[2]
    return diff_r, diff_g, diff_b

# Function to adjust the paper texture with the calculated shadow difference
def adjust_paper_color(paper_color, diff):
    new_r = max(0, paper_color[0] - diff[0])
    new_g = max(0, paper_color[1] - diff[1])
    new_b = max(0, paper_color[2] - diff[2])
    return new_r, new_g, new_b

# Iterate over pixels to apply dynamic shadow adjustments only in the shadow range
for y in range(yellow_img.height):
    for x in range(yellow_img.width):
        r, g, b, a = pixels_yellow[x, y]
        
        # Check if the current color is within the shadow range
        if is_within_shadow_range((r, g, b), original_beige, shadow_threshold):
            # Calculate shadow difference from the original beige
            shadow_diff = calculate_shadow_adjustment((r, g, b), original_beige)
            
            # Adjust the white paper texture with this shadow difference
            paper_r, paper_g, paper_b, paper_a = pixels_white[x, y]
            new_r, new_g, new_b = adjust_paper_color((paper_r, paper_g, paper_b), shadow_diff)
            
            # Replace the pixel in the original image with the adjusted color
            pixels_yellow[x, y] = (new_r, new_g, new_b, paper_a)

# Save the final dynamically adjusted result
output_path_dynamic = "latest/dynamic_shadow_replacement_only_shadows.png"
yellow_img.save(output_path_dynamic)

output_path_dynamic
