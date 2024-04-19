from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.
def home(request):
    records = Record.objects.all()
    
    
    #Check if user is authenticated
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        #Autenticação
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Login realizado com sucesso")
            return redirect('home')
        
        else:  
            messages.success(request, "Usuário ou senha inválidos. Tente novamente.")
            return redirect('home')              
    
    return render(request, 'home.html', {'records': records})

def logout_user(request):
    logout(request)
    messages.success(request, "Logout realizado com sucesso")
    
    return redirect('home')     

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            #Authenticate and Login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Conta criada para  {username} . Bem vindo!')
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    
    return render(request, 'register.html', {'form': form})

def costumer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    
    else:
        messages.success(request, "Você precisa estar logado para acessar essa página")
        return redirect('home')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        record.delete()
        messages.success(request, "Registro deletado com sucesso")
        return redirect('home')
    
    else:
        messages.success(request, "Você precisa estar logado para acessar essa página")
        return redirect('home')
    
def add_record(request):
    form = AddRecordForm(request.POST or None)
    
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save() 
                messages.success(request, "Registro adicionado com sucesso")           
                return redirect('home')
        else:
            return render(request, 'add_record.html', {'form': form})
    else:
        messages.success(request, "Você precisa estar logado para acessar essa página")
        return redirect('home')
    
def update_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=record)
        
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, "Registro atualizado com sucesso")
                return redirect('home')
        else:
            return render(request, 'update_record.html', {'form': form})
    else:
        messages.success(request, "Você precisa estar logado para acessar essa página")
        return redirect('home')