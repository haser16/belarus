class TitleMixin:
    title = None

    def get_context_data(self, **kwargs):
        context = super(TitleMixin, self).get_context_data(**kwargs)

        context['title'] = self.title

        return context


class PathMixin:
    path = None

    def get_context_data(self, **kwargs):
        context = super(PathMixin, self).get_context_data(**kwargs)

        context['path'] = self.path

        return context


class ModelMixin:
    model_text = None

    def get_context_data(self, **kwargs):
        context = super(ModelMixin, self).get_context_data(**kwargs)

        context['text'] = self.model_text

        return context
