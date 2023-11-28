from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView
from backend.note.models import Note


class NoteView(TemplateView):
    template_name = 'note/note.html'

    def get(self, request):
        if request.user.is_authenticated:
            note = Note.objects.all()
            ctx = {}
            ctx['notes'] = note
            ctx['description'] = "Я отдам тебе два текста, один критикующий тебя, другой открывающий мои чувства." \
                                 "Но знай открыв одну ссылку, ты не сможешь прочесть другую. " \
                                 "Выбири свой путь сама. "+ \
                                 "Однако, я не монстр, у тебя есть способ прочесть оба текста, " \
                                 "для ясности всей картины, нужна только смекалка."

            return render(request, self.template_name, ctx)
        else:
            return render(request, self.template_name, {})

class NoteDetail(DetailView):
    template_name = 'note/note_detail.html'
    context_object_name = 'object'
    model = Note
    pk_url_kwarg = 'pk'
    queryset = Note.objects.filter(is_published=True)
    def get_object(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        if pk == 1:
            n = Note.objects.get(pk=2)
            n.is_published = False
            n.save()
        else:
            n = Note.objects.get(pk=1)
            n.is_published = False
            n.save()
        obj  = super(NoteDetail, self).get_object()
        return obj

"""def detail(request, pk):
    if pk == 0:
        n = Note.objects.get(pk=1)
        n.is_published = False
        n.save()
    else:
        n = Note.objects.get(pk=0)
        n.is_published = False
        n.save()
    note = Note.objects.filter(is_published=True)
    return render(request, "note/note_detail.html", {'object': note})"""