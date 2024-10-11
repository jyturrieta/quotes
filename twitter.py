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
    "The way I drive, the way I handle a car, is an expression of my inner feelings. ~ (Lewis Hamilton).",
    "It’s important for everyone to stand up for what they believe in. ~ (Lewis Hamilton).",
    "Still we rise ~ (Lewis Hamilton).",
    "That’s for all the kids out there who dream the impossible. You can do it too man! I believe in you guys! Thank you so much everyone for your support. ~ (Lewis Hamilton).",
    "You just need to be accepted for who you are and be proud of who you are and that is what I’m trying to do. ~ (Lewis Hamilton).",
    "That was a frickin' good lap! ~ (Lewis Hamilton).",
    "That was I'm talking about! WOO, YES! ~ (Lewis Hamilton).",
    "(Toto Wolff) Lewis, this is Toto. This was the most EPIC lap I have ever seen around here! \n (Lewis Hamilton) Ha ha! Thank you man."
    "That's some bullshit! Where is that in the rule book? ~ (Lewis Hamilton).",
    "(Bono, after winning British GP 2024) GET IN THERE LEWIS! YOU THE MAN, YOU THE MAN! \n (Lewis Hamilton) Phew! Thank you so much guys. It means a lot to get this one. A big thank you for all the fans here. Love you guys.",
    "I’m not a celebrity; I’m a normal person. ~ (Lewis Hamilton).",
    "I’ve accomplished more than I ever dreamed. But I’m hungry for more. ~ (Lewis Hamilton).",
    "Why you stopped George? That was a mistake man ~ (Lewis Hamilton).",
    "I like taking risks. I like trying new things, whether it be style or restaurants or whatever. ~ (Lewis Hamilton).",
    "It takes me forever to read a book. I have such a small attention span. ~ (Lewis Hamilton).",
    "I started watching Formula 1 with my dad when I was just four or five years old. I loved cars. ~ (Lewis Hamilton).",
    "You can knock me down, but I get up twice as strong. ~ (Lewis Hamilton).",
    "I don’t think you can fully call yourself a vegan if you wear leathers. ~ (Lewis Hamilton).",
    "I’m happy to race against anyone. ~ (Lewis Hamilton).",
    "I hate losing. It doesn’t matter if it’s racing or playing Ping-Pong – I hate it. ~ (Lewis Hamilton).",
    "I train to quite an intense level because Formula 1 is so physical – the G-forces, the demands on your body. Your heart rate is 150, 160 through the whole race. On qualifying lap, your heart rate can be up to 180, 190, under tough conditions. ~ (Lewis Hamilton).",
    "Tupac is my favorite artist, and he had mad style. ~ (Lewis Hamilton).",
    "Lots of other drivers like cycling, but I’m not so keen. I have some really cool bikes, but I’m just not in love with it like Jenson Button and Fernando Alonso. ~ (Lewis Hamilton).",
    "I think my style is definitely urban chic. I love mixing street style with the high-end luxury brands, like Gucci, for example. Quite fun. ~ (Lewis Hamilton).",
    "Since I started driving in F1 in 2006-07, the cars have got slower and easier to drive. ~ (Lewis Hamilton).",
    "If Ferrari wanted me, they would have approached me. I want to work with people who want me. If they don’t want me, it is no problem. ~ (Lewis Hamilton).",
    "What people tend to forget is the journey that I had getting to Formula One. There were plenty of years where I had to learn about losing and having bad races. ~ (Lewis Hamilton).",
    "My dad wanted me to have a better life than he had ever had. He wanted us to succeed so badly. And I never wanted to let him down. ~ (Lewis Hamilton).",
    "I certainly lead a different life from many people. I have a great life that I am thankful for, and I like travelling. ~ (Lewis Hamilton).",
    "When I’m driving, the fewer distractions there are, the better it is to focus on the job in hand. ~ (Lewis Hamilton).",
    "Sometimes, I arrive at races more energetic and clear-minded than ever, and then I have a terrible race. And the opposite is also true. ~ (Lewis Hamilton).",
    "I feel like people are expecting me to fail; therefore, I expect myself to win. ~ (Lewis Hamilton).",
    "I’m willing to take any amount of pain to win. ~ (Lewis Hamilton).",
    "I think it’s a shame that people are so quick to put you in a box; sometimes it’s as if you do one thing, and that’s all you’re allowed to do. ~ (Lewis Hamilton).",
    "I don’t believe I have a playboy life. ~ (Lewis Hamilton).",
    "Going for a really long run, a bike ride, or cross-country skiing helps me get away from all the noise. I tell myself, ‘The pain you’re feeling, just enjoy it because it’s going to help you across that finish line first.’ If you’re having a crap day, go for a run. It makes a big difference. ~ (Lewis Hamilton).",
    "Every person I have met who has gone vegan says it is the best decision they have ever made. ~ (Lewis Hamilton).",
    "I love all of the Marvel comics movies. ~ (Lewis Hamilton).",
    "I usually sleep four or five hours, but when you are training, you need more than that. ~ (Lewis Hamilton).",
    "There have been some ups and downs. I’ve not always had it my own way. That’s the way racing is supposed to be. ~ (Lewis Hamilton).",
    "Every lap is different. ~ (Lewis Hamilton).",
    "My immediate family are from the West Indies – from Trinidad and Grenada – and I have relatives all over the Caribbean. ~ (Lewis Hamilton).",
    "It is open for anyone to have freedom of speech, and I guess we can all play a role in trying to make a difference in the world. Particularly if your leader is not helping in that area. ~ (Lewis Hamilton).",
    "I listen to music before every race. Generally, there will be a song I’ll get into over the weekend, and I play it all weekend, particularly when I’m getting ready for a race. ~ (Lewis Hamilton).",
    "Whether it’s with my engineers in the team, my home life, or my friends, I don’t like things to get complicated – and one good example would be the steering wheel in my Mercedes Formula 1 car. ~ (Lewis Hamilton).",
    "I enjoy trying to develop a car and Mercedes are one of the biggest car manufacturers in the world. ~ (Lewis Hamilton).",
    "People need to remember that I am the first black driver in F1, so I am obviously going to be different to past drivers. ~ (Lewis Hamilton).",
    "If I’d won every single race and got pole everywhere, that would just be boring. It would suck. Where’s the fun in that? ~ (Lewis Hamilton).",
    "I have so much energy. I train, I travel, I’m learning about music and fashion, reading a lot. I don’t want to miss anything. I want to experience everything. ~ (Lewis Hamilton).",
    "Ayrton Senna was my favorite driver who I wanted to be like. ~ (Lewis Hamilton).",
    "Everyone has complicated lives, but the more you can simplify it and make it work for you, the better it is going to be. ~ (Lewis Hamilton).",
    "I don’t aspire to be like other drivers – I aspire to be unique in my own way. ~ (Lewis Hamilton).",
    "As a driver, you’ve always got to believe in your heart that you’ve got what it takes to win it. You’ve always got to believe in yourself. You’ve always got to arrive on the day and believe it can happen. You’ve always got to believe in the positives. ~ (Lewis Hamilton).",
    "Everyone loves a winner. That’s just how the world is. And Ayrton Senna was one of the greatest winners this sport has ever had. ~ (Lewis Hamilton).",
    "On my back, I have the cross and angel wings: rise above it, no matter what life throws at you. And also, you know, Jesus rose from the grave. ~ (Lewis Hamilton).",
    "There are times when you are growing through experiences, but sometimes there is a point of diminishing returns in terms of growth. ~ (Lewis Hamilton).",
    "I want to crush everyone. I want to outsmart everyone. ~ (Lewis Hamilton).",
    "I can't believe guys, you screw my race man! ~ (Lewis Hamilton).",
    "I don’t like to read fiction. I like to learn something when I’m reading. ~ (Lewis Hamilton).",
    "I’m an extremist so I’m either hated or loved. I think it’s down to when I first got to Formula One not always knowing what I was saying, saying things that mean one thing but people were taking the other way and then people don’t forget. ~ (Lewis Hamilton).",
    "My daily breakfast is two poached eggs in the morning with half an avocado, and I get to have half a piece of toast. ~ (Lewis Hamilton).",
    "I had a lot of racism growing up where I grew up. Bullied at school. It definitely encouraged me. It’s like battle wounds – you come out the other side, and it just makes you tougher. ~ (Lewis Hamilton).",
    "F1 is about the best drivers competing against each other for the best teams producing the best cars they can. ~ (Lewis Hamilton).",
    "I love my ink. They all have a meaning. I’m very strong in my faith, so I wanted to have some religious images. I’ve got Pieta, a Michelangelo sculpture of Mary holding Jesus after he came off the cross, on my shoulder. A sacred heart on my arm. Musical notes because I love music. The compass on my chest is there because church is my compass. ~ (Lewis Hamilton).",
    "When I think about greatness I just know Ayrton Senna. He was great. ~ (Lewis Hamilton).",
    "My job is to get into the car and drive as fast and as well as possible. ~ (Lewis Hamilton).",
    "Generally, I hate training – just like most people, I guess. I try to make it fun and varied. ~ (Lewis Hamilton).",
    "I have always wanted to learn the piano, but because I’ve been travelling so much, I just have not been able to fit it in. ~ (Lewis Hamilton).",
    "Music is my escape. I love to listen to it before racing. It’s great for the soul. ~ (Lewis Hamilton).",
    "When you’re doing something and someone is telling you what to do, you can only take it so far. ~ (Lewis Hamilton).",
    "As a kid, I wanted to be a race car driver, but I wanted to be Michael Jackson, too. ~ (Lewis Hamilton).",
    "You never know what to expect. If you want to survive in the sport, you’ve got to adapt. ~ (Lewis Hamilton).",
    "I think that people will remember me as a driver who made a difference in the sport and in the world – as a positive influence. ~ (Lewis Hamilton)."
]






while True:
    quote = random.choice(quotes)
    client.create_tweet(text=quote)
    print("Tweeted: ", quote)
    time.sleep(3600)


