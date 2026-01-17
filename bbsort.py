from colorama import Fore as C, init
init(autoreset=True)

def log(color, text):
    print(color + text)

data = [64, 34, 25, 12, 22, 11, 90]
n = len(data)

log(C.YELLOW, f"Initial array: {data}\n")

for pass_no in range(n - 1):
    swapped = False
    log(C.MAGENTA, f"PASS {pass_no + 1}")

    for i in range(n - 1 - pass_no):
        log(C.CYAN, f" Comparing {data[i]} and {data[i+1]}")

        if data[i] > data[i + 1]:
            log(C.RED, "  Swap!")
            data[i], data[i + 1] = data[i + 1], data[i]
            swapped = True
        else:
            log(C.GREEN, "  No swap")

        log(C.WHITE, f"  Current: {data}\n")

    if not swapped:
        log(C.GREEN, "Array sorted early")
        break

log(C.YELLOW, f"\nSorted array: {data}")
