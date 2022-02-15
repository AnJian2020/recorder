from django.db import models
from django.utils import timezone


class ReadNoteModel(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='id')
    title = models.CharField(verbose_name='标题', max_length=256)
    content = models.TextField(verbose_name='内容')
    submit_time = models.DateTimeField(verbose_name='提交时间', default=timezone.now)
    edit_time = models.DateTimeField(verbose_name="最后编辑时间", default=timezone.now)
    link = models.CharField(verbose_name='阅读链接', max_length=256, blank=True, null=True)

    def __str__(self):
        return "编号：%s 标题：%s" % (self.id, self.title)

    def save(self, *args, **kwargs):
        if not self.id:
            self.submit_time=timezone.now()
            self.edit_time=timezone.now()
        else:
            self.edit_time=timezone.now()
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = '阅读笔记'
        verbose_name_plural = '阅读笔记'
        db_table = 'read_note_table'
