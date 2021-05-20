from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse, Http404
from graphviz import Digraph
from .models import Possesion
from django.forms import modelformset_factory, inlineformset_factory
from django.http import HttpResponseRedirect
from .sequence import Sequence

def home (request):

    PossessionFormset = modelformset_factory(Possesion, fields=('mother','child','share',))
    formset = PossessionFormset()
    if request.method == 'POST':
        formset = PossessionFormset(request.POST)
        if formset.is_valid ():
            formset.save()
            return HttpResponseRedirect(request.path_info)

    return render(request,'diagram/home.html',{'formset':formset})

def checkCompanies (request):

    result = Possesion.objects.all()

    context = { 'query_results' : result }

    # Returning the rendered html
    return render(request, "diagram/review.html", context)

def generatePDF (request):

    result = Possesion.objects.all()

    u = Digraph('unix', filename='unix.gv',
                node_attr={'color': 'lightblue2', 'style': 'filled'})
    u.attr(size='6,6')

    for obj in result:
        u.edge(obj.mother, obj.child, label=str(obj.share))

    u.render()
    return redirect("pdf")


def pdf_view(request):
    try:
        return FileResponse(open('unix.gv.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

def deleteAll (request):
    Possesion.objects.all().delete()
    return redirect("home")

def sequenceSelection (request):

    start = request.GET.get('start')
    end = request.GET.get('end')

    sequence = Sequence()
    graph = sequence.getGraphDisct()
    paths = sequence.find_all_paths(graph,start,end)

    for path in paths:
        share = sequence.shareCalculations(path)
        path.append(share)

    context = {'paths': paths}

    return render(request,"diagram/sequence.html",context)

