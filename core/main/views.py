from django.views.generic import TemplateView
from django.shortcuts import render
from .models import *
from .forms import *

class HomeListView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self._extract_all_data())
        context['form'] = BookingForm()
        return context
    
    def _extract_all_data(self):
        intro = HomePage.objects.get()
        story = MyStory.objects.get()
        prom = Promo.objects.get()
        order = Services.objects.all()
        price = PriceList.objects.all()
        contact = ContactUs.objects.get()
        context = {
            'intro': intro,
            'story': story,
            'prom': prom,
            'order': order,
            'price': price,
            'contact': contact,
        }
        return context

    def post(self, request):
        form = BookingForm(request.POST)

        if form.is_valid():
            form.save()
        else:
            context = self._extract_all_data()
            context['form'] = BookingForm()
        
        return render(request , self.template_name , context)