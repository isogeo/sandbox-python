# -*- coding: UTF-8 -*-
#! python3

# ############################################################################
# ########## Libraries #############
# ##################################

# ##### Standards ##################
import json
import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(r"./"))
sys.path.insert(0, os.path.abspath(r"./isogeo_search_engine"))

# ##### Modules ####################

from isogeo_search_engine import IsogeoAPI


class IsogeoAPITest(unittest.TestCase):

    # standard methods
    def setUp(self):
        """ Fixtures prepared before each test."""
        self.isogeo = IsogeoAPI()
        self.api_response_sample = os.path.normpath(
            r"tests/fixtures/api_basic_response.json"
        )

        with open(self.api_response_sample, "r") as f:
            search = json.loads(f.read())

        self.ref_tags = search.get("tags")
        self.ref_total = search.get("total")
        pass

    def tearDown(self):
        """Executed after each test."""
        pass

    def test_request_maker_parameters(self):
        self.assertRaises(TypeError, self.isogeo.request_maker, "")
        self.assertRaises(TypeError, self.isogeo.request_maker, 1, 0)

    def test_request_maker_result(self):
        init_request = self.isogeo.request_maker()

        basic_request = self.isogeo.request_maker(
            filter_request=True, filter_query="type:service"
        )

        self.assertDictEqual(init_request[0], self.ref_tags)
        self.assertEqual(init_request[1], self.ref_total)

        self.assertDictContainsSubset(basic_request[0]["types"], self.ref_tags["types"])
        self.assertGreater(self.ref_total, basic_request[1])

    def test_request_maker_type_result(self):
        self.assertIsInstance(self.isogeo.request_maker(), tuple)
        self.assertIsInstance(self.isogeo.request_maker()[0], dict)
        self.assertIsInstance(self.isogeo.request_maker()[1], int)


if __name__ == "__main__":
    unittest.main()
