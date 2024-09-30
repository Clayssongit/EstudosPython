"""
1 - O método estático não utiliza o parâmetro referente a classe.
2 - O método estático pode acessar mas não pode modificar o estado da classe.
3 - Usamos o decorator @staticmethod para criar um método estático.
"""

class Course:
    def __init__(self, name, trail):
        self.name = name
        self.trail = trail

    @staticmethod   
    def course_trail(trail):
        if trail == "Python Fundamentos":
            course = ["Dominando o Python", "Módulos e pip", "Orientação a Objetos"]
        elif trail == "Automação com Python":
            course = ["Automação de Tarefas", "Web Scraping", "Assistente Virtual em python"]
        else:
            course = ["A definir "]
        return course
print(Course.course_trail("Python Fundamentos"))
