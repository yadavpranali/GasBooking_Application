from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from templates.form import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout

# Create your views here.
def base(request):
    return render(request,'index.html')



def home(request):

    return render(request,'home.html')




@login_required
def connection(request):
    if request.method == "POST":
        form = ConnectionForm(request.POST)
        if form.is_valid():
            connections = Connection(
                user = request.user,
                name = request.POST['name'],
                email = request.POST['email'],
                mobilenumber = request.POST['mobilenumber'],
                gender = request.POST['gender'],
                marriedstatus = request.POST['marriedstatus'],
                adharno = request.POST['adharno'],
                address = request.POST['address'],
                
                zipcode = request.POST['zipcode'],
            )
            connections.save()
            context={}
            context['success']="Connection Addedd Successfully"
            return render(request,'connection.html',context)
    else:
        form=ConnectionForm
        connection=Connection.objects.filter(user=request.user.id)
        context={'connection':connection,'form':form}
        return render(request,'connection.html',context)
    
@login_required
def bookcylinder(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            bookc =BookGas(
                user=request.user,
                cylinder_KG=request.POST['cylinder_KG'],
                
            )
            bookc.save()
            context={}
            context['success']="Cylinder Booked successfully !!!"
            return render(request,'book.html',context)
        
    else:
        form = BookForm()
        bookc = BookGas.objects.filter(user=request.user.id)
        context= {'bookc':bookc,'form':form}
        return render(request,'book.html',context)
    
'''
def connection(request):
    return render(request,'connection.html')
'''
'''
def boookhistory(request):
    bookc = Bookc.objects.filter(user=request.user.id)
    context={
        'bookc':bookc
    }
    return render(request,'bookhistory.html',context)

'''
@login_required
def bookinghistory(request):
    bookc = BookGas.objects.filter(user=request.user.id)
    context = {
        'bookc': bookc
    }
    return render(request,'allbookings.html',context)


'''
def display_bookings(request):
    # Retrieve all BookGas objects
    bookings = BookGas.objects.all()

    # Pass the bookings to the template
    return render(request, 'allbookings.html', {'bookings': bookings})
'''
@login_required
def delete_booking(request,pk=None):
    BookGas.objects.get(id=pk).delete()
    return redirect('bookhistory')
    
@login_required
def  book_cylinder_view(request,pk=None):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            user=request.user
            connection=Connection.objects.get(id=pk)
            BookGas.objects.create(
                user=user,
                connection=connection,
                cylinder_KG=form.cleaned_data['cylinder_KG'],
                
                

            )
            return redirect ('bookhistory')
    else:
        form=BookForm()
        return render(request,'book.html',{'form':form})


@login_required
def connectioninfo(request):
    connections = Connection.objects.filter(user=request.user.id)
    context = {
        'connections': connections
    }
    return render(request,'connectioninfo.html',context)

def delete_connection(request,pk=None):
    Connection.objects.get(id=pk).delete()
    return redirect('connectioninfo')

@login_required
def update_connection(request, rid):
    
    connection = get_object_or_404(Connection, id=rid)
    
    if request.method == "POST":
        form = ConnectionForm(request.POST, instance=connection)
        if form.is_valid():
            form.save()
            context = {'success': "Connection updated successfully."}
            return render(request, 'connection.html', context)
    else:
        form = ConnectionForm(instance=connection)

    context = {'form': form, 'connection': connection}
    return render(request, 'connection.html', context)

            
            
'''

def get_connection_details(user):
    # Query the Connection model to get relevant details for the user
    connection = Connection.objects.filter(user=user).first()  # Assuming one Connection per user
    if connection:
        return {
            'name': connection.name,
            'mobilenumber': connection.mobilenumber,
            'id': connection.id,
            'email': connection.email,
        }
    return None
    '''
'''

def display_bookgas_records(request):
    # Query all BookGas records
    bookgas_records = BookGas.objects.all()

    # Render the HTML template with the bookgas_records
    return render(request, 'bookgas.html', {'bookgas_records': bookgas_records})

'''




'''

def update_connection(request,rid):
    if request.method == "GET":
        form = ConnectionForm()
        connections = Connection.objects.filter(id=rid)
        context= {'connections':connections,'form':form}
        return render(request,'connection.html',context)
    else:
        form = ConnectionForm(request.POST)
        if form.is_valid():
            connections = Connection(
                user = request.user,
                name = request.POST['name'],
                email = request.POST['email'],
                mobilenumber = request.POST['mobilenumber'],
                gender = request.POST['gender'],
                marriedstatus = request.POST['marriedstatus'],
                adharno = request.POST['adharno'],
                address = request.POST['address'],
                
                zipcode = request.POST['zipcode'],
            )
            connections.save()
            context={}
            context['success']="Connection Addedd Successfully"
            return render(request,'connection.html',context)

    

    context={}
    if request.method == "GET":
        connection=Connection.objects.filter(id=rid)
        context['connections']=connection
        return render(request,'connection.html',context)

        '''


'''
    else:
        form = ConnectionForm(request.POST)
        if form.is_valid():
            connections = Connection(
                user = request.user,
                name = request.POST['name'],
                email = request.POST['email'],
                mobilenumber = request.POST['mobilenumber'],
                gender = request.POST['gender'],
                marriedstatus = request.POST['marriedstatus'],
                adharno = request.POST['adharno'],
                address = request.POST['address'],
                applieddate = request.POST['applieddate'],
                zipcode = request.POST['zipcode'],
            )
            connections.save()
            
            context['success']="Connection Addedd Successfully"
            return render(request,'connection.html',context)
            ''' '''
        cname = request.POST['name']
        cemail = request.POST['email']
        cmobilenumber = request.POST['mobilenumber']
        cgender = request.POST['gender']
        cmarriedstatus = request.POST['marriedstatus']
        cadharno = request.POST['adharno']
        caddress = request.POST['address']
        capplieddate = request.POST['applieddate']
        czipcode = request.POST['zipcode']
        connection=Connection.objects.filter(id=rid)
        connection.update(name=cname,email=cemail,mobilenumber=cmobilenumber,gender=cgender,
                          marriedstatus=cmarriedstatus,adharno=cadharno,address=caddress,
                          applieddate=capplieddate,zipcode=czipcode)
        return redirect('connectioninfo')
 
     '''

'''

def login(request):
    if request.method == 'GET':
        return render(request, "login.html")
    else:
        un = request.POST['']

        '''


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid:
            form.save()
            username=form.cleaned_data.get('username')
            return redirect ('login')
    else:
        form=UserRegistrationForm()
        context = {
            'form':form
        }
        return render(request,'register.html',context)

