# CLASSES
class Clas:
    # Constructor, init project
    def __init__(self):
        self.classes = []

    def add_class(self, classes_in_file):
        for clas in classes_in_file:
            self.classes.append(clas)
            clas_container = self.get_class_container(clas)

    def get_class_container(self, clas):
        print(str(clas.name))
        print(clas.modifiers)
        print(clas.name)
        print(clas.extends)
        print(clas.implements)
        print(clas.body)
        #           Iterract thru body elements
        print("Elements:")
        for element in clas.body:
            print(element.modifiers)
            print(element.type)

            print("END OF CLASS")
    def format_to_plantuml(self, classList):
        pass

    def write_to_file(self, fileHandler):
        pass