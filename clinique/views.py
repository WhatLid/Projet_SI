from django.shortcuts import render, redirect
from .forms import DemRdvForm 

def DemRdvView(request):
    if request.method == 'POST':
        form = DemRdvForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('page_succes')  
    else:
        form = DemRdvForm()

    return render(request, 'DemRdv.html', {'form': form})
