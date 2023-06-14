from django.urls import path
from. import views
from myapp.views import employee_form, employee_list


urlpatterns = [
    #path("index",views.index,name="index"),
    # path("home",views.home,name="home"),
    # path('home/<user>',views.user,name="user")
    # path('contact',views.contact,name='contact'),
    # path('placement',views.placement,name='placement'),
    #path('student',views.my_view,name="student"),
    #path('product',views.my_view,name="product"),
    #path('products/<int:product_id>/',views.product_details)
    # path('students</int:student_id/>',views.student_detali,name='student_detail')
   #path('',views.my_views,name="main"),
#path('products/<int:product_id>/',views.product_details,name="product_details")
    #path('tapaswini',views.tapaswini,name='tapaswini'),
    # path('form',views.getform,name='form'),
    # path('formsubmit',views.formsubmit,name='formsubmit'),
    # path('course',views.courseform,name="course"),
    # path('create_course',views.create_course,name='create_course'),
    # path('',views.get_course,name="get_course"),
    # path('delete/<rid>',views.delete,name="delete"),
    # path('edit/<rid>',views.edit,name="edit"),
    # path('filter_records',views.filter_records,name='filter_records')
    # path('',views.home,name="Home"),
    # path('about',views.about,name='about'),
    # path('set_cookie',views.set_cookie,name="set_cookie"),
    # path('get_cookie',views.get_cookie,name='get_cookie'),
    path('employee-form',views. employee_form, name='employee_form'),
    path('employee-list',views. employee_list, name='employee_list'),

    #path('astrology',views.astrology, name='astrology')

]
