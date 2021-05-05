from django.db import models
from random import shuffle


DIFF_CHOICES=(
    ('easy','easy'),
    ('medium','meduim'),
    ('hard','hard'),

)

class Quiz(models.Model):

    name = models.CharField(max_length=120)
    topic = models.CharField(max_length=120)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="Duration of the quiz in minutes")
    required_score_to_pass = models.IntegerField(help_text="minimum score to pass in %")
    difficulty = models.CharField(max_length=6,choices=DIFF_CHOICES)
    quiz_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}-{self.topic}"

    def get_questions(self):
        questions = list(self.question_set.all())
        shuffle(questions)
        return questions[:self.number_of_questions]
    
    class Meta:
        verbose_name_plural = 'Quizes'