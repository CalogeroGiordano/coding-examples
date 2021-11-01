def compute_histogram(arr):
    histogram = {}

    for i in range(256):
        histogram[i] = 0

    for color in arr:
        histogram[color] = histogram[color] + 1
    
    for i in range(256):
        histogram[i] = histogram[i] / len(arr)

    return histogram

def extract_colors(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

        width = int(lines[1])
        height = int(lines[2])

        i = 3
        reds = []
        greens = []
        blues = []
        for pixel in lines[3:]:
            pixel = tuple(pixel.split())
            red, green, blue = pixel

            red = int(red)
            green = int(green)
            blue = int(blue)

            reds.append(red)
            greens.append(green)
            blues.append(blue)


    return reds, greens, blues

def do_part_A(filename):
    reds, greens, blues = extract_colors(filename)
    red_hist = compute_histogram(reds)
    green_hist = compute_histogram(greens)
    blue_hist = compute_histogram(blues)

    return red_hist, green_hist, blue_hist
