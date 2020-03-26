from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt


def index(request):
    return render(request, "index.html")


def sign_in(request):
    return render(request, "sign_in.html")


def register_page(request):
    return render(request, "register.html")


def home(request):
    return redirect("/")


def logout(request):
    request.session.clear()
    return redirect("/")


def reg(request):
    errors = User.objects.validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/register_page")

    # if already existing will return an objects of a user
    is_user_in_db = User.objects.filter(email=request.POST["email"]).first()

    if is_user_in_db:
        print("user is already exsiting")
        return redirect("/register_page")

    hashed_pw = bcrypt.hashpw(
        request.POST["password"].encode(), bcrypt.gensalt()
    ).decode()

    user_created = User.objects.create(
        first_name=request.POST["fname"],
        last_name=request.POST["lname"],
        email=request.POST["email"],
        password=hashed_pw,
    )

    request.session["user_id"] = user_created.id
    return redirect("/dash")


def log(request):
    found_user = User.objects.filter(email=request.POST["email"]).first()

    if found_user:  # if email is found in db
        is_pw_correct = bcrypt.checkpw(
            request.POST["password"].encode(), found_user.password.encode()
        )

        if is_pw_correct:  # if password is correct
            request.session["user_id"] = found_user.id
            return redirect("/dash")
        else:  # if pw is incorrect
            messages.error(request, "Incorrect password")
            return redirect("/sign_in")
    else:  # if email is not found
        messages.error(request, "User doesn't exist")
        return redirect("/sign_in")


def dash(request):
    user_id_is_session = request.session.get("user_id")
    budget = Budget.objects.all()
    if request.session.get("activities") == None:
        request.session["activities"] = []
    if request.session.get("new_budget") == None:
        request.session["new_budget"] = 0
    if user_id_is_session:
        user_from_db = User.objects.get(id=user_id_is_session)
        context = {
            "user": user_from_db,
            "budget": budget,
            "activities": request.session["activities"],
            "new_budget": request.session["new_budget"],
        }
    return render(request, "success.html", context)


def edit_page(request):
    return render(request, "edit_page.html")


def edit_info(request):
    current_user = User.objects.get(id=request.session["user_id"])
    create_budget = Budget.objects.create(
        account=request.POST["account"],
        total_amount=request.POST["total_amount"],
        budget=request.POST["budget"],
        created_by=current_user,
    )
    return redirect("/dash")


def about_page(request):
    return render(request, "about_page.html")


def calendar_page(request):
    return render(request, "calendar_page.html")


def delete(request, id):
    account_id = Budget.objects.get(id=id)
    account_id.delete()
    return redirect("/dash")


def splurge(request, id):
    user_id_is_session = request.session.get("user_id")
    budgetz = Budget.objects.get(id=id)
    print(budgetz.budget)
    budgetz.budget = budgetz.budget * 0.3

    activities = request.session.get("activities")
    activities.append("You just splurged your new balance is " + str(budgetz.budget))
    request.session["activities"] = activities

    budgetz.save()
    print(request.session["activities"])
    return redirect("/dash")


def manage_page(request):
    return render(request, "manage_page.html")


def expenses(request):
    return redirect("/manage_page")
