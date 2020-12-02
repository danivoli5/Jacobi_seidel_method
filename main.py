def printMat(Mat):
    for i in Mat:
        for j in i:
            print(j, end=' ')
        print()


def testDiagonal(A):
    diagonal = []
    for i in range(0, len(A)):
        for j in range(0, len(A)):
            if i == j:
                diagonal.append(A[i][j])

    for i in range(0, len(A)):
        sum = 0
        for j in range(0, len(A)):
            if j != i:
                sum += A[i][j]

        if abs(diagonal[i]) < sum:
            print("Wrong diagonal")
            break


def jacoby(a, x, b):
    # Finding length of a(3)
    n = len(a)
    # for loop for 3 times as to calculate x, y , z
    y = [0 for a in x]
    for j in range(0, n):
        # temp variable d to store b[j]
        d = b[j]

        # to calculate respective xi, yi, zi
        for i in range(0, n):
            if (j != i):
                d -= a[j][i] * x[i]
                # updating the value of our solution
        y[j] = d / a[j][j]
        # returning our updated solution
    return y


def seidel(a, x, b):
    # Finding length of a(3)
    n = len(a)
    # for loop for 3 times as to calculate x, y , z
    for j in range(0, n):
        # temp variable d to store b[j]
        d = b[j]

        # to calculate respective xi, yi, zi
        for i in range(0, n):
            if (j != i):
                d -= a[j][i] * x[i]
                # updating the value of our solution
        x[j] = d / a[j][j]
        # returning our updated solution
    return x


def calsEps(x, y, eps):
    for i in range(len(x)):
        if abs(x[i] - y[i]) > eps:
            return True
    return False


def mainSeidel_seidel(a, x, b, eps):
    first = [eps + 1 for a in x]
    iter = 0
    while (calsEps(x, first, eps)):
        iter = iter + 1
        first = [a for a in x]
        x = seidel(a, x, b)
        # print each time the updated solution
        print(x)
    print(x)
    print("number of itertion=" + str(iter))


def mainSeidel_jacoby(a, x, b, eps):
    testDiagonal(a)
    first = [eps + 1 for a in x]
    iter = 0
    while (calsEps(x, first, eps)):
        iter = iter + 1
        first = [a for a in x]
        x = jacoby(a, x, b)
        # print each time the updated solution
        print(x)
    print(x)
    print("number of itertion=" + str(iter))


def main():
    eps = 0.0001
    a = []
    x = [0, 0, 0]
    b = []

    # Initialize matrix
    print("Enter the Mat(a) by row:")

    for i in range(0, 3):
        row = []
        for j in range(0, 3):
            row.append(int(input()))
        a.append(row)
    printMat(a)
    print()

    print("Enter the Solution(b) vector:")

    for i in range(0, 3):
        b.append(int(input()))
    print(b)
    print()

    menu = {'1': "mainSeidel_seidel.", '2': "mainSeidel_jacoby.", '3': "Exit"}

    while True:
        options = menu.keys()
        for entry in options:
            print(entry, menu[entry])

        selection = input("Please Select:")
        if selection == '1':
            mainSeidel_jacoby(a, x, b, eps)
        elif selection == '2':
            mainSeidel_seidel(a, x, b, eps)
        elif selection == '3':
            print("Bye Bye..")
            return False
        else:
            print("Unknown option selected!")


if __name__ == "__main__":
    main()
