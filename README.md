# flask-bookmark-api

## packages

✨ flask 

✨ werkzeug.security

✨ flask_jwt_extended

✨ flasgger 

✨ flask_sqlalchemy 

✨ validators

✨ flask.json

## endpoints

| Endpoint  | Http Request Method  | Body  | Params  | Args | Description  |
| ------------ | ------------ | ------------ | ------------ | ------------ | ------------ |
| /api/v1/auth/register  |  POST | {"username":"username","email":"example@mail.com","password":"M12345."}  | Empty  | Empty | It allows us to register the user. |
| /api/v1/auth/login  |  POST | {"email":"example@mail.com","password":"M12345."}  | Empty  | Empty |It allows us to login.
| /api/v1/auth/me  | GET  | Empty  | Empty  | Empty | It returns our username and email information. |
| /api/v1/auth/token/refresh  |  POST | Empty  |  Empty | Empty | Creates a new access token.  |
| /api/v1/bookmarks/  |  GET | Empty  | Empty | page=1&per_page=5  | Get bookmarks by pagination. |
| /api/v1/bookmarks/   | POST  | {"body":"Comlaf","url":"comlaf.com"}   | Empty  | Empty  | Creates a bookmark. |
| /api/v1/bookmarks/:id | GET | Empty | id:int | Empty |  Get the bookmark by id. | 
| /api/v1/bookmarks/:id | PUT & PATCH | Empty | id:int | Empty | Update bookmark by id. |
| /api/v1/bookmarks/:id | DELETE | Empty | id:int | Empty | Delete bookmark by id. |
| /api/v1/bookmarks/stats | GET | Empty | Empty | Empty | Get bookmarks with visit information. |
