from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, AlunoForm
from django.contrib.auth.models import User
from .models import Aluno, Animal, Casa, Varinha

# Create your views here.

def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST': #if the form has been submitted
        form = UserRegistrationForm(request.POST) #form bound with post data
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def area_logada(request):
    return render(request, 'area_logada.html')

class AlunoListView(generic.ListView):
    model = Aluno
    #defaults
    queryset = Aluno.objects.all()
    context_object_name = 'aluno_list'
    template_name = 'aluno/aluno_list.html'
    paginate_by = 10
    
class AlunoDetailView(generic.DetailView):
    model = Aluno
    #defaults
    context_object_name = 'aluno_detail'
    template_name = 'aluno/aluno_detail.html'

class CreateAluno(LoginRequiredMixin, generic.CreateView):
    model = Aluno
    form_class = AlunoForm
    success_url = reverse_lazy('area_logada')
    
    context_object_name = 'aluno_create'
    template_name = 'aluno/aluno_create.html'
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.usuario = self.request.user
        self.object.save()
        
        return HttpResponseRedirect(self.get_success_url())

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CreateAluno, self).get_form_kwargs(*args, **kwargs)
        kwargs['usuario'] = self.request.user
        return kwargs
    
class UpdateAluno(generic.UpdateView):
    model = Aluno
    fields = ['nome', 'casa', 'varinha', 'animal']
    success_url = reverse_lazy('area_logada')
    
    context_object_name = 'aluno_create'
    template_name = 'aluno/aluno_create.html'
    
class DeleteAluno(generic.DeleteView):
    model = Aluno
    template_name = 'aluno/aluno_delete.html'
    success_url = reverse_lazy('area_logada')
    
class CasaDetailView(generic.DetailView):
    model = Casa
    template_name = "area_logada/casa_detail.html"
    context_object_name = 'casa'
