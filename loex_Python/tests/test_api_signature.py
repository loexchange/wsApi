import unittest
import loex
from unittest import mock
from loex.utils import *



class TestApi(unittest.TestCase):
    def test_request(self):
        builder = UrlParamsBuilder()
        loex.utils.api_signature.utc_now = mock.Mock(return_value="123")
        create_signature("123", "456", "",  "", builder)
        self.assertEqual("?AccessKeyId=123&SignatureVersion=2&SignatureMethod=HmacSHA256&Timestamp=123&Signature=Hhiaq8xYQPiBZOyWV37MdQutLo4f0ZOHiJtG3p%2BnILc%3D", builder.build_url())
        return


if __name__ == "__main__":
    unittest.main()