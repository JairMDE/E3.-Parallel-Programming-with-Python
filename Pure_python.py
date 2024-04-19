import math
import time

def f(x):
    return math.sqrt(1 - x**2)

def compute_pi_sequential(N):
    delta_x = 1.0/N
    sum = 0.0

    for i in range(N):
        xi = i * delta_x
        sum += f(xi) * delta_x
    return sum * 4



start_time = time.time()
pi_approx = compute_pi_sequential(1000000)
end_time = time.time()

print("Approximation of π:", pi_approx)
print("Execution time:", end_time - start_time, "seconds")
