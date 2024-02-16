import numpy as np
import time

# Allocate memory
memory_array = np.zeros(200 * 1024 * 1024 // 8, dtype=np.float64)

# Keep the script running to hold memory
while True:
    time.sleep(1)
