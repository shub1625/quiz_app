from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView
from .models import Quiz
from questions.models import Question,Answer
from results.models import Result

class QuizListView(ListView):
    model = Quiz
    template_name = 'quizes/quiz_list.html'

def quiz_detail_view(request,pk):
    quiz = Quiz.objects.get(id=pk)
    return render(request,'quizes/quiz.html',{'quiz': quiz})


def quiz_data_view(request,pk):
    quiz = Quiz.objects.get(id=pk)
    questions = []
    for que in quiz.get_questions():
        answers = []
        for ans in que.get_answers():
            answers.append(ans.text)
        questions.append({
            str(que): answers
        })
    
    return JsonResponse({
        'data': questions,
        'time' : quiz.time,
    })

def quiz_save_view(request,pk):
    
    if request.is_ajax():
        data = request.POST
        data_ = dict(data.lists())
        data_.pop('csrfmiddlewaretoken')
        
        questions = []

        for key in data_.keys():
            question = Question.objects.get(text=key)
            questions.append(question)

        user = request.user
        quiz = Quiz.objects.get(pk=pk)
        
        score = 0
        multipler = 100/quiz.number_of_questions
        results = []
        correct_answer = None

        for que in questions:
            a_selected = request.POST.get(que.text)

            if a_selected != "":
                question_answer = Answer.objects.filter(question=que).filter(text=a_selected)[0]
                
                print(question_answer)
                if question_answer.correct:
                    score += 1
                    correct_answer = question_answer.text
                else:
                    correct_answer = Answer.objects.filter(question=que).filter(correct=True)[0].text
                
                
                results.append({
                    str(que) : {'correct_answer': correct_answer ,
                                'answered': question_answer.text}
                })

            else:
                results.append({
                    str(que) : 'not answered'
                })
        # print(results)
        final_score = score * multipler
        
        res = Result.objects.create(quiz=quiz,user=user,score=final_score)
        # res.save()

        if final_score >= quiz.required_score_to_pass:
            return JsonResponse({
                'passed': True,
                'score' : final_score,
                'results': results
            })
        else:    
            return JsonResponse({
                'passed': False,
                'score' : final_score,
                'results': results
                })