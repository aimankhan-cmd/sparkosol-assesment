from fastapi import FastAPI, Body, Depends

from app.model import PostSchema, UserSchema
from app.auth.auth_bearer import JWTBearer
from app.auth.auth_handler import signJWT

from fastapi.middleware.cors import CORSMiddleware
import requests


# Posts Dict 
posts = [
    {
        "id": 1,
        "title": "test",
        "content": "backend assesment Task 3"
    }
]

# User Dict 
users = []

#initilize FastAPI
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Welcome index page"] )
async def read_root() -> dict:
    return {"message": "Welcome to JWT backend assesment!."}

@app.post("/user/signup", tags=["User Signup to get token"])
async def create_user(user: UserSchema = Body(...)):
    users.append(user) 
    return signJWT(user.email)


@app.post("/posts", dependencies=[Depends(JWTBearer())], tags=["Add Post"])
async def add_post(post: PostSchema) -> dict:
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {
        "data": "post added."
    }


@app.get("/temperature/{city}", dependencies=[Depends(JWTBearer())], tags=["Check City Temperature"])
async def temperature(city):
    api_key ='4f951dbca8834fc03ebe458753c8c881'
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    # Give city name 
    city_name = city
    # # complete url address
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
  
    response = requests.get(complete_url).json()
    
    # #convert temp to Celsius
 
    min_temp = round(response['main']['temp_min'] - 273.15, 3)
    max_temp = round(response['main']['temp_max'] - 273.15, 3)
    

    # #output in string format must add xlass htmlresponse 
    result =  f"{city}'s Max temperature in Celsius {max_temp}°C and  Min temperature in Celsius {min_temp}°C."

    return {
        " City Name": {city},
        " Max temperature in °C":{max_temp},
        " Min temperature in °C":{min_temp}
    }

    #openApi response
    
    #return (city,min_temp, max_temp)
  
   


