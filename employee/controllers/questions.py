from employee.models import Question,Choice
from django.utils import timezone
from django.http import HttpResponse
from django.http import JsonResponse

def register(request):
	q=Question()
	q.text="Asua Programmer"
	q.regdate=timezone.now()
	q.save()
	return HttpResponse("ok")
def get(request):
	query=Question.objects.all()
	arr=[]
	count=0
	while(count<len(query)):
		arr.insert(0,{"text":query[count].text,"regdate":str(query[count].regdate)})
		count=count+1
	return HttpResponse(JsonResponse(arr,safe=False)) 