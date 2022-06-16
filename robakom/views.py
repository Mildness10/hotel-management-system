from django.shortcuts import redirect, render
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from robakom.forms import HotelSystemForm
from .models import HotelSystem
from django.urls import reverse_lazy


def showform(request):
    form = HotelSystemForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('success')
        
    context = {'form': form}
    
    
    
    return render(request, 'home.html', context)
    
# class HotelSystemview(FormView, TemplateView):
#     model = HotelSystem
#     template_name = 'home.html'
#     success_url = reverse_lazy("success")
#     form_class = HotelSystemForm
    
#     def form_valid(self, form):
#         if form.is_valid():
#             return super().form_valid(form)
        
    
class HotelSystemSuccessView(TemplateView):
    model = HotelSystem
    template_name = 'success.html'