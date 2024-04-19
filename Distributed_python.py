from mpi4py import MPI
import time
import math

def f(x):
    return math.sqrt(1 - x**2)

def compute_pi_distributed(N):
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()
    start_time = MPI.Wtime()  # Start timing

    delta_x = 1.0 / N
    local_n = N // size
    local_sum = sum(f(i * delta_x) * delta_x for i in range(rank * local_n, (rank + 1) * local_n))

    total_sum = comm.reduce(local_sum, op=MPI.SUM, root=0)

    if rank == 0:
        end_time = MPI.Wtime()  # End timing
        print("Approximation of π:", total_sum * 4)
        print("Execution time:", end_time - start_time, "seconds")

if __name__ == "__main__":
    compute_pi_distributed(1000000)
