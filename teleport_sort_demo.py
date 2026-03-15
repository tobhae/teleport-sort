import argparse
import random
import time

from teleport_sort import teleport_sort

def generate_list(size):
    return random.sample(range(size * 3), size)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--size", help="Length of the random list", type=int, required=True)

    args = parser.parse_args()
    arr = generate_list(args.size)

    print(f"Initial list: {arr}")

    start = time.time()

    sorted_arr, iterations = teleport_sort(arr)

    elapsed = time.time() - start

    print(f"Sorted list: {sorted_arr}")
    print(f"It took {elapsed:.3f} seconds to TeleportSort this list.")
    print(f"Elements were teleported {iterations:,}".replace(",", " ") + " times.")

if __name__ == "__main__":
    main()