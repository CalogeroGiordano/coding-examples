from os import remove
from A import do_part_A
from glob import glob

ball_files = glob("images\\easy\\ball\\*.txt")
brick_files = glob("images\\easy\\brick\\*.txt")
cylinder_files = glob("images\\easy\\cylinder\\*.txt")
test_files = glob("images\\test\\*.txt")

def get_histograms(filenames):
    reds = []
    greens = []
    blues = []

    for filename in filenames:
        r, g, b = do_part_A(filename)
        
        reds.append(r)
        greens.append(g)
        blues.append(b)
    
    return reds, greens, blues

def take_average(histograms):
    avg_hist = {}

    for i in range(256):
        avg_hist[i] = 0

    for hist in histograms:
        for i in range(256):
            avg_hist[i] = avg_hist[i] + hist[i]
    
    for i in range(256):
        avg_hist[i] = avg_hist[i] / len(histograms)
    
    return avg_hist

def average_hist(files):
    if type(files) == list:
        reds, greens, blues = get_histograms(files)
        avg_hist = {
            "red": take_average(reds),
            "green": take_average(greens),
            "blue": take_average(blues)
        }
    else:
        reds, greens, blues = do_part_A(files)
        avg_hist = {
            "red": reds,
            "green": greens,
            "blue": blues
        }

    return avg_hist


ball_avg = average_hist(ball_files)
brick_avg = average_hist(brick_files)
cylinder_avg = average_hist(cylinder_files)

def compare_histograms(lhs, rhs):
    result = 0

    for i in range(256):
        result = result + abs(lhs[i] - rhs[i])
    
    return result

def predict(ball, brick, cylinder, test_file):
    results = []
    test = average_hist(test_file)

    for obj in [ball, brick, cylinder]:
        result = 0
        for channel in ["red", "green", "blue"]:
            result += compare_histograms(obj[channel], test[channel])
        
        results.append(result)
    
    min_value = min(results)
    min_index = results.index(min_value)

    return ["ball", "brick", "cylinder"][min_index]


for test_file in test_files:
    print(f"{test_file}\t -> {predict(ball_avg, brick_avg, cylinder_avg, test_file)}")
