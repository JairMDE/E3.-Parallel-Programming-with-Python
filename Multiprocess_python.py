import multiprocessing as mp
import math
import time

def f(x):
    return math.sqrt(1 - x**2)

def partial_sum(start, end, delta_x):
    sum = 0.0
    for i in range(start, end):
        xi = i * delta_x
        sum += f(xi) * delta_x
    return sum

def compute_pi_parallel(N, num_processes):
    delta_x = 1.0 / N
    pool = mp.Pool(num_processes)
    results = [pool.apply_async(partial_sum, (i * N // num_processes, (i + 1) * N // num_processes, delta_x)) for i in range(num_processes)]
    pool.close()
    pool.join()
    pi_approx = sum([result.get() for result in results]) * 4
    return pi_approx

def main():
    num_processes = 4

    start_time = time.time()
    pi_approx = compute_pi_parallel(1000000, num_processes)
    end_time = time.time()

    print("Approximation of π:", pi_approx)
    print("Execution time:", end_time - start_time, "seconds")


if __name__ == '__main__':
    main()
