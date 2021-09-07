#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 14:24:15 2021

@author: shaoxiong
"""
from primelib import is_prime

def test_false():
    assert is_prime(10) is False

def test_true():
    assert is_prime(11) is True