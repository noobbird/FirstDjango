from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from Post.models import Record,Hot_50
from Post.serializers import RecordSerializer, HotSerializer, ActivitySerializer, HourSerializer
from rest_framework import generics
from Post import utils
import json
from django.http import HttpResponse
from django.db.models import Count
from django.core import serializers

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

def update(request):
    singer_name = request.GET.get("singer_name", None)
    code = utils.update_by_name(singer_name)
    resp = {"success":code}
    return HttpResponse(json.dumps(resp), content_type="application/json")

def activity(request):
    return render(request=request, template_name='Post/mock.html')

def search(request):
    resp = {"suggestions":[]}
    r = utils.search(request.GET.get("query", None))
    res_json = json.loads(r)
    try:
        for i in range(len(res_json["result"]["artists"])):
            resp["suggestions"].append(res_json["result"]["artists"][i]["name"])
    except KeyError:
        print("Search No artists")
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

class LisentFrequence(generics.ListAPIView):
    queryset = Record.objects.extra(select={'day': "TO_CHAR(listen_time, 'YYYY-MM-DD')"}).values('day').annotate(
        available=Count('listen_time'))
    serializer_class = ActivitySerializer

class HourFrequence(generics.ListAPIView):
    queryset = Record.objects.extra(select={'hour': "TO_CHAR(listen_time, 'HH24')"}).values('hour').annotate(
        available=Count('listen_time'))
    serializer_class = HourSerializer
