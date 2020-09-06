from django.shortcuts import render, redirect



def home(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            return redirect('teachers:assignment_page')
        else:
            return redirect('main_page')
    return redirect('login')



def main_view(request):
    context = {

    }

    return render(request, 'main.html', context)
