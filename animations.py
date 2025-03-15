import time

# Displays loading animation with cycling dots
def loading_animation(cycles):
    patterns = ["", ".", "..", "..."]
    for _ in range(cycles):
        for pattern in patterns:
            # Clear the current line and print the new pattern with padding
            print(f"\rCalculating{pattern}   ", end='', flush=True)
            time.sleep(0.3)
    print()