from django.shortcuts import render, redirect
import pyshorteners as psh
import clipboard


# Create your views here.
def index(request):
    if request.method == "POST":
        original_url = request.POST.get("original_url")
        if original_url:
            new_url = psh.Shortener().tinyurl.short(original_url)
            clipboard.copy(new_url)
            return render(request, "main/base.html", {"new_url": new_url})
        else:
            new_url = "Shortened URL Would Be Displayed Here."

    else:
        pass

    return render(request, "main/base.html", {})


def socials(response):
    return render(response, "main/socials.html", {})
