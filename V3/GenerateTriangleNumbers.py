def get_triangle_x(n):
    if n < 1:
        return None  # handle invalid input
    else:
        result = sum(range(1, n+1))
        return result
    
def get_triangle_range(n):
    return [get_triangle_x(i) for i in range(1, n+1)]


if __name__ == "__main__":
    pass