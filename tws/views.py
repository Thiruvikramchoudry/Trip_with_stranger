from django.shortcuts import render,redirect
from .models import comments,registration, slot_details, user_with_slotdetail
from django.contrib.auth.models import User, auth
from datetime import date
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
import random as ran

import json

import random

# Create your views here.

def index(request):
    return render(request, 'tws/index.html')

def comment(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        user_email = request.POST.get('user_email')
        commentext = request.POST.get('comment')

        comment_save = comments(username=username, user_email=user_email, comment=commentext)
        comment_save.save()
        return render(request, 'tws/index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        passWord = request.POST['pass']


        user = authenticate(username=username, password=passWord)
        if user is not None:
            users = user_with_slotdetail.objects.all()
            flag = 0
            slotid=""
            for user_name in users:
                if user_name.username == username:
                    flag = 1
                    slotid=user_name.slot_id
            auth.login(request, user)
            if flag == 0:
                return redirect('/userpage')
            else:
                return redirect('slotpage/' + str(slotid))
        else:
            # used to pass comments ....

            return render(request, 'tws/login.html',
                          {'messages': "incorrect password"})

    else:
        return render(request, 'tws/login.html')



# registration form...
def register(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        useremail = request.POST.get('email')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')

        if gender == "male":
            gender = "Male"
        else:
            gender = 'Female'
        phone_no = request.POST.get('phone')
        user_name = request.POST.get('username')

        datas = registration.objects.all()
        username_taken = []
        for i in datas:
            username_taken.append(i.username)
        if user_name in username_taken:
            error = "username_taken"
            return render(request, 'tws/registeration_form.html',{'error':error})


        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        city = request.POST.get('city')
        state = request.POST.get('state')
        address = request.POST.get('address')
        pin = request.POST.get('pincode')

        #print(user_image)
        image_no=random.randint(0, 4)
        image_url=""
        if gender=="Male":
            image_url="tws/dynamixcpage1_styles/profile_avators/male_pics/male_avt"+str(image_no)+".png"
        else:
            image_url="tws/dynamixcpage1_styles/profile_avators/female_pics/female_avt"+str(image_no)+".png"



        # converting date of birth to age
        today = date.today()
        today_date = (today.strftime("%d/%m/%Y")).split("/")

        age = dob.split("/")
        user_age = int(today_date[2]) - int(age[2])




        user = User.objects.create_user(username=user_name, email=useremail, password=password)
        regForm = registration(firstname=firstname, lastname=lastname, user_email=useremail, age=user_age,
                               gender=gender,
                               mobile_number=phone_no, username=user_name, password=password,
                               city=city, state=state, address=address, pincode=pin,image_url=image_url)
        regForm.save()

        user.save()
        return redirect('/login')
    else:
        """datas=registration.objects.all()
        username_taken=[]
        for i in datas:
            username_taken.append(i.username)
        username_taken=json.dumps(username_taken)"""

        return render(request, 'tws/registeration_form.html')


@login_required()
def dynamic_page_notjoined(request):
    username = request.user
    userdetail=registration.objects.get(username=username)
    print(userdetail.username)
    userage=userdetail.age
    usergender=""
    image_url=""


    slot_detail = slot_details.objects.all()
    slots = []


    for slot in slot_detail:

        flag=0
        if(str(usergender)=="Male" and int(slot.Current_Number_Male)==int(slot.Total_Male)):
            flag=1
            print(1)
        elif(usergender=="Female" and slot.Current_Number_Female==slot.Total_Female):
            flag=1
            print(2)
        if(int(userage)>int(slot.Maximum_age_Members) or int(userage)<int(slot.Minimum_age_Members)):
            flag=1
            print(3,slot.Maximum_age_Members,userage,slot.Minimum_age_Members)
        if(flag==0):
            slots.append(slot)
    print(slots)


    return render(request, 'tws/dynamicpage_notjoineduser.html', {'userdetail': userdetail, 'slots': slots})


# create a slot

@login_required()
def create_slot_phase1(request):
    if request.method == 'POST':
        username = request.user
        slotname = request.POST['slotname']

        arrivalcity = request.POST['arrivalcity']
        destinationcity = request.POST['destinationcity']
        days_of_trip = request.POST['notrip']
        number_of_members = request.POST['nomembers']


        current_number_members = 1
        id=[]
        slot_detail=user_with_slotdetail.objects.all()
        for i in slot_detail:
            id.append(i.slot_id)
        try:
            slot_id=max(id)+1
        except:
            slot_id=100000

        minimum_age = request.POST['minage']
        maximum_age = request.POST['maxage']
        total_male = request.POST['totmale']
        totalfemale = request.POST['totfemale']
        starting_date = request.POST['dot']
        returning_date = request.POST['doa']

        current_number_female = 0
        current_number_male = 0
        gender=""
        details = registration.objects.get(username=username)
        gender=details.gender
        age=details.age
        if str(gender) == 'Male':
            current_number_male = 1
        else:
            current_number_female = 1

        if(int(maximum_age)<int(age) or int(minimum_age)>int(age)):
            difference=(int(maximum_age)-int(minimum_age))//2
            maximum_age=int(age)+difference
            minimum_age=int(age)-difference


        slot = slot_details(username=username, slotname=slotname,
                            Arrivalcity=arrivalcity, Destination=destinationcity, Days_of_Trip=days_of_trip,
                            Number_of_Members=number_of_members, Current_Number_Members=current_number_members,
                            Minimum_age_Members=minimum_age, Maximum_age_Members=maximum_age, Total_Male=total_male,
                            Total_Female=totalfemale, Starting_Date=starting_date, Returning_Date=returning_date,
                            Current_Number_Female=current_number_female, Current_Number_Male=current_number_male,slot_id=slot_id)
        slot.save()
        userandslot = user_with_slotdetail(username=username, slot_id=slot_id)
        userandslot.save()
        user_ = str(username)
        return redirect('/slotpage/' + str(slot_id))
    else:
        return render(request, 'tws/slotcreate.html')


# logout
def logout(request):
    auth.logout(request)

    return redirect('/login')


# join a slot
# @login_required()
def joinuser(request, slotid):
    username = request.user
    slotname = slot_details.objects.get(slot_id=slotid).slotname
    userandslot = user_with_slotdetail(username=username, slot_id=slotid)
    userandslot.save()
    details=slot_details.objects.get(slotname=slotname)
    user_details=registration.objects.get(username=username)

    details.Current_Number_Members+=1
    slot=slot_details.objects.get(slot_id=slotid)

    mcount=0;fcount=0
    if(str(user_details.gender)=="Male"):
        slot.Current_Number_Male+=1
    else:
        slot.Current_Number_Female+=1
    slot.Current_Number_Members+=1
    slot.save()




    """slot = slot_details(username=details.username, slotname=slotname,
                        Arrivalcity=details.Arrivalcity, Destination=details.Destination, Days_of_Trip=details.Days_of_Trip,
                        Number_of_Members=details.Number_of_Members, Current_Number_Members=details.Current_Number_Members,
                        Minimum_age_Members=details.Minimum_age_Members, Maximum_age_Members=details.Maximum_age_Members, Total_Male=details.Total_Male,
                        Total_Female=details.Total_Female, Starting_Date=details.Starting_Date, Returning_Date=details.Returning_Date,
                        Current_Number_Female=details.Current_Number_Female+fcount, Current_Number_Male=details.Current_Number_Male+mcount)

    details.delete()
    slot.save()"""



    return redirect('/slotpage/'+str(slotid))
   # return render(request, 'tws/dynamicpage_joined.html')


# page for slot joined users
@login_required()
def slotpage(request, slotid):
    username=request.user
    users = user_with_slotdetail.objects.all()
    teammembers = []
    for user in users:
        if user.slot_id == slotid:
            teammembers.append(user.username)
    userdetails = []
    userdetail=registration.objects.all()
    for user in userdetail:
        if user.username in teammembers:
            userdetails.append(user)
    innertext = ""
    try:
        status = slot_details.objects.get(username=username)
    except:
        status = 0
    if (status == 0):
        innertext = "Leave"
    else:
        innertext = "Delete Slot"
    slot=slot_details.objects.get(slot_id=slotid)

    return render(request, "tws/dynamicpage_joineduser.html",{"slotname": slot.slotname, "team": userdetails, "innertext": innertext})



def delete_slot(request):
    slotname = slot_details.objects.get(username=request.user)

    users = user_with_slotdetail.objects.filter(slot_id=slotname.slot_id)
    for user in users:
        user.delete()

    slot_details.objects.filter(username=request.user).delete()
    return redirect('/userpage')

def leave_slot(request):

    slotname="none"
    gender=registration.objects.get(username=request.user).gender

    user_details = user_with_slotdetail.objects.get(username=request.user)

    slot_upd=slot_details.objects.get(slot_id=user_details.slot_id)
    slot_upd.Current_Number_Members-=1
    if gender=="Male":
        slot_upd.Current_Number_Male-=1
    else:
        slot_upd.Current_Number_Female-=1
    slot_upd.save()
    users = user_with_slotdetail.objects.filter(username=request.user).delete()


    return redirect('userpage')


def sample(request):
    return render(request,'tws/dynamicpage_notjoined.html')
