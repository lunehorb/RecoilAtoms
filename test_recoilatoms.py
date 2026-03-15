# test_recoilatoms.py
"""
Tests for RecoilAtoms module.
"""

import unittest
from recoilatoms import RecoilAtoms

class TestRecoilAtoms(unittest.TestCase):
    """Test cases for RecoilAtoms class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RecoilAtoms()
        self.assertIsInstance(instance, RecoilAtoms)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RecoilAtoms()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
