from django.views.generic.base import TemplateView

from common.views import ModelMixin, PathMixin, TitleMixin
from main.models import (IT, Agriculture, Architecture, CarBuilding,
                         Construction, Culture, Forestry, Industry, Medicine)


class IndexTemplateView(TitleMixin, TemplateView):
    template_name = 'main/index.html'
    title = 'Беларусь Современная'


class MedicineTemplateView(TitleMixin, PathMixin, ModelMixin, TemplateView):
    template_name = 'main/category.html'
    title = 'Беларусь Современная - Медицина'
    path = '/Главная/Медицина/'
    model_text = Medicine.objects.all()


class IndustryTemplateView(TitleMixin, PathMixin, ModelMixin, TemplateView):
    template_name = 'main/category.html'
    title = 'Беларусь Современная - Промышленность'
    path = '/Главная/Промышленность/'
    model_text = Industry.objects.all()


class ConstructionTemplateView(TitleMixin, PathMixin, ModelMixin, TemplateView):
    template_name = 'main/category.html'
    title = 'Беларусь Современная - Строительство'
    path = '/Главная/Строительство/'
    model_text = Construction.objects.all()


class CarBuildingTemplateView(TitleMixin, PathMixin, ModelMixin, TemplateView):
    template_name = 'main/category.html'
    title = 'Беларусь Современная - Промышленность(Машиностроение)'
    path = '/Главная/Промышленность(Машиностроение)/'
    model_text = Construction.objects.all()


class AgricultureTemplateView(TitleMixin, PathMixin, ModelMixin, TemplateView):
    template_name = 'main/category.html'
    title = 'Беларусь Современная - Сельское хозяйство'
    path = '/Главная/Сельское хозяйство/'
    model_text = Agriculture.objects.all()


class ForestryTemplateView(TitleMixin, PathMixin, ModelMixin, TemplateView):
    template_name = 'main/category.html'
    title = 'Беларусь Современная - Лесное хозяйство'
    path = '/Главная/Лесное хозяйство/'
    model_text = Forestry.objects.all()


class ITTemplateView(TitleMixin, PathMixin, ModelMixin, TemplateView):
    template_name = 'main/category.html'
    title = 'Беларусь Современная - IT(Информационные технологии)'
    path = '/Главная/IT(Информационные технологии)/'
    model_text = IT.objects.all()


class CultureTemplateView(TitleMixin, PathMixin, ModelMixin, TemplateView):
    template_name = 'main/category.html'
    title = 'Беларусь Современная - Культура'
    path = '/Главная/Культура/'
    model_text = Culture.objects.all()


class ArchitectureTemplateView(TitleMixin, PathMixin, ModelMixin, TemplateView):
    template_name = 'main/category.html'
    title = 'Беларусь Современная - Архитектура'
    path = '/Главная/Архитектура/'
    model_text = Architecture.objects.all()
