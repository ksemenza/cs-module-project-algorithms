'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    # Your code here

    for i in range(0, len(arr)-1):
        appeared = 1
        for k in range(0, len(arr)-1):
            # check array values against it self
            if i != k:
                # check for pairs
                if arr[i] == arr[k]:
                    # if pair is found 
                    appeared += 1
        if appeared != 2:
            return arr[i]


def single_number_new(arr):
    result = 0
    for i in arr:
        result ^= i
    return result


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
    print(f"The odd-number-out in new is {single_number_new(arr)}")
