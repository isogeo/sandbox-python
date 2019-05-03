# -*- coding: UTF-8 -*-
#! python3

# ############################################################################
# ########## Libraries #############
# ##################################

# ##### Standards ##################
import sys
import os
import unittest
import random

sys.path.insert(0, os.path.abspath(r"./"))
sys.path.insert(0, os.path.abspath(r"./isogeo_search_engine"))

# ##### Modules ####################

from isogeo_search_engine import IsogeoSearchEngine


class IsogeoSearchEngineTest(unittest.TestCase):

    # standard methods
    def setUp(self):
        """ Fixtures prepared before each test."""
        self.se_test = IsogeoSearchEngine()
        pass

    def tearDown(self):
        """Executed after each test."""
        self.se_test.filter_output = {
            "providers": "",
            "owners": "",
            "types": "",
            "keywords": "",
            "formats": "",
        }

        self.se_test.field_dict = {
            self.se_test.fourn_frame.cbbox: "providers",
            self.se_test.grpTrav_frame.cbbox: "owners",
            self.se_test.type_frame.cbbox: "types",
            self.se_test.keyW_frame.cbbox: "keywords",
            self.se_test.format_frame.cbbox: "formats",
        }
        pass

    def test_set_result_parameter(self):
        self.assertRaises(TypeError, self.se_test.set_result, "")
        self.assertRaises(TypeError, self.se_test.set_result, 0.5)
        self.assertRaises(TypeError, self.se_test.set_result, [85, "métadonnée"])

    def test_fields_setting_parameter(self):
        param_test = [
            1,
            "t",
            0.5,
            ["t", 0.5],
            {"1": "a", "2": "b"},
            (1, {"1": "a", "2": "b"}),
            ({"1": "a", "2": "b"}, 0.5),
            (["t", 0.5], "t"),
        ]
        self.assertRaises(TypeError, self.se_test.fields_setting, param_test[0])
        self.assertRaises(TypeError, self.se_test.fields_setting, param_test[1])
        self.assertRaises(TypeError, self.se_test.fields_setting, param_test[2])
        self.assertRaises(TypeError, self.se_test.fields_setting, param_test[3])
        self.assertRaises(TypeError, self.se_test.fields_setting, param_test[4])
        self.assertRaises(TypeError, self.se_test.fields_setting, param_test[5])
        self.assertRaises(TypeError, self.se_test.fields_setting, param_test[6])
        self.assertRaises(TypeError, self.se_test.fields_setting, param_test[7])

    def test_set_query(self):
        self.se_test.filter_output["formats"] = "test_value"
        self.se_test.set_query()
        self.assertIn("test_value", self.se_test.query)

    def test_field_updating(self):
        dict_value = self.se_test.init_request[0]
        field_test = random.sample(list(self.se_test.field_dict.keys()), 1)
        field_test_name = self.se_test.field_dict[field_test]
        value_dict_test = dict_value[self.se_test.field_dict[field_test]]
        value_test = random.choice(list(self.se_test.field_dict.keys()))

        field_test.set(str(value_test))

        # field_test.set("WFS")

        self.se_test.cbbox_callback(
            event="< VirtualEvent event x=0 y=0 >", field=field_test
        )

        # field_test.set("WFS")
        # self.se_test.cbbox_callback(event= "< VirtualEvent event x=0 y=0 >", field=self.se_test.format_frame.cbbox)

        self.assertTrue(
            self.se_test.filter_output[field_test_name] == value_dict_test[value_test]
        )

        print(
            "'{}' vs '{}'".format(
                self.se_test.filter_output[field_test_name], value_dict_test[value_test]
            )
        )


if __name__ == "__main__":
    unittest.main()
