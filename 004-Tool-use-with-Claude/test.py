import math
from main import calculate_pi, greeting


def test_calculate_pi():
    """Test the calculate_pi function"""
    
    # Get the calculated pi value
    calculated_pi = calculate_pi()
    
    # Get the expected pi value from math module
    expected_pi = math.pi
    
    print("=" * 50)
    print("Testing calculate_pi() function")
    print("=" * 50)
    print(f"Calculated Pi: {calculated_pi}")
    print(f"Expected Pi:   {expected_pi}")
    print(f"Match to 5 decimals: {round(expected_pi, 5)}")
    print()
    
    # Test 1: Check if the result is close to math.pi
    assert abs(calculated_pi - expected_pi) < 0.00001, \
        f"Pi value {calculated_pi} is not close enough to {expected_pi}"
    print("✓ Test 1 passed: Calculated pi matches math.pi to 5 decimal places")
    
    # Test 2: Check if pi is rounded to exactly 5 decimal places
    decimal_places = len(str(calculated_pi).split('.')[-1]) if '.' in str(calculated_pi) else 0
    assert decimal_places <= 5, \
        f"Pi should have at most 5 decimal places, got {decimal_places}"
    print(f"✓ Test 2 passed: Pi has {decimal_places} decimal places (max 5)")
    
    # Test 3: Check if pi is approximately 3.14159
    expected_rounded = 3.14159
    assert calculated_pi == expected_rounded, \
        f"Pi should be 3.14159, got {calculated_pi}"
    print(f"✓ Test 3 passed: Pi equals 3.14159")
    
    # Test 4: Check if pi is within reasonable bounds
    assert 3.14 < calculated_pi < 3.15, \
        f"Pi should be between 3.14 and 3.15, got {calculated_pi}"
    print(f"✓ Test 4 passed: Pi is within bounds (3.14 < pi < 3.15)")
    
    print()
    print("=" * 50)
    print("All tests passed! ✓")
    print("=" * 50)


def test_greeting():
    """Test the greeting function"""
    print("\nTesting greeting() function")
    print("=" * 50)
    result = greeting()
    print(f"Greeting result: {result}")
    assert isinstance(result, str), "Greeting should return a string"
    assert "Hello" in result, "Greeting should contain 'Hello'"
    print("✓ Greeting function works correctly")
    print("=" * 50)


if __name__ == "__main__":
    test_greeting()
    test_calculate_pi()
