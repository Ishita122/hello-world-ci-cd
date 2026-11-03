import unittest
from app import hello_world, welcome_message

class TestHelloWorld(unittest.TestCase):
    def test_hello_world_message(self):
        self.assertEqual(
            hello_world(),
            "Hello, DevOps!"
        )

    def test_hello_world_returns_string(self):
        self.assertIsInstance(
            hello_world(),
            str
        )

class TestWelcomeMessage(unittest.TestCase):
    def test_welcome_message_alice(self):
        self.assertEqual(
            welcome_message("Alice"),
            "Welcome to DevOps, Alice!"
        )

    def test_welcome_message_bob(self):
        self.assertEqual(
            welcome_message("Bob"),
            "Welcome to DevOps, Bob!"
        )

    def test_welcome_message_returns_string(self):
        self.assertIsInstance(
            welcome_message("Charlie"),
            str
        )

if __name__ == "__main__":
    unittest.main()
