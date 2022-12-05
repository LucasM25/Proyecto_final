from django.shortcuts import render
from App1.modelos import familiar
import datetime

class Familiar_view:

    def autogenerar_listar_familiares(request):
        fm1 = familiar.create("lucas", 25, datetime.date(1997, 3, 20 ))
        fm2 = familiar.create("luana", 25, datetime.date(1997, 3, 20 ))
        fm3 = familiar.create("leandro", 25, datetime.date(1997, 3, 20 ))

        fm1.save()
        fm2.save()
        fm3.save()

        return render(request,"autogenerar_listar_familiares.html",{"familiares": [fm1, fm2, fm3]})
