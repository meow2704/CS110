# omyaasree
# cs110
# sorting a list of classes

class Book:
    def __init__(self, name, num_pages):
        self._name = name
        self._num_pages = num_pages

    def set_name(self, name):
        self.__name = name

    def set_num_pages (self, num_pages):
        self.__num_pages = num_pages

    def get_name(self):
        return self._name

    def get_num_pages(self):
        return self._num_pages

    def __str__(self):
        return f"Book: {self._name}, Pages: {self._num_pages}"
