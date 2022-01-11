from django.test import TestCase
from django.core import mail


class FirstViewsTestCase(TestCase):

    def test_index_page(self):
        response = self.client.get('')
        self.assertContains(response, 'Hello, Mountains!!!')

    def test_page_email_sending(self):
        mail.send_mail('Subject here',
                       'Here is the message.',
                       'from@example.com',
                       ['to@example.com'],
                       fail_silently=False,)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject,
                         'Subject here')
