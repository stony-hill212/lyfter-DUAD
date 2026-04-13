1. •	Squiggle API: Ofrece: retorna una lista de fuentes de datos relacionadas al football de reglas australiano (AFL), con datos como tabla, marcadores, fechas de encuentros y demás, por medio de un archivo JSON.
   •	JSON placeholder: Datos falsos para crear tests y hacer prototipos.

2.
    Métodos:
   GET, PUT, POST y DELETE.
  
3.  Get data (GET): {{base_url_squiggle}}/?q=sources
  {
    "sources": [
        {
            "url": "https://live.squiggle.com.au/",
            "icon": "/wp-content/themes/squiggle/assets/images/Squiggle.png",
            "id": 1,
            "name": "Squiggle"
        }

   Get Games (GET): {{base_url_squiggle}}/?q=games&year=2020
  {
    "games": [
        {
            "is_final": 0,
            "year": 2020,
            "updated": "2020-03-19 22:02:03",
            "date": "2020-03-19 19:40:00",
            "round": 1,

  Post data (POST): {{base_url_json}}/posts
  {
    "title": "Practice Post",
    "body": "Learning Postman step by step",
    "userId": 1,
    "id": 101
}

 Update post (PUT): {{base_url_json}}/posts/1
 {
    "id": 1,
    "title": "Updated title",
    "body": "Now I undestand PUT",
    "userId": 1
}
Delete post (DELETE): {{base_url_json}}/posts/1

{}

4. Aprendi mas sobre el tema de APIs y la metodologia CRUD (create, read, update, delete)
mediante todas las herramintas e instrucciones brindadas durante el curso lectivo y la asignación.
