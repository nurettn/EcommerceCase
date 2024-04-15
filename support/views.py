from django.shortcuts import get_object_or_404, redirect, render

from .forms import StoreInformationForm, UserInformationForm
from .models import UserInformation


def user_info_view(request):
    if request.method == "POST":
        form = UserInformationForm(request.POST)
        if form.is_valid():
            user_info = form.save()
            return redirect("store_info", user_id=user_info.id)
    else:
        form = UserInformationForm()
    return render(request, "user_info.html", {"form": form})


def store_info_view(request, user_id=None):
    if user_id is None:
        return redirect("user_info")

    user = get_object_or_404(UserInformation, pk=user_id)

    if request.method == "POST":
        form = StoreInformationForm(request.POST)
        if form.is_valid():
            store_info = form.save(commit=False)
            store_info.user = user
            store_info.save()
            return render(
                request,
                "completion.html",
                {"message": "Your application is completed"},
            )
    else:
        form = StoreInformationForm()

    return render(
        request, "store_info.html", {"form": form, "user_id": user_id}
    )
