#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 12:07:36 2021

@author: kosh
"""

import unittest
from net_n import initialize_net
class TestNet_n(unittest.TestCase):
    def test_initialize_net(self):
        self.assertEqual(len(initialize_net(2,1,2)),2)
if __name__=="__main__":
    unittest.main()