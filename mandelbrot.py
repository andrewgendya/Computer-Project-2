def get_escape_time(c: complex, max_iterations: int) -> int | None:
    """takes complex number and sets z value to that. loops through till max iteration
    and applies mandelbrot calculation to it. if calculated z value is greater than 2, then returns
    the number of iterations, which is i. returns None if never exceeds 2 after iterating
    the maximum number of times"""
    z = 0 + 0j #notes z is a complex number
    for i in range(max_iterations): #looping through max times
        z = z**2 + c # calculation for mandelbrot set
        if abs(z) > 2: # if the z value is greater than two, then set will go to infinity
            return i # therefore returns the i value, which is the number of iterations
    return None # returns none for complex numbers that don't exceed 2 after maximum iterations





