from django.db import models

class Note(models.Model):
    class Meta:
        db_table = 'note'
        verbose_name = 'notes'
        verbose_name_plural = "Заметки"
    title = models.CharField("Заголовок", max_length=50)
    text = models.TextField("Текст")
    is_published = models.BooleanField("Published", default=True, help_text="Заметка, если ты дошла до этого пункта, то ты очень упорная, я ценью это." \
                       "Подсказка: один из этих полей явно отрицательны, нужно их поменять на True значение, " \
                       "и ты дошла до явной победы. Теперь всего лишь нужно прочесть, по прежней ссылке.")

    def __str__(self):
        return '{}'.format(self.title)