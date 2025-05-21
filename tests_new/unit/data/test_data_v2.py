import pytest
from tests_new.base_test import BaseTest
import numpy as np

class TestDataV2(BaseTest):
    def test_data_loading(self):
        """Test data loading"""
        data = self.get_test_data(100)
        assert len(data) == 100

    def test_data_preprocessing(self):
        """Test data preprocessing"""
        data = self.get_test_data(100)
        assert isinstance(data, np.ndarray)
