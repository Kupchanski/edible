from django.db.models import Q
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Category, Carts
from .forms import NewCartForm, UpdateCartForm
# Create your views here.


class CategoryView(ListView):
    model = Category
    template_name = 'category_list.html'

class CartsView(ListView):
    model = Carts
    queryset = Carts.objects.all()
    template_name = 'carts_list.html'


    def get_queryset(self, *args, **kwargs):
        qs = super(CartsView, self).get_queryset(*args, **kwargs)
        query = self.request.GET.get('q')
        if query:
            print(query)
            qs = self.model.objects.filter(
                Q(title__icontains=query) |
                Q(place__icontains=query) |
                Q(comment__icontains=query)
            )
        return qs

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail_list.html'

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['obj'] = self.get_object()
            context['category_list'] = Carts.objects.filter(category__name=context['obj'].name)
            # context['cart'] = Carts.objects.filter(category__name=context['obj'].name, title=title)
            return context


class CartsDetailView(DetailView):
    model = Carts
    template_name = 'cart_detail_list.html'

    def get_context_data(self,  **kwargs):
            context = super().get_context_data(**kwargs)
            # Add in a QuerySet of all the books
            context['cart_obj'] = self.get_object()
            return context


def add_to_red_cart(request):
    form = NewCartForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.color = "red"
        instance.save()
        return redirect('carts')
    color = "красную"
    context = {
        "form": form,
        "color": color
    }
    return render(request, "add_cart_form.html", context)


def add_to_green_cart(request):
    form = NewCartForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.cart_color = "Green"
        instance.save()
        return redirect('carts')
    color = "зеленую"
    context = {
        "form": form,
        "color": color
    }
    return render(request, "add_cart_form.html", context)

def cart_update_view(request, category_slug= None, pk=None):
    cart = get_object_or_404(Carts, id=pk, category__slug=category_slug)
    form = UpdateCartForm(request.POST or None, request.FILES or None, instance=cart)
    context = {
        'form': form,
    }
    if form.is_valid():
        form.save()
        return redirect('carts_detail', cart.category.slug, cart.id)
    return render(request,  "add_cart_form.html", context)