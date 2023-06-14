from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
# from .models import pets
from django.db.models import Q
from .forms import EmployeeForm
from .models import Employee

# Create your views here
#def index(request):
   #content={}
   #content['l']=[10,20,30,40,50]
   #content['t']=(1,2,3,4,5,'it-vedant')
   #content['s']={1,2,4,5}
   #content['y']=60
   #return render(request,'index.html',content)
   
#    form=''' 
#     <html>
#  <head>
#  <title>my Form</title>
#  </head>
# # <body>
# # <form method="">
# # <table>
# # <tr>
# # <td>Heading</td>
# # <td><input type'"test" name="bhead"></td>
# # </tr>
# # <tr>
# # <td>catagory</td>
# # <td><input type'"test" name="bcat"></td>
# # </tr>
# # <tr>
# # <td><input type'"submit" name="bcat"></td>
# # <tr>

# # </table>
# # <button> Submit</button>
# # </form>
# # </body>
# # </html>
#    '''
#    #return HttpResponse(form )
  
        
# #class Home(View):
#     # def get(self,request):
#     #     return HttpResponse("todays day is good")

# #def home(request):
#     #x=20
#     #content="value of x is :{}".format(x)
#     #return HttpResponse(content)
# #def user(request,user):
#     #content="<h1>Hello:{}</h1>".format(user)
#     #return HttpResponse(content)
# #def contact(request):
#     #return render(request,'contact.html')
# #def placement(request):
#     #return render(request,'placement.html')
# def my_views(request):
#     products=[
#         {
#             'id':1,
#             'name':'pet food',
#             'description':'delicious and nutrious pet food',
#             'price':10
#         },
#         {
#             'id':2,
#             'name':'tommy',
#             'description':'its is looking good',
#             'price':40
#         }
#     ]
#     return render(request,'main.html',{'products':products})
# #def product_details(request,product_id):
#     #products=[
#         #{
#             #'id':1,
#             #'name':'pet food',
#             #'description':'delicious and nutrious pet food',
#             #'price':10
#         #},
#         #{
#             #'id':2,
#             #'name':'tommy',
#             #'description':'its is looking good',
#             #'price':40
#         #}
#     #]
#     #product=next((p for p in products if p['id']==product_id),None)
#     #if product is None:
#         #return render(request,'product_not_found.html')
#     #return render(request,'product_detail.html',{'product':product})
#import datetime
# def index(request):
#     content={}
#     content['name']='itvedant'
#     return render(request,'index.html',content)
# def index(request):
#     content={}
#     now=datetime.datetime.now()
#     content['name']='itvedant_class'
#     content['cdt']=now
#     return render(request,'index.html',content)
# def getform(request):
#     return render(request,'form.html')
# def formsubmit(request):
#     mn=request.POST['mn']
#     fd=request.POST['feedback']
#     content={'m':mn,'f':fd}
#     return render(request,'contact.html',content)
# 

def employee_form(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee_form.html', {'form': form})

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})