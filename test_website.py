import unittest
from unittest.mock import patch, Mock
from server import Server


class TestServer(unittest.TestCase):

    def setUp(self):
        self.server = Server(logfile="test.log")
        
    def tearDown(self):
        pass
        
            

    def test_sign_in(self):
        with patch("server.render_template") as mock_render_template:
            response = self.server.sign_in()
            self.assertIsNotNone(response)
            self.assertTrue(mock_render_template.called)
            
    def test_sign_up(self):
        with patch("server.render_template") as mock_render_template:
            response = self.server.sign_up()
            self.assertIsNotNone(response)
            self.assertTrue(mock_render_template.called)
            
    def test_upload(self):
        with patch("server.render_template") as mock_render_template:
            response = self.server.upload()
            self.assertIsNotNone(response)
            self.assertTrue(mock_render_template.called)
            
    def test_coral_info(self):
        with patch("server.render_template") as mock_render_template:
            response = self.server.coral_info()
            self.assertIsNotNone(response)
            self.assertTrue(mock_render_template.called)
            
