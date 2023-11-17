def make_pattern():
    patterns = ["    *    ", "   * *   ", "  * * *  ", " * * * * ", "* * * * *"]
    x = 0
    for loop in range(5):
        print(patterns[x])
        print("\n")
        x += 1


make_pattern()
