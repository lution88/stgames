from django.contrib import admin
from django.urls import path
from stgame_recommend import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # 관리자 페이지 url
    path('admin/', admin.site.urls),

    # 시작 페이지 url
    path('', views.index, name='index'),

    # 로그인 url
    path('sign-in/', views.sign_in, name='sign-in'),

    # 회원가입 url
    path('sign-up/', views.sign_up, name='sign-up'),

    # 아이디 중복 확인 url
    path('id-check/', views.id_check, name='id-check'),

    # 이메일 중복 확인 url
    path('email-check/', views.email_check, name='email-check'),

    # 아이디 찾기 url
    path('find-id/', views.find_id, name='find-id'),

    # 비밀번호 찾기 url
    path('find-pw/', views.find_pw, name='find-pw'),

    # password 초기화 url
    path('password_reset/', views.UserPasswordResetView.as_view(), name="password_reset"),
    path('password_reset_done/', views.UserPasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', views.UserPasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('password_reset_complete/', views.UserPasswordResetCompleteView.as_view(), name="password_reset_complete"),

    # 메인 페이지 url
    path('main/', views.main, name='main'),

    #
    path('testurl/', views.take_url, name='takeurl'),

    #
    path('tensorflow/', views.tensorflow, name='tensorflow'),

    # 마이 페이지 url
    path('my-page/', views.my_page, name='my-page'),

    # 추천 ML 작동 api
    path('addrecommend/', views.add_reco_fa, name='addrecommend'),

    # 로그아웃
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
