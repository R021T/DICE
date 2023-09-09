from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render(request,'base.html')

def roll(request):
    lx={1:0,2:-90,3:0,4:0,5:90,6:180}
    ly={1:0,2:0,3:90,4:-90,5:0,6:0}
    n=random.randrange(1,7)
    return render(request,'roll.html',{'x':lx[n],'y':ly[n],'a':lx[n]+360,'b':ly[n]+360})
