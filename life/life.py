import sys, random, time

boardSize = (10,10)
# board = tuple([random.random() < 0.5 for i in range(boardSize[0] * boardSize[1])])
# board = [
#     [random.random() < 0.5 for i in range(boardSize[0])] for j in range(boardSize[1])
# ]

# def print_board():
#     return None if globals().get('board') is None else [
#         (
#             sys.stdout.write('%.2d '%num),
#             [sys.stdout.write('X' if cell else '_') for cell in row],
#             sys.stdout.write('\n')
#         ) for num, row in enumerate(board)
#     ]


# def transform():
#     return [
#         map(
#             lambda z: (z[1] in (2,3) and board[y][z[0]]) or z[1]==3,
#             [
#                 (
#                     x,
#                     sum(
#                         [
#                             int(
#                                 y0 in range(len(board)) and x0 in range(len(board[y0])) and board[y0][x0]
#                             ) for x0,y0 in (
#                                 (x - 1, y - 1),
#                                 (x, y -1),
#                                 (x + 1, y - 1),
#                                 (x - 1, y),
#                                 (x + 1, y),
#                                 (x - 1, y + 1),
#                                 (x, y + 1),
#                                 (x + 1, y + 1)
#                                 )
#                             ]
#                         )
#                 ) for x in range(len(board[y]))]
#             ) for y in range(len(board))
#         ]

while True: foo, bar, baz, globals()['board'] = None if globals().get('board') is None else [
        (
            sys.stdout.write('%.2d '%num),
            [sys.stdout.write('X' if cell else '_') for cell in row],
            sys.stdout.write('\n')
        ) for num, row in enumerate(board)
    ], time.sleep(1), sys.stdout.write('==============\n'), [
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
