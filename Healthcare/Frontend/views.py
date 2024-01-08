from django.http.response import JsonResponse
from django.shortcuts import render,redirect,get_object_or_404
from Backend.models import DiseaseDb,ExpertDb,HomeremedyDb,Chat_Intraction,DatasetDB
from Frontend.models import SymptomDb,SuggestionDb,LoginDb,ComplainDb,UserProfile,ChatMessage,Thread,ChatBotUser
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from Frontend.forms import ChatMessageForm
from django.contrib import messages
from datetime import datetime
import re, math
# Create your views here.
def expertspage(request):
    return render(request, "expertindex.html")
def exphomepage(request):
    return render(request, "expert/exphome.html")
def symptompage(request):
    dis = DiseaseDb.objects.all()
    return render(request,"expert/Add Symptoms.html", {'dis':dis})
def savesymptoms(request):
    if request.method == "POST":
        dis = request.POST.get('disease')
        sym = request.POST.get('symptom')
        obj = SymptomDb(DName=dis,Symptom=sym)
        obj.save()
        return redirect(symptompage)
def managesymptoms(request):
    sym = SymptomDb.objects.all()
    return render(request,'expert/Add and Manage Symptom.html',{'sym':sym})
def deletesymptom(request, dataid):
    syms = SymptomDb.objects.filter(id=dataid)
    syms.delete()
    return redirect(managesymptoms)

def suggestionpage(request):
    obci=ExpertDb.objects.get(id=request.session['LoginId'])
    obc=ChatMessage.objects.filter(fromid__id=obci.CI_ID.id)
    r=[]
    for i in obc:
        r.append(i.toid.id)
    use = LoginDb.objects.filter(CI_ID__id__in=r)
    return render(request,"expert/Add Suggestion.html", {'use':use})
def savesuggestion(request):
    if request.method == "POST":
        sug = request.POST.get('suggestion')
        dis = request.POST.get('discription')
        uid = request.POST.get('user')


        obj = SuggestionDb(Suggestion=sug, Discription=dis, Ex_Id=ExpertDb.objects.get(id=request.session['LoginId']), Login_ID=LoginDb.objects.get(id=uid))
        obj.save()
        return redirect(managesuggestion)
def managesuggestion(request):
    sug = SuggestionDb.objects.filter(Ex_Id=request.session['LoginId'])
    return render(request,'expert/Add and Manage Suggestion.html',{'sug':sug})
def deletesuggestion(request, dataid):
    sugs = SuggestionDb.objects.filter(id=dataid)
    sugs.delete()
    return redirect(managesuggestion)

def sugesstionview(request):
    sug =SuggestionDb.objects.filter(Login_ID__id=request.session['LoginId'])
    return render(request, 'user/View sugesstion.html', {'sug': sug})

def userpage(request):
    log = LoginDb.objects.first()
    context = {'log': log}
    return render(request, 'userindex.html',context)
def usehomepage(request):
    return render(request, "user/usehome.html")

def user_login(request):
    return render(request,"Logreg.html")
def savereg(request):
    if request.method == "POST":
        fn = request.POST.get('fname')
        ln = request.POST.get('lname')
        eml = request.POST.get('email')
        use = request.POST.get('username')
        pas = request.POST.get('password')
        obj_chat=Chat_Intraction(type="user")
        obj_chat.save()
        obj = LoginDb(First_Name=fn, Last_Name=ln, Email=eml , UserName=use, PassWord=pas,CI_ID=obj_chat)
        obj.save()
        return redirect('user_login')
def userlogin(request):
    if request.method == "POST":
        un = request.POST.get('user_name')
        pwd = request.POST.get('pass_word')
        ob=LoginDb.objects.filter(UserName=un, PassWord=pwd)
        if len(ob)==1:
            request.session['UserName'] = un
            request.session['LoginId'] = ob[0].id
            messages.success(request, "Welcome")
            return redirect('userpage')
        else:
            messages.error(request, "Invalid Username or Password")
            return redirect('user_login')
    return redirect('user_login')
def user_logout(request):
    if 'UserName' in request.session:
        del request.session['UserName']
        messages.success(request, "Logout successful")
    return redirect('user_login')
def expert_login(request):
    return render(request, "expertlogin.html")

def expertlogin(request):
    if request.method == "POST":
        un = request.POST.get('expert_user_name')
        pwd = request.POST.get('expert_pass_word')
        expert = ExpertDb.objects.filter(UserNaMe=un, PassWoRd=pwd).first()
        if expert and not expert.is_blocked:
            messages.success(request, "Login successful")
            request.session['LoginId']=expert.id
            request.session['ExpName']=expert.First_Name+" "+expert.Last_Name
            return redirect('expertspage')
        elif expert and  expert.is_blocked:
            messages.error(request, "Admin has blocked you")
            return redirect('expert_login')
        else:
            messages.error(request, "Invalid username and Password")
            return redirect('expert_login')
    return redirect('expert_login')

