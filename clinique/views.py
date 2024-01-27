from django.shortcuts import render, redirect, get_object_or_404
from .forms import DemRdvForm, MedecinForm

def DemRdvView(request):
    if request.method == 'POST':
        form = DemRdvForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagesuc')  
    else:
        form = DemRdvForm()

    #return render(request, 'DemRdv.html', {'form': form}) 
    return render(request, 'DemRdv.html', {'form': form})

def successView(request):
    return render(request,'pagesuccess.html')

def medecin_detail(request,medecin_id):
    medecin = get_object_or_404(medecin, pk=medecin_id)
    form = MedecinForm(instance=medecin)

    if request.method == 'POST':
        form = MedecinForm(request.POST, instance=medecin)
        if form.is_valid():
            form.save()
            
    return render(request, 'medecin_detail.html', {'medecin': medecin, 'form': form})
