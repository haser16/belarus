from django.views.generic.base import TemplateView

from common.views import *


class IndexTemplateView(TitleMixin, TemplateView):
    template_name = 'main/index.html'
    title = 'Беларусь Современная'


class MedicineTemplateView(ImageMixin, TitleMixin, PathMixin, ModelMixin, TemplateView):
    template_name = 'main/category.html'
    title = 'Беларусь Современная - Медицина'
    path = '/Главная/Медицина/'


class IndustryTemplateView(ImageMixin, TitleMixin, PathMixin, ModelMixin, TemplateView):
    template_name = 'main/category.html'
    title = 'Беларусь Современная - Промышленность'
    path = '/Главная/Промышленность/'


class ConstructionTemplateView(ImageMixin, TitleMixin, PathMixin, ModelMixin, TemplateView):
    template_name = 'main/category.html'
    title = 'Беларусь Современная - Строительство'
    path = '/Главная/Строительство/'


class CarBuildingTemplateView(ImageMixin, TitleMixin, PathMixin, ModelMixin, TemplateView):
    template_name = 'main/category.html'
    title = 'Беларусь Современная - Промышленность(Машиностроение)'
    path = '/Главная/Промышленность(Машиностроение)/'


class AgricultureTemplateView(ImageMixin, TitleMixin, PathMixin, ModelMixin, TemplateView):
    template_name = 'main/category.html'
    title = 'Беларусь Современная - Сельское хозяйство'
    path = '/Главная/Сельское хозяйство/'


class ForestryTemplateView(ImageMixin, TitleMixin, PathMixin, ModelMixin, TemplateView):
    template_name = 'main/category.html'
    title = 'Беларусь Современная - Лесное хозяйство'
    path = '/Главная/Лесное хозяйство/'


class ITTemplateView(ImageMixin, TitleMixin, PathMixin, ModelMixin, TemplateView):
    template_name = 'main/category.html'
    title = 'Беларусь Современная - IT(Информационные технологии)'
    path = '/Главная/IT(Информационные технологии)/'

class CultureTemplateView(ImageMixin, TitleMixin, PathMixin, ModelMixin, TemplateView):
    template_name = 'main/category.html'
    title = 'Беларусь Современная - Культура'
    path = '/Главная/Культура/'


class ArchitectureTemplateView(ImageMixin, TitleMixin, PathMixin, ModelMixin, TemplateView):
    template_name = 'main/category.html'
    title = 'Беларусь Современная - Архитектура'
    path = '/Главная/Архитектура/'
