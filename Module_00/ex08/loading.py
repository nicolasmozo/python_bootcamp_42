import time

def ft_progress(lst):
    size = len(lst)
    start = time.time()
    eta = size/100*2
    for i in range(size):
        percent = ('{0:.' + str(1) + 'f}').format(100 * i/float(size))
        filled_length = int(100*i // size)
        bar = '=' * filled_length + '>' + ' ' * (100 - filled_length)
        end = time.time()
        print(f'\r   ETA: {eta:.1f}s [{percent}%] [{bar}] {i}/{size} | elapsed time {end-start:.2f}s',end='\r')
        yield i