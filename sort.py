# Function to sort and categorize
def sort(width, height, length, mass):
    volume = width * height * length
    bulky = volume >= 1000000 or width >= 150 or height >= 150 or length >= 150
    heavy = mass >= 20

    if bulky and heavy:
        return "REJECTED"
    if bulky or heavy:
        return "SPECIAL"
    return "STANDARD"

# Test cases
def run_tests():
    assert sort(100, 100, 100, 10) == "SPECIAL", "Test 1 Failed"
    assert sort(160, 50, 50, 10) == "SPECIAL", "Test 2 Failed"   # bulky
    assert sort(100, 100, 100, 25) == "REJECTED", "Test 3 Failed" # heavy
    assert sort(200, 200, 200, 30) == "REJECTED", "Test 4 Failed" # both
    assert sort(149, 149, 149, 19.9) == "SPECIAL", "Test 5 Failed" # edge
    assert sort(150, 100, 100, 19.9) == "SPECIAL", "Test 6 Failed" # bulky edge
    assert sort(100, 10, 100, 10) == "STANDARD", "Test 7 Failed" # heavy edge
    print("All tests passed!")

# Running Test Cases
if __name__ == "__main__":
    run_tests()