def expert_logout(request):
    # if 'UserNaMe' in request.session:
    #     del request.session['UserNaMe']
        messages.success(request, "Logout successful")
        return redirect('expert_login')

def profileview(request):
    log = LoginDb.objects.filter(id=request.session['LoginId'])
    return render(request, 'user/View profile.html',{'log':log})
def updateprofile(request,dataid):
    logs = LoginDb.objects.get(id=dataid)
    return render(request, "user/View and Update profile.html", {'logs':logs})
def saveupdate(request, dataid):
    if request.method == "POST":
        fna = request.POST.get('fname')
        lna = request.POST.get('lname')
        eml = request.POST.get('email')
        LoginDb.objects.filter(id=dataid).update(First_Name=fna, Last_Name =lna, Email=eml)
        return redirect(profileview)

def userview(request):
    user_id = request.user.id
    val = LoginDb.objects.filter(UserName=user_id)
    return render(request, 'expert/Chatwithuser.html', {'val': val})


def expertview(request):
    experts = ExpertDb.objects.all()
    return render(request, 'user/View Expert.html', {'experts': experts})


def chat_with_expert(request,id):

    expert=ExpertDb.objects.get(id=id)
    request.session['Exp_id'] = expert.CI_ID.id
    request.session['ename']=expert.First_Name+" "+expert.Last_Name

    obu=LoginDb.objects.get(id=request.session['LoginId'])
    request.session['cuid']=obu.CI_ID.id

    ob_chat=ChatMessage.objects.filter(fromid__id=request.session['cuid'],toid=request.session['Exp_id'])
    ob_chat1=ChatMessage.objects.filter(toid=request.session['cuid'],fromid__id=request.session['Exp_id'])
    ob_chat=(ob_chat.union(ob_chat1)).order_by('id')
    return render(request, 'user/Chat_expert.html',{"val":ob_chat})


def chat_user(request):
    return render(request, 'expert/Chat_user.html')
def my_view(request):
    # Assuming the user is authenticated
    if request.user.is_authenticated:
        context = {
            'logged_in_username': request.user.UserNaMe
        }
        return render(request, 'expert/Chat_user.html', context)
    else:
        # Handle the case where the user is not authenticated
        return render(request, 'expert/Chat_user.html')
def sendcomplain(request):
    return render(request,'user/Send Complaint.html')
def savecomplain(request):
    if request.method == "POST":
        com = request.POST.get('complain')
        obj = ComplainDb(Complaint = com,Login=LoginDb.objects.get(id=request.session['LoginId']),Reply='pending')
        obj.save()
        return redirect(managecomplain)
def managecomplain(request):
    com = ComplainDb.objects.filter(Login__id=request.session['LoginId'])
    return render(request,'user/Send complaint and View reply.html',{'com':com})

def viewhomeremedies(request):
    hmrem = HomeremedyDb.objects.filter()
    return render(request,'user/View Homeremedies.html', {'hmrem':hmrem})
def chat_box(request, chat_box_name):
    return render(request, "chatbox.html", {"chat_box_name": chat_box_name})



def coun_msg(request):
    ob_chat = ChatMessage.objects.filter(fromid__id=request.session['cuid'], toid=request.session['Exp_id'])
    ob_chat1 = ChatMessage.objects.filter(toid=request.session['cuid'], fromid__id=request.session['Exp_id'])
    ob_chat = (ob_chat.union(ob_chat1)).order_by('id')
    res=[]
    for i in ob_chat:
        print(str(request.session['cuid']),str(i.fromid.id))
        if str(request.session['cuid'])==str(i.fromid.id):
            res.append({"s":"f","msg":i.message,"date":str(i.timestamp),"chat_id":i.id})
        else:
            res.append({"s": "t", "msg": i.message, "date": str(i.timestamp), "chat_id": i.id})
    for i in res:
        print(i)



    return JsonResponse({"data":res})
def expert_coun_msg1(request,id):
    ob=ExpertDb.objects.get(id=request.session['LoginId'])
    ob_chat = ChatMessage.objects.filter(fromid__id=id, toid=ob.CI_ID.id)
    ob_chat1 = ChatMessage.objects.filter(toid=id, fromid__id=ob.CI_ID.id)
    ob_chat = (ob_chat.union(ob_chat1)).order_by('id')
    uob=LoginDb.objects.get(CI_ID__id=id)
    res=[]
    for i in ob_chat:
        print(str(ob.CI_ID.id),str(i.fromid.id))
        if str(ob.CI_ID.id)==str(i.fromid.id):
            res.append({"s":"f","msg":i.message,"date":str(i.timestamp),"chat_id":i.id})
        else:
            res.append({"s": "t", "msg": i.message, "date": str(i.timestamp), "chat_id": i.id})
    for i in res:
        print(i)



    return JsonResponse({"data":res,"name":uob.First_Name+" "+uob.Last_Name,"user_lid":uob.CI_ID.id})
