from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import PageForm
from .models import Page
from datetime import datetime
from zoneinfo import ZoneInfo

#urls.pyからリスエストを受けて、レスポンスを返す

#クラスの継承 getトップページにアクセスした時に動く

class IndexView(View):
  def get(self, request):
      datetime_now = datetime.now(
         ZoneInfo("Asia/Tokyo")
      ).strftime("%Y年%m月%d日 %H:%M:%S")
      return render(
         request, "diary/index.html", {"datetime_now": datetime_now})



# データを入力する画面を表示する
# get(form = PageForm()空のフォームを作成する
class PageCreateView(View):
   def get(self, request):
      form = PageForm()
      return render(request, "diary/form.html", {"form": form})
   

# ユーザが保存ボタンを押した時に動く 
# post request.POSTに送信されたデータが格納される PageForm(request.POST)でフォームを初期化する formが
   def post(self, request):
     form = PageForm(request.POST, request.FILES) 
     if form.is_valid():
        form.save()
        return redirect("diary:index")
     return render(request, "diary/form.html", {"form": form})
      
      
class PageListView(View):
   def get(self, request):
      page_list = Page.objects.order_by("page_date")
      return render(request, "diary/page_list.html", {"page_list": page_list})


# get_object_or_404 データベースからIDが一致するPageのデータを取得
class PageDetailView(View):
   def get(self, request, id):
      page = get_object_or_404(Page, id=id)
      return render(request, "diary/page_detail.html", {"page": page})



index = IndexView.as_view()
page_create = PageCreateView.as_view()
page_list = PageListView.as_view()
page_detail = PageDetailView.as_view()
# indexには関数に変換したものを代入