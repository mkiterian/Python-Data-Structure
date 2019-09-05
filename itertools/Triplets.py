from itertools import combinations


# Pythogeros Triplet - Formula - a^2 + b^2 = c^2

def test(inputValue):
    return combinations(inputValue, 2)



print(list(test("1234")))


def testWithInputArray(inputArray):
    squareArray = dict((y**2, y) for y in inputArray)
    print(squareArray)

    print(list(combinations(squareArray, 2)))

    for x,y in combinations(squareArray, 2):
        if x+y in squareArray.keys():
            print(squareArray[x], squareArray[y], squareArray[x+y])

print(testWithInputArray(list(range(1,100))))