from django.shortcuts import render, get_object_or_404, redirect
from Backend.models import ExpertDb,DiseaseDb,DatasetDB,HomeremedyDb,Chat_Intraction
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Frontend.models import ComplainDb
from django.db import IntegrityError
# Create your views here.
def adminpage(request):
    return render(request, "adminindex.html")
def admin_login(request):
    return render(request,"AdminLogin.html")
def adminlogin(request):
    if request.method == "POST":
        un = request.POST.get('user_name')
        pwd = request.POST.get('pass_word')
        if User.objects.filter(username__contains=un).exists():
            x = authenticate(username=un, password=pwd)
            if x is not None:
                login(request, x)
                request.session['username'] = un
                request.session['password'] = pwd

                # Directly assign the success message to messages dictionary
                messages.success(request, "Login successful")

                return redirect(adminpage)
            else:
                messages.error(request, "Invalid Username or Password")
                return redirect(admin_login)
        else:
            messages.error(request, "Invalid Username or Password")
            return redirect(admin_login)
def admin_logout(request):
    del request.session['username']
    messages.success(request, "Logout successfull")
    return redirect(admin_login)
def expertpage(request):
    return render(request, "admin/Add Expert.html")
def saveexpert(request):
    if request.method == "POST":
        fna = request.POST.get('fname')
        lna = request.POST.get('lname')
        plc = request.POST.get('place')
        ps = request.POST.get('post')
        pn = request.POST.get('pin')
        eml = request.POST.get('email')
        pho = request.POST.get('phone')
        dep = request.POST.get('department')
        use = request.POST.get('username')
        pwd = request.POST.get('password')
        obj_ci=Chat_Intraction(type="Expert")
        obj_ci.save()

        obj = ExpertDb(First_Name=fna, Last_Name =lna, Place=plc, Post=ps, Pin=pn, Email=eml, Phone=pho, Department=dep, UserNaMe=use, PassWoRd=pwd,CI_ID=obj_ci)
        messages.success(request, "Expert added "
                                  "...!")
        obj.save()
        return redirect(expertpage)
def manageexpert(request):
    exp = ExpertDb.objects.all()
    return render(request, 'admin/Add and Manage Expert.html',{'exp':exp})
def editexpert(request,dataid):
    expt = ExpertDb.objects.get(id=dataid)
    return render(request, "admin/Edit Expert.html", {'expt':expt})
def updateexpert(request, dataid):
    if request.method == "POST":
        fna = request.POST.get('fname')
        lna = request.POST.get('lname')
        plc = request.POST.get('place')
        ps = request.POST.get('post')
        pn = request.POST.get('pin')
        eml = request.POST.get('email')
        pho = request.POST.get('phone')
        dep = request.POST.get('department')
        ExpertDb.objects.filter(id=dataid).update(First_Name=fna, Last_Name =lna, Place=plc, Post=ps, Pin=pn, Email=eml, Phone=pho, Department=dep)
        return redirect(manageexpert)
def deleteexpert(request, dataid):
    expt = ExpertDb.objects.filter(id=dataid)
    expt.delete()
    return redirect(manageexpert)

def diseasepage(request):
    return render(request, "admin/Add Disease.html")
def savedisease(request):
    if request.method == "POST":
        dis = request.POST.get('disease')
        obj = DiseaseDb(DName=dis)
        messages.success(request, "Added successfully...!")
        obj.save()
        return redirect(diseasepage)
def managedisease(request):
    dis = DiseaseDb.objects.all()
    return render(request, 'admin/Add and Manage Disease.html',{'dis':dis})
def deletedisease(request, dataid):
    dis = DiseaseDb.objects.filter(id=dataid)
    dis.delete()
    return redirect(managedisease)

def replypage(request,id):
    request.session['cid']=id
    return render(request, 'admin/Reply.html')
def savereply(request):
    if request.method == "POST":
         rep= request.POST.get('reply')
         ob=ComplainDb.objects.get(id=request.session['cid'])
         ob.Reply=rep
         ob.save()
         # obj = ReplyDb(Reply=rep)
         # obj.save()
         return redirect(complaintpage)



def complaintpage(request):
    ob=ComplainDb.objects.all()
    return render(request, 'admin/View complaint.html',{'val':ob})




def blkunblk(request):
    blkexp = ExpertDb.objects.all()
    return render(request, 'admin/Block or Unblock.html', {'blkexp': blkexp})

@csrf_exempt
def toggle_block_status(request, dataid):
    if request.method == 'POST':
        blkexpt = get_object_or_404(ExpertDb, id=dataid)
        blkexpt.is_blocked = not blkexpt.is_blocked
        blkexpt.save()
        return JsonResponse({'status': blkexpt.is_blocked})
    else:
        return JsonResponse({'error': 'Invalid request method'})

@csrf_exempt
def blockexpert(request, dataid):
    if request.method == 'POST':
        blkexpt = get_object_or_404(ExpertDb, id=dataid)
        blkexpt.is_blocked = True
        blkexpt.save()
        return JsonResponse({'status': blkexpt.is_blocked})
    else:
        return JsonResponse({'error': 'Invalid request method'})

@csrf_exempt
def unblockexpert(request, dataid):
    if request.method == 'POST':
        blkexpt = get_object_or_404(ExpertDb, id=dataid)
        blkexpt.is_blocked = False
        blkexpt.save()
        return JsonResponse({'status': blkexpt.is_blocked})
    else:
        return JsonResponse({'error': 'Invalid request method'})
def datasetpage(request):
    return render(request, 'admin/Add Dataset.html')
def savedataset(request):
    if request.method == "POST":
        ques = request.POST.get('question')
        ans = request.POST.get('answer')
        obj = DatasetDB(Question = ques,Answer = ans)
        messages.success(request, "Added successfully...!")
        obj.save()
        return redirect(datasetpage)
def managedataset(request):
    dtst = DatasetDB.objects.all()
    return render(request, 'admin/Add and Manage Dataset.html', {'dtst': dtst})
def deletedataset(request, dataid):
    dtset = DatasetDB.objects.filter(id=dataid)
    dtset.delete()
    return redirect(managedataset)

def homeremedypage(request):
    dis = DiseaseDb.objects.all()
    return render(request,"admin/Add Home remedies.html", {'dis':dis})

def savehomeremedies(request):
    if request.method == "POST":
        dis = request.POST.get('disease')
        hna = request.POST.get('hname')
        rem = request.POST.get('remedy')
        obj = HomeremedyDb(DName=dis,HName=hna,Remedy=rem)
        messages.success(request, "Added successfully...!")
        obj.save()
        return redirect(homeremedypage)

def managehomeremedies(request):
    hr = HomeremedyDb.objects.all()
    return render(request,'admin/Add and Manage Homeremedies.html',{'hr':hr})

def deletehomeremedies(request, dataid):
    hrs = HomeremedyDb.objects.filter(id=dataid)
    hrs.delete()
    return redirect(managehomeremedies)