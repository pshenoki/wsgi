from abc import ABC, abstractmethod


class FrontController(ABC):
    @abstractmethod
    def __call__(self, request):
        pass


class TopFront(FrontController):
    def __call__(self, request):
        request['top_page'] = 'Привет, я фронт контроллер с заголовком страницы'


class BottomFront(FrontController):
    def __call__(self, request):
        request['bottom_page'] = 'Привет, я фронт контроллер с подвалом страницы'


FRONTS = [TopFront(), BottomFront()]
