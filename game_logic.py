import numpy as np


def get_next_stage(stage: np.ndarray):
    next_stage = np.empty_like(stage)
    for y in range(stage.shape[0]):
        for x in range(stage.shape[1]):
            min_x = x-1 if x > 0 else x
            min_y = y-1 if y > 0 else y
            max_x = x+2 if x + 2 <= stage.shape[1] else x + 1
            max_y = y+2 if y + 2 <= stage.shape[0] else y + 1
            count = np.count_nonzero(stage[min_y:max_y, min_x:max_x])  # arr[y][x] is inside the slice, then is counted
            next_stage[y][x] = (stage[y][x] and count in [3, 4]) or (not stage[y][x] and count == 3)
    return next_stage


if __name__ == '__main__':
    import time

    arr = np.array([
        [False, False, False],
        [True, True, True],
        [False, False, False]
    ])
    print('original stage:')
    print(arr)
    arr = get_next_stage(arr)
    print('next stage:')
    print(arr)

    arr = np.random.choice(a=[False, True], size=(1000, 1000))
    t = time.process_time()
    arr = get_next_stage(arr)
    print(f'elapsed time in big array: {time.process_time()-t} sec')
