# Pokédex functional app using Python

This is a functional desktop application that imitates the OG Pokédex. You can press the two arrows to see the different pokémons and some stats.

## How was this made?

For this project, I mostly followed the instructions provided by a YouTuber named Linkfy, who made a video creating his own Pokédex.
Although I'm not the biggest Pokémon fan, I thought it would be cool to give it a shot, since I had just started using Flutter and I wandted to try Flet. 

This is a very simple project, just one file was necessary. 

## How does it work?

Well, this project is quite simple.
Flet lets you build a UI, in whih I implemented whe widgets and styles for it to look like a Retro Pokédex.
The better part in my opinion is being able to make requests to an API (The PokéAPI), and turning the results of the petition into visible content in the screen (Text, images...)

For this part, we use asynchronous functions, which make the program able to run whilst the functions is running on the background.
Otherwise, the program would just wait until the function is done and keep udating the UI (Which is not what we want).


## Dependencies

To be able to run this in your local PC, you first need to download the Python interpreter, then also get the following libraries:

+ Flet
+ Asyncio
+ AIOHTTP

you can install them by typing this on your terminal:
```
pip install flet
pip install asyncio
pip install aiohttp
```

## Personal thoughts

This project made me understand better how the UI world works.
I had rarely used async functions in my projects before I made this one, so it helped me understan how they work (though I sure could do my research, since I can't say I'm a master using them...)

Overall, this was a fun thing to code, so I recommend trying to code it by yourself (you can follow the tutorial I mentioned).
I'm sure this project will make new coders get better at what they do.



### Acknowledgements

Linkfy was the original author of this idea.

https://www.youtube.com/@Linkfydev

I recommend checking out his channel if you were interested in this project.