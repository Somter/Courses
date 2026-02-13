from api.models import CourseResource, CategoryResource
from tastypie.api import Api
from django.urls import path, include


api = Api(api_name='v1')
course_resourse = CourseResource()
categories_resource = CategoryResource()

api.register(course_resourse)
api.register(categories_resource)

urlpatterns = api.urls
