from .. import TAGGERS
from .base_tagger import BaseTagger
import numpy as np
import bisect


@TAGGERS.register_module
class searchfork(BaseTagger):
    supported_cam_ids = ["cam0", "cam1"]

    def __init__(self, iou=0.15):
        #self.non_cccc = ["double_yellow", "double_white", "solid_dash", "single_solid", "road_curb_edge", "solid_slow", "obstacle"]
        self.candidate = ['fork']
    def _pred_json_schema_check(self, pred_json):
        input_check = True
        if 'LLD' not in pred_json:
            input_check = False
        #elif 'SOD' not in pred_json:
        #    input_check = False
        return input_check

    def _process(self, pred_json):
        tag = False
        #lld_json, sod_json = pred_json["LLD"], pred_json["SOD"]
        lld_json = pred_json["LLD"]
        
        if lld_json["global"][0] == "fork":
            return True

        return tag