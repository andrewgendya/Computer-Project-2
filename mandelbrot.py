import numpy as np


def get_escape_time(c: complex, max_iterations: int) -> int | None:
    """takes complex number and sets z value to that. loops through till max iteration
    and applies mandelbrot calculation to it. if calculated z value is greater than 2, then returns
    the number of iterations, which is i. returns None if never exceeds 2 after iterating
    the maximum number of times"""
    z = 0 + 0j #notes z is a complex number
    for i in range(max_iterations): #looping through max times
        z = z*z + c # calculation for mandelbrot set
        if abs(z) > 2: # if the z value is greater than two, then set will go to infinity
            return i # therefore returns the i value, which is the number of iterations
    return None # returns none for complex numbers that don't exceed 2 after maximum iterations

# print(get_escape_time(2+1j, 5))
# print(get_escape_time(1+1j, 10))
# print(get_escape_time(0.5+0.5j, 3))
# print(get_escape_time(0.5+0.5j, 4))
# print(get_escape_time(0.38+0.25j, 100))

def get_escape_time_color_arr(
    c_arr: np.ndarray,
    max_iterations: int
) -> np.ndarray:
    z= np.zeros_like(c_arr, dtype=np.complex128)
    escape_time =np.full(c_arr.shape, max_iterations+1, dtype=np.int32)
    mask=np.ones(c_arr.shape, dtype=np.bool)
    for i in range(1, max_iterations+1):
        z[mask]=z[mask]**2+c_arr[mask]
        escape=np.abs(z)>2
        escape_time[mask * escape]=i
        mask= mask*(~escape)
    color_arr = (max_iterations-escape_time+1)/(max_iterations+1)
    return color_arr



