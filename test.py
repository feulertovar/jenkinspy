import unittest
import hello  # Assuming 'hello.py' contains the say_hello function

class TestHelloWorld(unittest.TestCase):

    def test_say_hello(self):
        """Test that the say_hello function returns the expected message."""
        result = hello.say_hello()
        self.assertEqual(result, "Hello, Jenkins!")
    
    def test_say_hello_empty_input(self):
        """Test the behavior when an empty string is passed to say_hello (if applicable)."""
        # Modify the say_hello function in 'hello.py' to handle inputs if needed
        result = hello.say_hello("")
        self.assertEqual(result, "Hello, Jenkins!")  # Or other expected result
    
    def test_say_hello_edge_case(self):
        """Test the behavior for edge cases or unusual inputs (if applicable)."""
        # For example, test for a very long string input or None if it's allowed
        long_input = "a" * 10000
        result = hello.say_hello(long_input)
        self.assertTrue(result.startswith("Hello,"))
    
    def test_say_hello_type_error(self):
        """Test that passing a non-string type (e.g., integer) to the function raises a TypeError."""
        with self.assertRaises(TypeError):
            hello.say_hello(12345)
    
    def test_say_hello_output_format(self):
        """Test the format of the returned message (if it includes dynamic content)."""
        name = "Jenkins"
        result = hello.say_hello(name)
        self.assertTrue(result.startswith("Hello,"))  # Verify it starts with 'Hello,'
        self.assertIn(name, result)  # Verify the name is included in the greeting
    
    def test_functionality_under_load(self):
        """Test the functionality under load (e.g., calling say_hello multiple times)."""
        for i in range(1000):  # Call the function 1000 times
            result = hello.say_hello(f"Test {i}")
            self.assertEqual(result, f"Hello, Test {i}!")

    def test_no_output(self):
        """Test that nothing is output to the console unless expected."""
        result = hello.say_hello("No Output Test")
        self.assertIsNotNone(result)  # Ensures that result is not None
        self.assertNotIn("error", result.lower())  # Ensure no error in output

if __name__ == '__main__':
    unittest.main()

