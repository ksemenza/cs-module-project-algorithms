'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    zeros = arr.count(0)
    count = 1
    while count <= zeros:
        i = arr.index(0)
        if arr[-count] != 0:
            arr[i], arr[-count] = arr[-count], arr[i]

        return arr


def moving_zeroes_new(arr):
    # Your code here
    resArr = []
    for i in range(0, len(arr)):
        if arr[i] == 0:
            resArr.append(0)
        else:
            resArr.insert(0, arr[i])

    return resArr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
    print(f"The resulting of moving_zeroes_new is: {moving_zeroes_new(arr)}")
