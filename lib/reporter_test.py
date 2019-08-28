# -*- coding: utf-8 -*-
import pytest
from reporter import Reporter

reporter = Reporter()

def test_start():
    assert reporter.gen_start() == """<html><head><style>.main {width: 50%;margin-left: 25%;margin-right: 25%;margin-top: 0px;margin-bottom: 0px;background-color: #eeeeee;}.main_heading {text-align: center;color: #ff6c4f;}.normal_img {width: 75%;margin-left: 12.5%;margin-right: 12.5%;}.big_img {width: 95%;margin-left: 2.5%;margin-right: 2.5%;}.definition {background-color: #dedede;margin-left: 5px;margin-right: 5px;}.defname {margin: 5px;}.deftext {margin-left: 10px;}.heading {font-size: 125%;color: #ff6c4f;}.text {margin-left: 5px;}body {padding: 0px;margin: 0px;}</style></head><body><div class='main'>"""
