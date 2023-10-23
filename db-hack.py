import random
from datacenter.models import Schoolkid,Mark,Commendation,Chastisement,Lesson


def get_compliment():
    compliments = [
        "Молодец!",
        "Отлично!",
        "Хорошо!",
        "Гораздо лучше, чем я ожидал!",
        "Ты меня приятно удивил!",
        "Великолепно!",
        "Прекрасно!",
        "Ты меня очень обрадовал!",
        "Именно этого я давно ждал от тебя!",
        "Сказано здорово – просто и ясно!",
        "Ты, как всегда, точен!",
        "Очень хороший ответ!",
        "Талантливо!",
        "Ты сегодня прыгнул выше головы!","Я поражен!",
        "Уже существенно лучше!",
        "Потрясающе!",
        "Замечательно!",
        "Прекрасное начало!",
        "Так держать!",
        "Ты на верном пути!",
        "Здорово!",
        "Это как раз то, что нужно!",
        "Я тобой горжусь!",
        "С каждым разом у тебя получается всё лучше!",
        "Мы с тобой не зря поработали!",
        "Я вижу, как ты стараешься!",
        "Ты растешь над собой!",
        "Ты многое сделал, я это вижу!",
        "Теперь у тебя точно все получится!"
    ]
    return random.choice(compliments)

def get_schoolkid(name):
    try:
        return Schoolkid.objects.get(full_name__contains=name) 
    except Schoolkid.DoesNotExist:    
        print(f"Имя {name} отсутствует в базе данных.")
    except  Schoolkid.MultipleObjectsReturned:
        print("Найдено более одного имени.")   
      
def fix_marks(schoolkid):
    Mark.objects.filter(schoolkid=schoolkid, points__in=[2,3]).update(points=5)

def remove_chastisements(schoolkid):
    Chastisement.objects.filter(schoolkid=schoolkid).delete()

def create_commendation(schoolkid, lesson):
    if schoolkid:
        random_lesson=Lesson.objects.filter(year_of_study=schoolkid.year_of_study, 
                                    group_letter=schoolkid.group_letter,
                                    subject__title = lesson).order_by('?').first() 
        if random_lesson:
            Commendation.objects.create(text=get_compliment(),created=random_lesson.date,schoolkid=schoolkid,subject=random_lesson.subject,teacher=random_lesson.teacher)
        else:
            print(f"Предмет {lesson} отсутствует в базе данных")
