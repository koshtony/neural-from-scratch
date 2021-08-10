#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 12:07:36 2021

@author: kosh
"""

import unittest
from neural import initialize,activate,transfer
class TestNeural(unittest.TestCase):
    def test_initialize(self):
        self.assertEqual(len(initialize(2,1,2)),2)
    def test_activation(self):
        self.assertGreaterEqual(activate([0.2,0.3],[0,1]), 0)
        self.assertLessEqual(activate([0.2,0.3],[0,1]), 1)
    def test_transfer(self):
        self.assertGreaterEqual(transfer(0.5),0)
        self.assertLessEqual(transfer(0.5),1)
if __name__=="__main__":
    unittest.main()