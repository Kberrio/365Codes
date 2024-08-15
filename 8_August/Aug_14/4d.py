import numpy as np

class Complex4DCounter:
    def __init__(self, max_value):
        self.max_value = max_value
        self.dimensions = self._calculate_dimensions()
        self.counter = np.zeros(self.dimensions, dtype=np.uint8)
        
    def _calculate_dimensions(self):
        bits_needed = self.max_value.bit_length()
        dim_size = int(np.ceil(np.power(bits_needed, 1/4)))
        return (dim_size, dim_size, dim_size, dim_size)
    
    def increment(self):
        if self.get_value() >= self.max_value:
            raise ValueError("Counter overflow")
        
        for i in range(self.dimensions[0]-1, -1, -1):
            for j in range(self.dimensions[1]-1, -1, -1):
                for k in range(self.dimensions[2]-1, -1, -1):
                    for l in range(self.dimensions[3]-1, -1, -1):
                        if self.counter[i,j,k,l] == 0:
                            self.counter[i,j,k,l] = 1
                            return
                        else:
                            self.counter[i,j,k,l] = 0
    
    def get_value(self):
        value = 0
        bit_position = 0
        for i in range(self.dimensions[0]):
            for j in range(self.dimensions[1]):
                for k in range(self.dimensions[2]):
                    for l in range(self.dimensions[3]):
                        if self.counter[i,j,k,l] == 1:
                            value |= (1 << bit_position)
                        bit_position += 1
        return value

# Example usage
counter = Complex4DCounter(1000)
for _ in range(20):
    print(f"Counter value: {counter.get_value()}")
    counter.increment()