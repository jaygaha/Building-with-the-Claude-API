def greeting():
    return "Hello! How can I assist you today?"


def calculate_pi():
    """
    Calculate pi to the 5th decimal place using the Machin formula.
    
    The Machin formula is: pi/4 = 4*arctan(1/5) - arctan(1/239)
    This converges quickly and gives us pi ≈ 3.14159
    """
    from decimal import Decimal, getcontext
    
    # Set precision high enough to get accurate 5 decimal places
    getcontext().prec = 50
    
    # Use the Machin formula: pi/4 = 4*arctan(1/5) - arctan(1/239)
    # We'll compute arctan using the Taylor series
    def arctan(x, num_terms=100):
        """Calculate arctan(x) using Taylor series"""
        x = Decimal(x)
        result = Decimal(0)
        for n in range(num_terms):
            result += ((-1) ** n) * (x ** (2 * n + 1)) / (2 * n + 1)
        return result
    
    pi = 4 * (4 * arctan(Decimal(1) / Decimal(5)) - arctan(Decimal(1) / Decimal(239)))
    
    # Round to 5 decimal places
    pi_rounded = round(float(pi), 5)
    
    return pi_rounded