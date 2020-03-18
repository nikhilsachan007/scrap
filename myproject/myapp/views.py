from django.shortcuts import render,redirect
from myapp.scraping.main import scrap
from myapp.scraping.showinfourl import showinfourl
from myapp.forms import StudentsForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from myapp.models import Students
from django.shortcuts import HttpResponseRedirect

@login_required(login_url='/login/')
def std(request):
 
    if request.method == "POST": 
         form=StudentsForm(request.POST)

         
         if form.is_valid():
            try:
             studid = form.cleaned_data['keywords']
             studf = form.cleaned_data['Size']
             studl = form.cleaned_data['max_urls'] 
             form.save()  

             scrap(studid,studf,studl)
             return redirect('/view')
            except:
                    pass
    else:
          form=StudentsForm()    
    return render(request,'index.html',{'form':form})  

@login_required(login_url='/login/')
def urlstd(request):
    if request.method == "POST": 
         form=StudentsForm(request.POST)
         print("url")
         if form.is_valid():
            try:  
             
             url= form.cleaned_data['keywords']
            
             
             form.save()  
             showinfourl(url)
             return redirect('/view')
            except:
                    pass
    else:
          form=StudentsForm()    
    return render(request,'index.html',{'form':form}) 



@login_required(login_url='/login/')
def view(request):
    students=Students.objects.all()
    return render(request,'view.html',{'students':students})

@login_required(login_url='/login/')
def delete(request,id):
    students=Students.objects.get(id=id)
    students.delete()
    return redirect('/view')

@login_required(login_url='/login/')
def edit(request,id):
    students=Students.objects.get(id=id)
    return render(request,'edit.html',{'students':students})
    
@login_required(login_url='/login/')
def update(request, id):  
    students = Students.objects.get(id=id)  
    form = StudentsForm(request.POST, instance = students)  
    if form.is_valid(): 
        form.save()  
        return redirect("/view")  
    return render(request,'edit.html',{'students': students})  