def coun_insert_chat(request,msg):



    obj=ChatMessage()
    obj.fromid=Chat_Intraction.objects.get(id=request.session['cuid'])
    obj.toid=Chat_Intraction.objects.get(id=request.session['Exp_id'])
    obj.message=msg
    obj.timestamp=datetime.now()
    obj.save()






    return JsonResponse({"data":"ok"})

def expert_coun_insert_chat(request,msg,id):
    ob = ExpertDb.objects.get(id=request.session['LoginId'])

    obj=ChatMessage()
    obj.fromid=Chat_Intraction.objects.get(id=ob.CI_ID.id)
    obj.toid=Chat_Intraction.objects.get(id=id)
    obj.message=msg
    obj.timestamp=datetime.now()
    obj.save()






    return JsonResponse({"data":"ok"})


def chatview(request):
    ob = LoginDb.objects.all()
    d=[]
    for i in ob:
        try:
            r={"name":str(i.First_Name)+" "+str(i.Last_Name),'email':i.Email,'loginid':str(i.CI_ID.id)}
            d.append(r)
        except:
            pass
    print(d)
    return JsonResponse(d, safe=False)
def chat_bot(request):
    ob=ChatBotUser.objects.filter(fromid=request.session['LoginId'])
    row=[]
    for i in ob:
        r={"id":"1","msg":i.message}
        row.append(r)
        r = {"id": "0", "msg": i.reply}
        row.append(r)
    return render(request, 'user/Chat_bot.html',{"val":row})
def UserChatbot(request):
    msg=request.POST.get("txt")
    res=cb(msg)
    ob=ChatBotUser(fromid=LoginDb.objects.get(id=request.session['LoginId']),message=msg,reply=res)
    ob.save()

    return redirect(chat_bot)


def cb(qus):
    WORD = re.compile(r'\w+')

    from collections import Counter
    def text_to_vector(text):
        words = WORD.findall(text)
        sw=["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "you're", "you've", "youll", "youd", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "she's", "her", "hers", "herself", "it", "it's", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "that'll", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why",  "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "don't", "should", "should've", "now", "d", "ll", "m", "o", "re", "ve", "y", "ain", "aren", "aren't", "couldn", "couldn't", "didn", "didn't", "doesn", "doesn't", "hadn", "hadn't", "hasn", "hasn't", "haven", "haven't", "isn", "isn't", "ma", "mightn", "mightn't", "mustn", "mustn't", "needn", "needn't", "shan", "shan't", "shouldn", "shouldn't", "wasn", "wasn't", "weren", "weren't", "won", "won't", "wouldn", "wouldn't"]
        words = [w for w in words if not w.lower() in sw]

        return Counter(words)

    def get_cosine(vec1, vec2):
        intersection = set(vec1.keys()) & set(vec2.keys())
        numerator = sum([vec1[x] * vec2[x] for x in intersection])
        sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
        sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
        denominator = math.sqrt(sum1) * math.sqrt(sum2)

        if not denominator:
            return 0.0
        else:
            return float(numerator) / denominator

    vector1 = text_to_vector(qus.lower())
    print("vector1",vector1)
    print("vector1",vector1)
    print("vector1",vector1)
    print("vector1",vector1)
    print("vector1",vector1)
    print("vector1",vector1)
    print("vector1",vector1)
    ss1=DatasetDB.objects.all()


    print("s--" ,ss1)
    res = []
    for d in ss1:
        vector2 = text_to_vector(str(d.Question.lower()))
        print(vector1)
        print(vector2)
        cosine = get_cosine(vector1, vector2)
        print("cosine",cosine)

        res.append(cosine)

    print("res---" ,res)

    ss = 0
    cnt = -1
    i = 0
    for s in res:
        if s > 0.1:
            if ss <= float(s):
                cnt = i
                ss = s
        i = i + 1

    print("ss", ss)
    print("cnt", cnt)
    if cnt!=-1:

        aa = ss1[cnt].Answer
        print(aa)

        return aa
    else:
        return "Sorry, I can not understand the question"
def diseasepredict(request):
    return render(request, 'user/Disease prediction.html')

def viewprediction(request):
    return render(request,'user/Predict.html', )
