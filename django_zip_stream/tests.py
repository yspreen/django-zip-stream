""" Tests for the TransferZipResponse. """
from django.http import Http404
import django.test

from django_zip_stream import TransferZipResponse


class TransferZipResponseTestCase(django.test.TestCase):
    """ Tests TransferZipResponse. """

    def test_zip_single_file(self):
        """ Test creating a zip for a single file. """
        request = django.test.RequestFactory().get('/fake-url')
        filename = __file__
        files = [("/chicago.jpg", "/home/django/chicago.jpg", 4096), ]
        response = TransferZipResponse(filename, files)
        self.assertTrue(isinstance(response, TransferZipResponse))
        self.assertEqual(response['X-Archive-Files'], 'zip')
        self.assertEqual(response['Content-Type'], 'application/zip')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content,
                         b"- /chicago.jpg /home/django/chicago.jpg 4096")

    def test_zip_multiple_files(self):
        """ Test creating a zip for multiple files. """
        request = django.test.RequestFactory().get('/fake-url')
        filename = __file__
        files = [("/chicago.jpg", "/home/django/chicago.jpg", 4096),
                 ("/portland.jpg", "/home/django/portland.jpg", 4096), ]
        response = TransferZipResponse(filename, files)
        self.assertTrue(isinstance(response, TransferZipResponse))
        self.assertEqual(response['X-Archive-Files'], 'zip')
        self.assertEqual(response['Content-Type'], 'application/zip')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content,
                         b"- /chicago.jpg /home/django/chicago.jpg 4096\n"
                         b"- /portland.jpg /home/django/portland.jpg 4096")
