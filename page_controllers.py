from abc import ABC, abstractmethod
from shablonizator import render


class PageController(ABC):
    @abstractmethod
    def __call__(self, request):
        pass


class NotFoundPage(PageController):
    def __call__(self, request):
        return '404 Not Found', b'404 page not found'


class IndexPage(PageController):
    def __call__(self, request):
        return '200 OK', render('templates/index.html',
                                say_me='MY HOME PAGE',
                                front_request=request).encode('UTF-8')


class FirePage(PageController):
    def __call__(self, request):
        return '200 OK', render('templates/element.html',
                                object_list=[{'name': 'Flareon', 'number': 1},
                                             {'name': 'Charmander', 'number': 4}],
                                say_me='FIRE PAGE',
                                front_request=request).encode('UTF-8')


class WaterPage(PageController):
    def __call__(self, request):
        return '200 OK', render('templates/element.html',
                                object_list=[{'name': 'Megicarp', 'number': 11},
                                             {'name': 'Blastoise', 'number': 8}],
                                say_me='WATER PAGE',
                                front_request=request).encode('UTF-8')


ROUTES = {
    '/': IndexPage(),
    '/fire': FirePage(),
    '/water': WaterPage(),
    'error_404': NotFoundPage()
}
