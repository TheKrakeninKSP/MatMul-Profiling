import numpy as np
import time

N = 512

def loop_blocking_before(A, B, C, block_size):
    print("\n<------------------LOOP BLOCKING OPTIMIZATION----------------->")
    # Before optimization
    start_time = time.time()
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i, j] += A[i, k] * B[k, j]
    execution_time = time.time() - start_time
    print(f"Execution Time before manual optimization: {execution_time:.6f} seconds")

def loop_blocking(A, B, C, block_size):

    # After optimization with larger block size and better cache utilization
    C.fill(0)
    start_time = time.time()
    block_size = 32  # Increased block size for better cache utilization
    for ii in range(0, N, block_size):
        for kk in range(0, N, block_size):
            for jj in range(0, N, block_size):
                for i in range(ii, min(ii + block_size, N)):
                    for k in range(kk, min(kk + block_size, N)):
                        temp = A[i, k]
                        for j in range(jj, min(jj + block_size, N)):
                            C[i, j] += temp * B[k, j]
    execution_time = time.time() - start_time
    print(f"Execution Time after manual optimization: {execution_time:.6f} seconds")


if __name__ == "__main__":
    print("MATRIX MULTIPLICATION PROBLEM")
    
    # Initialize matrices
    A = np.random.rand(N, N)
    B = np.random.rand(N, N)
    C = np.zeros((N, N))

    # Run optimizations
    #loop_interchange(A, B, C)
    #C.fill(0)
    block_size = 32  # Increased block size
    loop_blocking_before(A, B, C, block_size)
    #C.fill(0)
    #loop_unrolling(A, B, C)
    #C.fill(0)
    #loop_fusion(A, B, C)
