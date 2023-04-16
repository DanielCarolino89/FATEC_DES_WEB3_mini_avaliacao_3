from django.shortcuts import render
# from django.http import HttpResponse
from core.models import FeriadoModel 
from datetime import date

def feriado(request):
	hoje = date.today()
	qs = FeriadoModels.objects.filter(data__day=hoje.day)
	qs = qs.filter(data__month=hoje.month)

	# se o tamanho for igual 0 nao tem feriado
	if len(qs) == 0:
		contexto = {}
		# return render(request, 'index.html')
	else:
		contexto = {'nome': = qs[0].nome}
		# posso usar um unico templete usando o contexto ou um pra cada 
		# return render(request, 'index.html', context)