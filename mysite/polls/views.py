from django.http import HttpResponse
from django.shortcuts import render
from .models import Question
def index(request):
    myname = "Ngoc Tuan"
    taisan1 = ["Dien thoai", "May Tinh", "May Bay", "Nhieu tien"]
    context = {"name": myname, "taisan": taisan1}
    return render(request, "polls/index.html", context)

def viewlist(request):
    #get_object_or_404(Question, pk=1)
    #list_question = get_object_or_404(Question, pk=4)
    list_question = Question.objects.all()
    context = {"dsquest": list_question}
    return render(request, "polls/question_list.html", context)
def detailView(request, question_id):
    q = Question.objects.get(pk = question_id)
    return render(request, "polls/detail_question.html", {"qs" : q})

