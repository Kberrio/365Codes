import numpy as np
import pycuda.autoinit
import pycuda.driver as cuda
from pycuda.compiler import SourceModule

# CUDA kernel to perform vector addition
cuda_code = """
__global__ void vector_add(float *a, float *b, float *result, int n) {
    int tid = blockIdx.x * blockDim.x + threadIdx.x;
    if (tid < n)
        result[tid] = a[tid] + b[tid];
}
"""

# Compile CUDA kernel code
mod = SourceModule(cuda_code)

# Get CUDA function
vector_add = mod.get_function("vector_add")

def main():
    # Define array size
    n = 10000

    # Generate random input arrays
    a = np.random.randn(n).astype(np.float32)
    b = np.random.randn(n).astype(np.float32)

    # Allocate memory on device
    a_gpu = cuda.mem_alloc(a.nbytes)
    b_gpu = cuda.mem_alloc(b.nbytes)
    result_gpu = cuda.mem_alloc(a.nbytes)

    # Transfer data from host to device
    cuda.memcpy_htod(a_gpu, a)
    cuda.memcpy_htod(b_gpu, b)

    # Define grid and block dimensions
    block_size = 256
    grid_size = (n + block_size - 1) // block_size

    # Execute CUDA kernel
    vector_add(a_gpu, b_gpu, result_gpu, np.int32(n), block=(block_size, 1, 1), grid=(grid_size, 1))

    # Allocate memory on host for result
    result = np.empty_like(a)

    # Transfer result from device to host
    cuda.memcpy_dtoh(result, result_gpu)

    # Verify result
    expected_result = a + b
    np.testing.assert_allclose(result, expected_result, rtol=1e-5)

    print("Vector addition successfully performed!")

if __name__ == "__main__":
    main()
