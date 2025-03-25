# Compiler Optimization Techniques for Reducing Cache Misses in Matrix Multiplication

## Introduction  
This project analyzes various **matrix multiplication (512 × 512) optimization techniques** to improve cache utilization and execution speed. The optimizations include:  
- **Loop Interchange**  
- **Loop Blocking**  
- **Loop Unrolling**  
- **Loop Fusion**  

Performance metrics such as **execution time, cache misses, and CPU cycles** were evaluated using Perf.  

---

## Optimization Techniques  

### Loop Interchange  
🔹 Changes the order of loop nesting to improve memory access patterns.  
**Results:** Negligible improvement, sometimes worsening performance.  

### Loop Blocking  
🔹 Divides the matrix into smaller blocks to improve cache reuse.  
**Results:** Achieved a **3.7% improvement** in execution time.  

### Loop Unrolling  
🔹 Expands loop iterations to reduce loop control overhead and improve instruction-level parallelism.  
**Results:** Improved execution time by **28.1%** but increased L1 cache pressure.  

### Loop Fusion  
🔹 Merges multiple loops to reduce loop overhead and enhance cache efficiency.  
**Results:** Best performance boost with a **40.4% reduction** in execution time.  

---

## Performance Metrics (Before vs After Optimization)  

| Optimization  | Execution Time ↓ | L1 D-Cache Load Misses ↓ | LLC Load Misses ↓ |
|--------------|----------------|-------------------------|-------------------|
| **Loop Interchange** | -1.2% (Worse) | 🔺 Increased | 🔺 Increased |
| **Loop Blocking** | ✅ +3.7% | ✅ -80% | ✅ -98% |
| **Loop Unrolling** | ✅ +28.1% | 🔺 Increased | 🔺 Increased |
| **Loop Fusion** | 🚀 +40.4% | ✅ Reduced | ✅ Drastically Reduced |

Loop Fusion proved to be the **most effective optimization**, reducing both execution time and cache misses.  

---

## Contributers
Kathiravan.S (CS22B2052)

Ashiq Irfaan.A.F (CS22B2021) 
