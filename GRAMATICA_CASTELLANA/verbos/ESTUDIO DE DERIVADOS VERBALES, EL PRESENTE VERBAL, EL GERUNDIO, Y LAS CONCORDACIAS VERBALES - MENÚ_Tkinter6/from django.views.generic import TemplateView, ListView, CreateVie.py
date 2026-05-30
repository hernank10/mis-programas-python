# numeros/views.py
from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy
from .models import NumeralExample
from django.shortcuts import redirect
import random

class HomeView(TemplateView):
    template_name = 'numeros/home.html'

class TheoryView(TemplateView):
    template_name = 'numeros/theory.html'

class PracticeView(TemplateView):
    template_name = 'numeros/practice.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        examples = list(NumeralExample.objects.all())
        random.shuffle(examples)
        self.request.session['practice_queue'] = [e.id for e in examples]
        self.request.session['practice_score'] = 0
        self.request.session['current_practice'] = 0
        return context

class QuizView(TemplateView):
    template_name = 'numeros/quiz.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        questions = list(NumeralExample.objects.all())
        random.shuffle(questions)
        self.request.session['quiz_questions'] = [q.id for q in questions[:10]]
        self.request.session['quiz_score'] = 0
        self.request.session['current_question'] = 0
        return context

class ExampleCreateView(CreateView):
    model = NumeralExample
    fields = ['phrase', 'answer', 'category']
    template_name = 'numeros/example_form.html'
    success_url = reverse_lazy('examples_list')
    
    def form_valid(self, form):
        form.instance.is_custom = True
        return super().form_valid(form)

class ExampleListView(ListView):
    model = NumeralExample
    template_name = 'numeros/examples_list.html'
    paginate_by = 10
