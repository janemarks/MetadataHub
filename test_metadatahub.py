# test_metadatahub.py
"""
Tests for MetadataHub module.
"""

import unittest
from metadatahub import MetadataHub

class TestMetadataHub(unittest.TestCase):
    """Test cases for MetadataHub class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MetadataHub()
        self.assertIsInstance(instance, MetadataHub)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MetadataHub()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
