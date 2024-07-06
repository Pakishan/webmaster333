
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def registro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirige a una página de éxito, por ejemplo
            return redirect('registro_exitoso')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registro.html', {'form': form})
