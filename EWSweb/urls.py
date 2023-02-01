"""EWSweb URL Configuration

Các Apps trong Website:
    1. Home: Trang chủ
    2. EarlyWarningNote: Thông tin cảnh báo
    3. MonitoringData: Dữ liệu quan trắc
    4. TraningMaterial: Tài liệu hướng dẫn - tập huấn
    5. Contact: Thông tin liên hệ và quản lý account

Danh sách `urlpatterns` định tuyến URL đến các chế độ xem. Để biết thêm thông tin vui lòng xem:
     https://docs.djangoproject.com/en/4.0/topics/http/urls/
Ví dụ:
Chế độ xem chức năng
     1. Thêm nhập: từ chế độ xem nhập của my_app
     2. Thêm URL vào urlpatterns: path ('', views.home, name = 'home')
Chế độ xem dựa trên lớp
     1. Thêm nhập: from other_app.views import Trang chủ
     2. Thêm URL vào urlpatterns: path ('', Home.as_view (), name = 'home')
Bao gồm một URLconf khác
     1. Nhập hàm include (): từ django.urls nhập bao gồm, đường dẫn
     2. Thêm một URL vào urlpatterns: path ('blog /', include ('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),
    path('EarlyWarningNote', include('EarlyWarningNote.urls')),
    path('MonitoringData', include('MonitoringData.urls')),
    path('TrainingMaterial', include('TrainingMaterial.urls')),
    path('Contact', include('Contact.urls')),
    path('Register', include('Register.urls')),
    path('Upload', include('Upload.urls')),
]
