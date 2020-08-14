# Máme informace o studentech zapsaných do 5-ti předmětů na naší škole. Rádi bychom zjistili,
#kteří studenti přišli na všechny předměty. Vytvořte skript s názvem class_stats.py
#Zde máme data:
#
classes = {
    'Biology' : ['Adam','Chelsea','Marcus','Oliver','Alex','Sandra','Ann'],
    'Math' : ['Marcus','Alex','Glenn','Samuel','Clara','Chelsea'],
    'PE'  : ['Adam','Tyler', 'Alex','Clara'],
    'Social Sciences': ['Abraham','Marcus','Alex','Glenn','Clara'],
    'Chemistry' : ['Alfred', 'Curt','Oliver','Alex','Tyler','Ann']
}
#Příklad běžícího kódu:
#
#~/PythonBeginner/Lesson2 $ python class_stats.py
#Students inscribed into all the subjects: {'Alex'}


student_all = set(classes.get('Biology')) & set(classes.get('Math')) & set(classes.get('PE')) & set(classes.get('Social Sciences')) & set(classes.get('Chemistry'))
print('Students inscribed into all the subjects:', student_all)
