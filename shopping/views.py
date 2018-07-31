# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from shopping.pagingHelper import pagingHelper

# Create your views here.

def index(request):
    return render(request,"index.html",{})

    # 한글!!

rowsPerPage = 2

'''
def home(request):  # model을 이용해서 별도 SQL 작성 없이 id 필드의 역순으로 (-id) 데이터를 2개만 조회해온다.
    boardList = Post.objects.order_by('-id')[0:2]
    current_page = 1

    # model 을 사용해서 전체 데이터 갯수를 구한다.
    totalCnt = Post.objects.all().count()

    # 이것은 페이징 처리를 위해 생성한 간단한 헬퍼 클래스이다. 별로 중요하지 않으므로 소스를 참조하기 바란다.
    pagingHelperIns = pagingHelper();
    totalPageList = pagingHelperIns.getTotalPageList(totalCnt, rowsPerPage)
    print('totalPageList', totalPageList)

    # 템플릿으로 필요한 정보들을 넘기는 부분이다. 이를 통해서 정적인 템플릿에 동적인 데이터가 결합되게 되는 것이다.
    # 우리는 게시판 최초 화면 처리를 위해서 listSpecificPage.html 템플릿을 호출했다.
    # 그리고 필요한 정보들을 dictionary 로 전달했다.
    return render(request,'shopping/listSpecificPage.html', {'boardList': boardList, 'totalCnt': totalCnt,
                                                        'current_page': current_page, 'totalPageList': totalPageList})

def show_write_form(request):
    return render(request,'shopping/whiteBoard.html',{})

@csrf_exempt
def DoWriteBoard(request):
    br = Post (title = request.POST['title'],
                      author = request.POST['author'],
                      text = request.POST['text'],
                      created_date = timezone.now(),
                    published_date = timezone.now()
                     )
    br.save()

    # 저장을 했으니, 다시 조회해서 보여준다.
    url = 'listSpecificPageWork?current_page=1'
    return HttpResponseRedirect(url)

def listSpecificPageWork(request):
    current_page = request.GET['current_page']
    totalCnt = Post.objects.all().count()

    print('current_page=', current_page)

    # 페이지를 가지고 범위 데이터를 조회한다 => raw SQL 사용함
    boardList = Post.objects.raw('SELECT Z.* FROM(SELECT X.*, ceil( rownum / %s ) as page FROM ( SELECT ID,TITLE,AUTHOR, CREATED_DATE,TEXT\
                                        FROM SHOPPING_POST  ORDER BY ID DESC ) X ) Z WHERE page = %s', [rowsPerPage, current_page])

    print('boardList=',boardList, 'count()=', totalCnt)

    # 전체 페이지를 구해서 전달...
    pagingHelperIns = pagingHelper();
    totalPageList = pagingHelperIns.getTotalPageList( totalCnt, rowsPerPage)

    print('totalPageList', totalPageList)

    return render(request,'shopping/listSpecificPage.html', {'boardList': boardList, 'totalCnt': totalCnt,
                                                        'current_page':int(current_page) ,'totalPageList':totalPageList} )
                                                        '''