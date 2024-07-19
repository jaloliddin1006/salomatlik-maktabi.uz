from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.views.generic import ListView, TemplateView
from apps.home.forms import ContactForm, SubscribeForm
from django.contrib import messages
from apps.resources.models import Resource, ResourceType
from apps.home.models import Favourite
# Create your views here.
from django.db.models import Q 
from django.core.paginator import Paginator


class HomePageView(View):
    def get(self, request):
        return render(request, 'home.html')
    
    
class ContactPage(View):
    def get(self, request):
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'contact.html', context)
    
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message sent successfully')
            return redirect('home:index')
        
        context = {
            'form': form
        }
        messages.error(request, f'Message not sent: {form.errors}')
        return render(request, 'contact.html', context)

class SubscribeView(View):
   
    def post(self, request):
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Siz muvaffaqiyatli obuna bo\'ldingiz')
            return redirect('home:index')
        
        context = {
            'form': form
        }
        messages.error(request, 'Siz obuna bo\'la olmadingiz iltimos qaytadan urinib ko\'ring')
        return redirect('home:index')
       
    

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from .models import Resource

class AddOrRemoveFavourite(APIView):
    def post(self, request):
        if not request.user.is_authenticated:
            return Response({'error': 'You must be logged in to add to favourites'}, status=status.HTTP_401_UNAUTHORIZED)
        
        resource_id = request.data.get('resource_id')
        print(resource_id)
        if not resource_id:
            return Response({'error': 'Resource ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        resource = get_object_or_404(Resource, id=resource_id)
        print(resource)
        if not resource:
            return Response({'error': 'Resource not found'}, status=status.HTTP_404_NOT_FOUND)
        
        if request.user.favourites.filter(resource=resource).exists():
            request.user.favourites.filter(resource=resource).delete()
            print('deleted')
            return Response({'message': 'Resource removed from favourites', 'isFavourite': False}, status=status.HTTP_200_OK)
        
        request.user.favourites.create(resource=resource)
        print('created')
        return Response({'message': 'Resource added to favourites', 'isFavourite': True}, status=status.HTTP_200_OK)
    
    
class MyFavouriteView(ListView):
    model = Favourite
    template_name = 'my_favourite.html'
    context_object_name = 'favourites'
    paginate_by = 8
    PAGINATION_URL = ''
    
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return redirect('accounts:login')
        queryset = self.request.user.favourites.filter(is_active=True)
        

        # Get search query from request.GET (modify as needed)
        search_query = self.request.GET.get('search', '')
        if search_query:
            self.PAGINATION_URL = f'&search={search_query}'  
            queryset = queryset.filter(Q(resource__title__icontains=search_query) | 
                                       Q(resource__description__icontains=search_query) | 
                                       Q(resource__author__icontains=search_query) | 
                                       Q(resource__keywords__icontains=search_query))

        # Add additional filters based on request.GET parameters (modify as needed)
        filter_by_category = self.request.GET.get('category', '')
        if filter_by_category:
            self.PAGINATION_URL += f'&category={filter_by_category}'  
            queryset = queryset.filter(resource__category__slug=filter_by_category)
            
            
        filter_by_type = self.request.GET.get('resourceType', '')
        if filter_by_type:
            self.PAGINATION_URL += f'&resourceType={filter_by_type}'
            queryset = queryset.filter(resource__resource_type=filter_by_type)
            
            
        filter_by_auditoriya = self.request.GET.get('auditoria', '')
        if filter_by_auditoriya:
            self.PAGINATION_URL += f'&auditoria={filter_by_auditoriya}'
            queryset = queryset.filter(aresource__uditoria=filter_by_auditoriya)
            
        return queryset.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resourceTypes'] = ResourceType.objects.all()
        context['search_query'] = self.request.GET.get('search', '')  # Pass search query to template
        context['filter_by_category'] = self.request.GET.get('category', '')  # Pass filter value to template
        context['filter_by_type'] = self.request.GET.get('resourceType', '')  
        context['filter_by_auditoriya'] = self.request.GET.get('auditoria', '') 
        context['pagination_url'] = self.PAGINATION_URL
        
        # Get paginated queryset
        favourites = self.object_list
        paginator = Paginator(favourites, self.paginate_by)
        page_number = self.request.GET.get('page', 1)  # Get current page from GET
        page_obj = paginator.get_page(page_number)

        # Update context with pagination information
        context['page_obj'] = page_obj
        context['is_paginated'] = paginator.num_pages > 1

        favorites = list(self.request.user.favourites.all().values_list('resource_id', flat=True))
        print(favorites)
        context['favorites'] = favorites
        
        return context
    

class PremiumPage(View):

    def get(self, request):
        context = {
        }
        return render(request, 'premium.html', context)