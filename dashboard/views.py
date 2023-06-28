from django.shortcuts import render,redirect
from dashboard.models import Notes,Homework
from . forms import *
from django.contrib import messages
from django.views.generic import DetailView
from youtubesearchpython import VideosSearch



def home(request):
    return render(request,'dashboard/home.html')


def notes(request):
    if request.method=="POST":
        form=NotesForm(request.POST)
        if form.is_valid():
            notes=Notes(user=request.user,title=request.POST['title'],description=request.POST['description'])
            notes.save()
            messages.success(request,'notes added  successfully')
    
    form=NotesForm
    notes=Notes.objects.filter(user=request.user)
    context={'notes':notes,'form':form}
    return render(request,'dashboard/notes.html',context)



def delete_notes(request,pk=None):
    Notes.objects.get(id=pk).delete()
    return redirect("notes")

class NotesDetailsView(DetailView):
    model=Notes
    template_name="dashboard/notes_detail.html"



def homework(request):
    if request.method=="POST":
        try:
            finished=request.POST['is_finished']
            if finished=="on":
                finished=True
            else:
                finished=False
        except:
            finished=False

             
        form = HomeworkForm(request.POST)
        if form.is_valid():
           homework = form.save(commit=False)
           homework.user = request.user
           homework.is_finished=finished
           homework.save()
           messages.success(request, "Homework added successfully.")
           return redirect('homework')
        else:
            form = HomeworkForm()
            return render(request, 'homework.html', {'form': form})
        # homeworks=HomeworkForm(
        #     user=request.user,
        #     subject=request.POST['subject'],
        #     title=request.POST['title'],
        #     description=request.POST['description'],
        #     due=request.POST['due'],
        #     is_finished=finished
        # )
        # homeworks.save()
        # messages.success(request,f"homework added")

    homeworks=Homework.objects.filter(user=request.user)
    form=HomeworkForm()
    if len(homeworks)==0:
        homework_done=True
    else:
        homework_done=False
    context={"homeworks":homeworks,
             "homework_done":homework_done,
             "form":form
             }
    return render(request,'dashboard/homework.html',context)



def update_homework(request,pk=None):
    homework=Homework.objects.get(id=pk)
    if homework.is_finished == True:
        homework.is_finished=False
    elif homework.is_finished==False:
         homework.is_finished=True
    homework.save()
    return redirect('homework')

def delete_homework(request,pk=None):
    Homework.objects.get(id=pk).delete()
    return redirect("homework")


def youtube(request):
    if request.method=="POST":
        form=Dashboardform(request.POST)
        text=request.POST['text']
        video=VideosSearch(text,limit=10)
        result_list=[]
        for i in video.result()['result']:
            result_dict={
                'input':text,
                "title":i['title'],
                "duration":i['duration'],
                "thumbnail":i['thumbnails'][0]['url'],
                "channel":i['channel']['name'],
                "link":i['link'],
                "views":i['viewCount']['short'],
                "published":i['publishedTime']
            }
            desc=''
            if i['descriptionSnippet']:
                for j in i['descriptionSnippet']:
                    desc+=j['text']
                    result_dict['description']=desc
                    result_list.append(result_dict)
                    context={
                        'form':form,
                        'results':result_list
                            }
        return render(request,'dashboard/youtube.html',context)
    form=Dashboardform()
    context={"form":form}
    return render(request,'dashboard/youtube.html',context)
