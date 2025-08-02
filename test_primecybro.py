# test_primecybro.py
"""
Tests for PrimeCybro module.
"""

import unittest
from primecybro import PrimeCybro

class TestPrimeCybro(unittest.TestCase):
    """Test cases for PrimeCybro class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PrimeCybro()
        self.assertIsInstance(instance, PrimeCybro)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PrimeCybro()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
