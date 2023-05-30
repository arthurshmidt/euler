# Euler problem #15
#
# Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routs to the bottom right corner.
#
# how many such routes are there through a 20x20 grid?

def recursive(e, p, f):
    if p == e:
        f = f + 1
    elif p != e:
            if p["X"] != e["X"]:
                p["X"] = p["X"] + 1
                e, p, f = recursive(e, p, f)
            if p["Y"] != e["Y"]:
                p["Y"] = p["Y"] + 1
                e, p, f = recursive(e, p, f)
    return e, p, f

if __name__ == "__main__":
    p = {
            "X": 0,
            "Y": 0
            }

    e = {
            "X": 2,
            "Y": 2
            }

    f = 0

    e, p, f = recursive(e,p,f)
    
    print(f"Number of Paths: {f}")

