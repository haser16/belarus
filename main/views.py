from django.shortcuts import render
from django.views.generic.base import TemplateView

from main.models import (IT, Agriculture, Architecture, CarBuilding,
                         Construction, Culture, Forestry, Industry, Medicine)


class IndexTemplateView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexTemplateView, self).get_context_data()

        context['title'] = 'Современная Беларусь'

        return context


class MedicineTemplateView(TemplateView):
    template_name = 'main/category.html'

    def get_context_data(self, **kwargs):
        context = super(MedicineTemplateView, self).get_context_data()

        context['path'] = '/Главная/Медицина/'
        context['text'] = Medicine.objects.all()

        return context


class IndustryTemplateView(TemplateView):
    template_name = 'main/category.html'

    def get_context_data(self, **kwargs):
        context = super(IndustryTemplateView, self).get_context_data()

        context['path'] = '/Главная/Промышленность/'
        context['text'] = Industry.objects.all()

        return context


class ConstructionTemplateView(TemplateView):
    template_name = 'main/category.html'

    def get_context_data(self, **kwargs):
        context = super(ConstructionTemplateView, self).get_context_data()

        context['path'] = '/Главная/Строительство/'
        context['text'] = Construction.objects.all()

        return context


class CarBuildingTemplateView(TemplateView):
    template_name = 'main/category.html'

    def get_context_data(self, **kwargs):
        context = super(CarBuildingTemplateView, self).get_context_data()

        context['path'] = '/Главная/Машиностроение/'
        context['text'] = CarBuilding.objects.all()

        return context


class AgricultureTemplateView(TemplateView):
    template_name = 'main/category.html'

    def get_context_data(self, **kwargs):
        context = super(AgricultureTemplateView, self).get_context_data()

        context['path'] = '/Главная/Сельское хозяйство/'
        context['text'] = Agriculture.objects.all()

        return context


class ForestryTemplateView(TemplateView):
    template_name = 'main/category.html'

    def get_context_data(self, **kwargs):
        context = super(ForestryTemplateView, self).get_context_data()

        context['path'] = '/Главная/Лесное хозяйство/'
        context['text'] = Forestry.objects.all()

        return context


class ITTemplateView(TemplateView):
    template_name = 'main/category.html'

    def get_context_data(self, **kwargs):
        context = super(ITTemplateView, self).get_context_data()

        context['path'] = '/Главная/IT(Информационные технологии)/'
        context['text'] = IT.objects.all()

        return context


class CultureTemplateView(TemplateView):
    template_name = 'main/category.html'

    def get_context_data(self, **kwargs):
        context = super(CultureTemplateView, self).get_context_data()

        context['path'] = '/Главная/Культура/'
        context['text'] = Culture.objects.all()

        return context


class ArchitectureTemplateView(TemplateView):
    template_name = 'main/category.html'

    def get_context_data(self, **kwargs):
        context = super(ArchitectureTemplateView, self).get_context_data()

        context['path'] = '/Главная/Архитектура/'
        context['text'] = Architecture.objects.all()

        return context

