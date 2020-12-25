## Знакомлюсь с JWT аутентификацией

Залогиниться, т.е. получить токен:
`http://localhost:8000/api/token/`

Обновить токен с refresh-экземпляром:
`http://localhost:8000/api/token/refresh`

В заголовке авторизации необходимо передавать JWT-токен с префиксом `Bearer Token`. Он должен во всех остальных запросах, так как для всех обработчиков установлен параметр **isAuthenticated=True**.  

Основные модели *ViewSet* согласно возможностям [DefaultRouter](https://www.django-rest-framework.org/api-guide/routers/#defaultrouter):  
`http://127.0.0.1:8000/api/posts/`  
`http://127.0.0.1:8000/api/user/`  
`http://127.0.0.1:8000/api/profile/`

Поставить лайк посту или снять лайк:  
`http://127.0.0.1:8000/api/posts/*id*/like_post/`  
`http://127.0.0.1:8000/api/posts/*id*/unlike_post/`  

