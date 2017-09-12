#!/usr/bin/python3


def squaresUnderQueenAttack(n, queens, queries):

    def checkVertHorz(queen, piece):
        if queen[0] == piece[0] or queen[1] == piece[1]:
            return True
        return False

    def checkDiag(n, queen, piece, direction):

        def goneTooFar(direction, queen, piece):
            '''Attempting to reduce costs by stopping calculation is queen
            is not in range to attack piece'''
            if goList == 0:
                print('tick')
                if queen[0] < piece[0] or queen[1] < piece[1]:
                    print('stopping NW')
                    return True
            elif goList == 1:
                if queen[0] < piece[0] or queen[1] > piece[1]:
                    return True
            elif goList == 2:
                if queen[0] > piece[0] or queen[1] < piece[1]:
                    return True
            else:
                if queen[0] > piece[0] or queen[1] > piece[1]:
                    return True
            return False

        goList = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        direction, goList = goList[direction], direction
        stopper = n-1
        while True:
            queen = [queen[0] + direction[0], queen[1] + direction[1]]
            if not goneTooFar(goList, queen, piece):
                if queen == piece:
                    return True
                if queen[0] < 0 or queen[0] > stopper:
                    return False
                if queen[1] < 0 or queen[1] > stopper:
                    return False
            else:
                return False

    outList = []
    for piece in queries:
        tests = []
        for queen in queens:
            tests.append(queen[0] == piece[0] or queen[1] == piece[1])
            if True not in tests:
                for direction in range(4):
                    result = checkDiag(n, queen, piece, direction)
                    if result is True:
                        tests.append(result)
                    else:
                        tests.append(result)
                        break
            else:
                tests.append(False)
                break

        if True not in tests:
            outList.append(False)
        else:
            outList.append(True)

    return outList


# if __name__ == '__main__':
#     squaresUnderQueenAttack()
