from PIL import Image, ImageEnhance

# Load the original image and the white paper texture image
yellow_img = Image.open("latest/yellow.jpg").convert("RGBA")
white_img = Image.open("latest/white.jpg").resize(yellow_img.size).convert("RGBA")

# Convert the white paper texture to grayscale to extract luminance
white_luminance = white_img.convert("L")  # Luminance-only image (grayscale)

# Access pixel data
pixels_yellow = yellow_img.load()
pixels_luminance = white_luminance.load()

# Define the original beige base color and a threshold for detecting shadows
original_beige = (255, 235, 202)
shadow_threshold = 15  # Adjust this to widen or narrow the shadow range

# Get the target color from the user for replacing the beige area
target_color_hex = input("Enter the target color for the beige region in HEX format (e.g., #D8BFD8 for pastel purple): ").strip()
target_color_rgb = tuple(int(target_color_hex[i:i+2], 16) for i in (1, 3, 5))  # Convert HEX to RGB

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

# Function to adjust color with the calculated shadow difference
def adjust_color(base_color, shadow_diff):
    new_r = max(0, min(255, base_color[0] - shadow_diff[0]))
    new_g = max(0, min(255, base_color[1] - shadow_diff[1]))
    new_b = max(0, min(255, base_color[2] - shadow_diff[2]))
    return new_r, new_g, new_b

# Iterate over pixels to replace the beige color and adjust the shadow accordingly
for y in range(yellow_img.height):
    for x in range(yellow_img.width):
        r, g, b, a = pixels_yellow[x, y]
        
        # Check if the current color is within the shadow range
        if is_within_shadow_range((r, g, b), original_beige, shadow_threshold):
            # Calculate shadow difference from the original beige
            shadow_diff = calculate_shadow_adjustment((r, g, b), original_beige)
            
            # Adjust the target color for the shadow effect
            adjusted_color = adjust_color(target_color_rgb, shadow_diff)
            
            # Get luminance value from the grayscale texture image
            luminance_value = pixels_luminance[x, y]
            
            # Blend luminance with target color (dominant luminance influence)
            blended_r = int((luminance_value / 255.0) * adjusted_color[0])
            blended_g = int((luminance_value / 255.0) * adjusted_color[1])
            blended_b = int((luminance_value / 255.0) * adjusted_color[2])
            
            # Update the pixel in the original image with the adjusted and blended color
            pixels_yellow[x, y] = (blended_r, blended_g, blended_b, a)

# Save the final dynamically adjusted result
output_path_dynamic = "latest/full_strength_texture_color.png"
yellow_img.save(output_path_dynamic)

print(f"Saved the final result at: {output_path_dynamic}")
