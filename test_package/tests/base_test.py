# Copyright 2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
# http://aws.amazon.com/apache2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.

import unittest
from airtest.core.api import *
from airtest.cli.parser import cli_setup


class BaseTest(unittest.TestCase):
    """Basis for all tests."""
    def setUp(self):
        print("end..")

    def tearDown(self):
        print("end..")

    def get_name(self):
        print("end..")

    def navigate_to_page(self):
        print("end..")
