from dimensional import Vector

if __name__ == "__main__":
    # Create a 5D vector and assign some values
    vec1 = Vector(5)
    vec1[1] = 46
    vec1[-1] = 90
    print(f"vec1 = {vec1}")   # Expected: <0, 46, 0, 0, 90>

    # Another vector with some elements
    vec2 = Vector(5)
    vec2[1] = 1
    vec2[2] = 2
    print(f"vec2 = {vec2}")   # Expected: <0, 1, 2, 0, 0>

    # Add two vectors
    sum_vec = vec1 + vec2
    print(f"vec1 + vec2 = {sum_vec}")  # Expected: <0, 47, 2, 0, 90>

    # Add a list to a vector
    list_add = vec2 + [5, 3, 10, -2, 1]
    print(f"vec2 + [5,3,10,-2,1] = {list_add}")  # Expected: <5, 4, 12, -2, 1>

    # Check equality
    print(f"Are vec1 and vec2 equal? {vec1 == vec2}")
    print(f"Are vec1 and vec2 different? {vec1 != vec2}")

    # Check length and sum
    print(f"Length of vec1: {len(vec1)}")
    print(f"Sum of elements in vec1: {sum(vec1)}")

