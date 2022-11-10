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

from base_test import BaseTest
from airtest.core.api import *
from airtest.cli.parser import cli_setup


class AlertsTest(BaseTest):
    """Container for all alerts page tests."""
    PAGE_NAME = 'Alerts'

    def setUp(self):
        """Set up Appium connection and navigate to image gallery page."""
        print("end..")

    def get_name(self):
        return PAGE_NAME

    def test_alert(self):
        """Clicks alert button, verifies alert text, accepts the alert message."""
        auto_setup(__file__, logdir=True, devices=["Android:///",])

        wake()
        
        start_app("com.apowersoft.mirror")
        
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco()
        poco('com.apowersoft.mirror:id/tv_tab_cloud').click()
        
        stop_app("com.apowersoft.mirror")
        print("end..")
