from django.shortcuts import redirect, render
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
        return render(request, 'formula2.html', context)
    

class FormulaDetail(View):
    def get(self, request, pk):
        formula = Formula.objects.filter(pk=pk)
        if not formula.exists():
            # return render(request, '404.html')
            return redirect('formula:formula')
        
        context = {
            'formula': formula.first()
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
    