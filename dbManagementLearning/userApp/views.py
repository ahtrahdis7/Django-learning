from django.shortcuts import render
# from userApp.models import users
# Create your views here.
from userApp.forms import NewUserForm

def home(request):
    return render(request, 'home.html' )


def users(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)


        if form.is_valid():
            form.save(commit = True)

            return home (request)

        else:
            print("ERROR FORM INVALID")

    return render(request, 'users.html', {'form':form})