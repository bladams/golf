import sys, random, time

boardSize = (10,10)

while True: foo, bar, baz, globals()['board'] = None if globals().get('board') is None else [
        (
            [sys.stdout.write('X' if cell else ' ') for cell in row],
            sys.stdout.write('\n')
        ) for row in board
    ], time.sleep(1), sys.stdout.write('=' * boardSize[0]  +'\n'), [
            [random.random() < 0.5 for i in range(boardSize[0])] for j in range(boardSize[1])
        ] if 'board' not in globals() else [
            map(
                lambda z: (z[1] in (2,3) and board[y][z[0]]) or z[1]==3,
                [
                    (
                        x,
                        sum(
                            [
                                int(
                                    y0 in range(len(board)) and x0 in range(len(board[y0])) and board[y0][x0]
                                ) for x0,y0 in (
                                    (x - 1, y - 1),
                                    (x, y -1),
                                    (x + 1, y - 1),
                                    (x - 1, y),
                                    (x + 1, y),
                                    (x - 1, y + 1),
                                    (x, y + 1),
                                    (x + 1, y + 1)
                                    )
                                ]
                            )
                    ) for x in range(len(board[y]))]
                ) for y in range(len(board))
            ]
