from django.shortcuts import render


def start(request):
    # ad = get_object_or_404(CarAdveritsment, id=id)
    return render(request,
                  'index.html',
                  # context={
                  #     'ad': ad
                  # }
                  )
