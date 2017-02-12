from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Category, Carts
# Create your views here.


class CategoryView(ListView):
    model = Category
    template_name = 'category_list.html'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail_list.html'


    def get_context_data(self,  **kwargs):
            context = super().get_context_data(**kwargs)
            # Add in a QuerySet of all the books
            context['obj'] = self.get_object()
            context['category_list'] = Carts.objects.filter(cart__category=self.get_object().name)
            return context
