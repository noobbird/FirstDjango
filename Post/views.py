from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from Post.models import Record,Hot_50
from Post.serializers import RecordSerializer, HotSerializer
from rest_framework import generics
import json
from django.http import HttpResponse

# Create your views here.

def index(request):

    records = Record.objects.all().order_by('-listen_time')
    limit =3
    paginator = Paginator(records, limit)
    page = request.GET.get('page', 1)
    result = paginator.page(page)
    context = {
        "record_list": records,
        "page": page
    }
    return render(request=request, template_name='Post/index.html', context=context)

def hot(request):
    return render(request=request,template_name='Post/hot.html')

def search(request):
    resp = {'errorcode': 100, 'detail': request.GET.get("key_word", None)};
    return HttpResponse(json.dumps(resp), content_type="application/json")

class RecordList(generics.ListAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    def get_queryset(self):
        # song_name = self.kwargs['song_name']
        song_name = self.request.query_params.get('song_name', None)
        if song_name is not None:
            return Record.objects.filter(song_name__icontains=song_name)
        return self.queryset

class RecordDetail(generics.RetrieveAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    lookup_field = 'singer_name'

class HotList(generics.ListAPIView):
    queryset = Hot_50.objects.all()
    serializer_class = HotSerializer
    def get_queryset(self):
        singer_name = self.request.query_params.get('singer_name', None)
        if singer_name is not None:
            return Hot_50.objects.filter(singer_name__icontains=singer_name).order_by('-comment_total')
        return self.queryset

class HotDetail(generics.RetrieveAPIView):
    queryset = Hot_50.objects.all()
    serializer_class = HotSerializer
    lookup_field = 'song_id'