from django.shortcuts import render

def profile_view(request):
    context = {

    }

    return render(request, 'profile.html', context)
