
# Teste para o modelo
from django.test import TestCase
from core.models import FeriadoModel
import datetime import date

class feriadoModelTest(TestCase):
    def setUp(self):
    self.cadastro = FeriadoModel(
    nome= 'hoje',
    data= date.today())
    self.cadastro.save()

   def test_created(self):
    self.assertTrue(FeriadoModel.objects.exists())