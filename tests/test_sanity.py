import unittest


class TestSanity(unittest.TestCase):

    def test_can_import_package(self):
        import flask_qrcode

    def test_can_initialize_app_and_extension(self):
        from flask import Flask
        from flask_qrcode import QRcode

        app = Flask(__name__)
        QRcode(app)

    if __name__ == '__main__':
        unittest.main()
