#!flask/bin/python

import unittest
import os
from app import app

class BasicTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_main_page(self):
        response = self.app.get('/api/v1.0/manual', content_type='html/text')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
  unittest.main()
