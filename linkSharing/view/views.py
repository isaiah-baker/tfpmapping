from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from view.models import Link


from .models import Link

# Create your views here.
def index(request):
    # model = Link
    # links = Link.objects.all()
    # def fetchLinks(id):
    id = User.id
    link_list = Link.objects.all()
    # link_list = Link.objects.get(id = User.id)
    
    # output = ', '.join([l.link_text for l in links])
    # user.entry_set.all()
    context = {'link_list': link_list}
    return render(request, 'view/view.html', context)
    # return HttpResponse(output)
    # links = Link.objects.filter
    # return render(request, 'polls/view.html, {links: 'links'})
    # return HttpResponse('link index')
    # return render(request, 'view/view.html',{'links': links} )

# class LinkList(ListView):
#     model = Link

# class LinkDetail(DetailView):

#     model = Link

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['link_list'] = Link.objects.all()
#         return context






# class LinkList(ListView):
#     model = Link