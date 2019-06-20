from django.shortcuts import render
# users/views.py
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.
#from django.shortcuts import render
from django.http import HttpResponse
from .forms import studentForm

#import pudb; pudb.set_trace()
class SignUp(CreateView):
    form_class = studentForm
    success_url = reverse_lazy('contentuser/index.html')
    template_name = 'register/index.html'
    def POST(self,request):
    	import pudb; pudb.set_trace()
    	print('hello')
    	pass

def register_db(request):
	if request.method=='POST':
		import pudb; pudb.set_trace()
		form = studentForm(request.POST)
		if form.is_valid():
			form.save()
			name = form.cleaned_data['name']
			last_name = form.cleaned_data['last_name']
			print(name,last_name)
			return render(request, 'initpage/index.html')
	else:
		form = studentForm()
		return render(request,'register/index.html',{'form':form})