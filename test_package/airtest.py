# -*- encoding=utf8 -*-
__author__ = "yorel"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["Android:///",])

    wake()
    
    start_app("com.apowersoft.mirror")
    
    from poco.drivers.android.uiautomation import AndroidUiautomationPoco
    poco = AndroidUiautomationPoco()
    poco('com.apowersoft.mirror:id/tv_tab_cloud').click()
    
    stop_app("com.apowersoft.mirror")
    

# script content
print("end..")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)