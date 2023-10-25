def update(request,pk):
    reservation = Reservation.objects.get(pk)
    if request.method == "POST":
        __(a)__
        if form.is_valid():
            form.save()
            return redirect("articles:detail",reservation.pk)
    else:
        __(b)__
    context = {
        'reservation':reservation,
        'form':form,
    }
    return render(request,"articles/update.html",context)


(a) : form = ReservationForm(data = request.POST, instance=reservation)
(b) : form = ReservationForm(instance=reservation)