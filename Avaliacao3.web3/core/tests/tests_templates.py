from django.test import TestCase
class FeriadoTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

    def test_texto(self):
        self.assertContains(self.resp, 'feriado')

    def test_template_used():
        # import pipdb; ipdb.set_trace()
        self.assertTemplateUsed(self.resp, 'index.html')
        # o template usado é este?