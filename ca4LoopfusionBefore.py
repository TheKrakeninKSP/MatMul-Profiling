import numpy as np
import time

N = 512
def loop_fusion_before(A, B, C):

    print("\n<------------------LOOP FUSION OPTIMIZATION----------------->")
    # Before optimization
    start_time = time.time()
    for i in range(N):
        for j in range(N):
            C[i, j] = 0.0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i, j] += A[i, k] * B[k, j]
    execution_time = time.time() - start_time
    print(f"Execution Time before loop fusion: {execution_time:.6f} seconds")

def loop_fusion(A, B, C):

    # After optimization with temporary accumulation
    C.fill(0)
    start_time = time.time()
    for i in range(N):
        for j in range(N):
            temp_sum = 0.0
            for k in range(N):
                temp_sum += A[i, k] * B[k, j]
            C[i, j] = temp_sum
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
    #block_size = 32  # Increased block size
    #loop_blocking(A, B, C, block_size)
    #C.fill(0)
    #loop_unrolling(A, B, C)
    #C.fill(0)
    loop_fusion_before(A, B, C)
