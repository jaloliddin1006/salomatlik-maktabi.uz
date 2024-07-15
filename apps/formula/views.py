from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Formula
import types
import math
# Create your views here.

class FormulaPage(View):
    def get(self, request):
        context = {
            'formulas': Formula.objects.all()
        }
        return render(request, 'formula-list.html', context)
    

class FormulaDetail(View):
    def get(self, request, pk):
        formula = get_object_or_404(Formula, pk=pk)
        other_formulas = Formula.objects.exclude(pk=pk)
        
        context = {
            'formula': formula,
            'formulas': other_formulas
        }
        return render(request, 'formula_detail.html', context)
    
    def post(self, request, pk):
        args = request.POST

        formula = Formula.objects.get(pk=pk)
        code = formula.code
        
        data = dict()
        for i in formula.variables:
            frac, whole = math.modf(float(args.get(i)) )
            if frac == 0:
                data[i] = int(args.get(i))
            else:
                data[i] = float(args.get(i)) 
            # print(i, type(i), data[i], type(data[i]))
            
        # print(data)
        my_namespace = types.SimpleNamespace()
        exec(code,  my_namespace.__dict__)
        res = my_namespace.solution(**data)
        
        context = {
            'formula': formula,
            'result': res,
        }
        return render(request, 'formula_detail.html', context)
        

class CalculateAPI(APIView):
    def post(self, request, id):
        print(request.data)
        args = request.data
        formula = Formula.objects.get(pk=id)
        code = formula.code
        data = dict()
        for i in formula.variables:
            frac, whole = math.modf(float(args.get(i)) )
            if frac == 0:
                data[i] = int(args.get(i))
            else:
                data[i] = float(args.get(i)) 
        my_namespace = types.SimpleNamespace()
        exec(code,  my_namespace.__dict__)
        res = my_namespace.solution(**data)
        return Response({'result': res})
    