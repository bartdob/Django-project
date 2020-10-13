from django.shortcuts import render

def calc(request):
    # return render (request, 'calc/calc.html')
    if(request.POST.get('btn1')):
        print('Button clicked')
        return render(request, 'calc/calc.html',{'val':100})
    else: return render(request, 'calc/calc.html',{'val':0})