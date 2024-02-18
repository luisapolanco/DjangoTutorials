from audioop import reverse
from django import forms
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View 
from django.views.generic import TemplateView, ListView
from .models import Product 

 

# Create your views here. 

class HomePageView(TemplateView): 
    template_name = 'pages/home.html'  
    
class ContactView(TemplateView): 
    template_name = 'pages/contact.html'  

class AboutPageView(TemplateView): 
    template_name = 'pages/about.html'   

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        context.update({ 
            "title": "About us - Online Store", 
            "subtitle": "About us", 
            "description": "This is an about page ...", 
            "author": "Developed by: Luisa Polanco", 
        }) 
        return context 

class ProductIndexView(View): 
    template_name = 'products/index.html' 

    def get(self, request): 
        viewData = {} 
        viewData["title"] = "Products - Online Store" 
        viewData["subtitle"] =  "List of products" 
        viewData["products"] = Product.objects.all()

        return render(request, self.template_name, viewData)  

class ProductShowView(View): 
    template_name = 'products/show.html'  

    def get(self, request, id): 
        viewData = {} 
        try:                     
            product_id = int(id) 
            product = get_object_or_404(Product, pk=product_id) 
        except (IndexError, ValueError):
            return HttpResponseRedirect('..')

        product = get_object_or_404(Product, pk=product_id)
        viewData["title"] = product.name + " - Online Store" 
        viewData["subtitle"] =  product.name + " - Product information" 
        viewData["product"] = product  

        return render(request, self.template_name, viewData)
    
class ProductListView(ListView): 
    model = Product 
    template_name = 'product_list.html' 
    context_object_name = 'products'  # This will allow you to loop through 'products' in your template  

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        context['title'] = 'Products - Online Store' 
        context['subtitle'] = 'List of products' 
        return context    
    
    
class ProductForm(forms.ModelForm): 
    class Meta: 
        model = Product 
        fields = ['name', 'price'] 


class ProductCreateView(View): 
    template_name = 'products/create.html' 

    def get(self, request): 
        form = ProductForm() 
        viewData = {} 
        viewData["title"] = "Create product" 
        viewData["form"] = form 
        return render(request, self.template_name, viewData)  

    def post(self, request): 
        form = ProductForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            return redirect('/products/succesful/created')  
        else: 
            viewData = {} 
            viewData["title"] = "Create product" 
            viewData["form"] = form 
            return render(request, self.template_name, viewData) 
        
class CreatedView(TemplateView):
    template_name = 'products/createdMessage.html'