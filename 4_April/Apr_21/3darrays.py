class MultiDimensionalArray:
    def __init__(self, shape):
        self.shape = shape
        self.size = self._calculate_size(shape)
        self.data = [0] * self.size

    def _calculate_size(self, shape):
        size = 1
        for dim in shape:
            size *= dim
        return size

    def _validate_index(self, index):
        if len(index) != len(self.shape):
            raise ValueError("Index dimensions must match array dimensions")
        for i, dim_size in enumerate(self.shape):
            if not (0 <= index[i] < dim_size):
                raise IndexError("Index out of range")

    def _index_to_flat(self, index):
        flat_index = 0
        multiplier = 1
        for i in range(len(index) - 1, -1, -1):
            flat_index += index[i] * multiplier
            multiplier *= self.shape[i]
        return flat_index

    def _flat_to_index(self, flat_index):
        index = []
        for dim_size in reversed(self.shape):
            index.append(flat_index % dim_size)
            flat_index //= dim_size
        return list(reversed(index))

    def __getitem__(self, index):
        self._validate_index(index)
        flat_index = self._index_to_flat(index)
        return self.data[flat_index]

    def __setitem__(self, index, value):
        self._validate_index(index)
        flat_index = self._index_to_flat(index)
        self.data[flat_index] = value

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return repr(self.data)

    def __add__(self, other):
        if isinstance(other, MultiDimensionalArray):
            if self.shape != other.shape:
                raise ValueError("Shapes of arrays must match for addition")
            result = MultiDimensionalArray(self.shape)
            for i in range(self.size):
                result.data[i] = self.data[i] + other.data[i]
            return result
        else:
            raise TypeError("Unsupported operand type(s) for +: '{}' and '{}'".format(
                type(self).__name__, type(other).__name__))

    def __sub__(self, other):
        if isinstance(other, MultiDimensionalArray):
            if self.shape != other.shape:
                raise ValueError("Shapes of arrays must match for subtraction")
            result = MultiDimensionalArray(self.shape)
            for i in range(self.size):
                result.data[i] = self.data[i] - other.data[i]
            return result
        else:
            raise TypeError("Unsupported operand type(s) for -: '{}' and '{}'".format(
                type(self).__name__, type(other).__name__))


# Example usage:
arr1 = MultiDimensionalArray([2, 3])
arr1[0, 0] = 1
arr1[0, 1] = 2
arr1[0, 2] = 3
arr1[1, 0] = 4
arr1[1, 1] = 5
arr1[1, 2] = 6

arr2 = MultiDimensionalArray([2, 3])
arr2[0, 0] = 7
arr2[0, 1] = 8
arr2[0, 2] = 9
arr2[1, 0] = 10
arr2[1, 1] = 11
arr2[1, 2] = 12

print("Array 1:")
print(arr1)
print("Array 2:")
print(arr2)

print("Array 1 + Array 2:")
print(arr1 + arr2)

print("Array 1 - Array 2:")
print(arr1 - arr2)
