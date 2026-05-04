import random
import json


def generate_random_numbers(n):
    """
    Return a random number between 1-1001 (in reality, 1-1000) for n times
    """
    return [random.randrange(1, 1001) for _ in range(n)]


def get_avg(nums):
    """
    Return the average of nums with no reminder
    """

    return sum(nums) / len(nums)


def get_standard_deviation(average, nums):
    """
    Standard deviation (SD) measures the spread of data around the mean,
    calculated by taking the square root of the variance
    """
    return (sum((x - average) ** 2 for x in nums) / len(nums)) ** 0.5  # chatgpt


def get_median(n, nums):
    """
    Median = The median is the middle value in an ordered dataset,
    separating the higher half from the lower half

    Sort nums in accending order.

    If even, find the middle index with n // 2 (no reminders), then
    since python list starts from index-0, middles are i and i - 1,
    we set left and right sides of middle and return it's average.

    If odd, middle is simply n // 2, which returns the middle number.
    """

    sorted_nums = sorted(nums)
    if n % 2 == 0:
        mid = n // 2
        mid_left = sorted_nums[mid - 1]
        mid_right = sorted_nums[mid]
        return (mid_left + mid_right) / 2
    else:
        mid = n // 2
        return sorted_nums[mid]


def get_modes(nums):
    """
    Modes = The numbers that appears the highest times.
    We iterate through all of the nums and count their appearances.

    We then find the highest count (max_count) by using #max() feeded with counts.values()
    which contains all of the counts, then, we iterate again through counts and compare each
    entry that has an equal count to max_count, then append to modes list.

    Finally, return a tuple containing the max_count and the list of nums accounting.
    """
    counts = {}
    for num in nums:
        if num in counts:
            counts[num] = counts[num] + 1
        else:
            counts[num] = 1

    max_count = max(counts.values())

    modes = []
    for number, count in counts.items():
        if count == max_count:
            modes.append(number)

    return (max_count, modes)


def GenerateRandomNumbersFile(file_name, n):
    try:
        with open(file_name, "w+") as file:
            if n <= 0:
                print("n must be greater than 0")
                return
            nums = generate_random_numbers(n)
            average = get_avg(nums)
            standard_deviation = get_standard_deviation(average, nums)
            median = get_median(n, nums)
            max_count, modes = get_modes(nums)
            file.write(json.dumps(
                {
                    "average": average,
                    "standard_deviation": standard_deviation,
                    "median": median,
                    "modes": {
                        "max_count": max_count,
                        "modes": modes
                    },
                    "nums": nums,
                }, indent=4
            ))
    except FileNotFoundError:
        print(f"{file_name} does not exist")
    except PermissionError:
        print(f"Permission denied for {file_name}")


if __name__ == "__main__":
    GenerateRandomNumbersFile("test.json", 1000)
