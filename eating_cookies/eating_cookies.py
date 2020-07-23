'''
Input: an integer
Returns: an integer
'''


def eating_cookies(n, cache=None):
    if not cache:
        cache = [0 for _ in range(11)]
    cache[0], cache[1], cache[2] = 1, 1, 2
    if cache[n]:
        return cache[n]
    cache[n] = eating_cookies(
        n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
    return cache[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
