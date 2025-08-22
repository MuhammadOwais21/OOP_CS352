class Vector:
    def __init__(self, dimension):
        self._coords = [0] * dimension

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, index):
        return self._coords[index]

    def __setitem__(self, index, value):
        self._coords[index] = value

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("Vector sizes must match")
        new_vec = Vector(len(self))
        for i in range(len(self)):
            new_vec[i] = self[i] + other[i]
        return new_vec

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        return all(self[i] == other[i] for i in range(len(self)))

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return f"<{', '.join(str(x) for x in self._coords)}>"
