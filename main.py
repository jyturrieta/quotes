import tweepy
import random
import time

# Twitter API credentials

api_key="8COhm46YGyOKQWzKB67QAwAqM"
api_secret="2Lv3bb2znhCHGv7poeklu7Nx0Cca2M0KPKdbV69P786wg9gVDG"
bearer_token="AAAAAAAAAAAAAAAAAAAAAFVwwQEAAAAAvKRGfH7DghLnppfQDbogbF3sGSI%3Da53Y2QX7L20r5tR2Op2peXpgkDPxa9wwwxysXheLNAJFExESbH"
access_token="1836080823054831616-Uuauw93hVnckfu3UAanxPxBt3Tvg5C"
access_token_secret="tS3RlRGSrHNuW3XsEGA75z2gjfZOxI9pnazaZ5pkU5p3n"


client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)


quotes = [
    "WE ARE THE CHAMPIOOOOOOONS!!! WE ARE THE CHAAAAAAAMPIOOOOOOOOOONS!!!",
    "Thank you! Fantastic job, fantastic!. All season. All season. Thank you for all these years, It has been a pleasure for me to work with you with this success.",
    "OK, he pushed me off the track. I think you have to leave space. ALL THE TIME YOU HAVE TO LEAVE SPACE.",
    "Michael Schumacher fue el mayor rival que he tenido en mi carrera. Fue un profesor para mi en muchas cosas.",
    "Ganar el tercer Mundial significaría mucho en términos de dejar un legado, por cómo buscar superar los límites, buscar la excelencia en lo que haces, tener una gran disciplina en la manera en la que planteas la competición sin importar si tienes 19 años, 42 o 43",
    "Estaré más allá de 2022, incluso si el coche no es tan competitivo. Mi plan es estar dos o tres años más",
    "Presioné a Kimi Räikkönen hasta que se le fue todo al carajo",
    "Yo hago de las leyes correctas mis milagros #samurai",
    "Después de lo ocurrido, no volveré a considerar nunca más la Fórmula 1 un deporte",
    
]






while True:
    quote = random.choice(quotes)
    client.create_tweet(text=quote)
    print("Tweeted: ", quote)
    time.sleep(3600)


