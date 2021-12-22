import unittest
import sys, os
from unittest.main import main
from unittest.mock import patch, Mock

import Builder
sys.path.append(os.getcwd())
from Builder import *


class Test_builder(unittest.TestCase):
    @patch.object(builder.Director, 'TurboCar')
    def test_turbocar(self, mock_turbocar):
        mock_turbocar.return_value = None

        director = Director()
        builder = CarBuilder()
        director.builder = builder

        self.assertEqual(director.TurboCar(), None)
if __name__ == "__main__":
    unittest.main()     