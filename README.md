# How was this made?

For this project, I mostly followed the instructions provided by a YouTuber named Linkfy, who made a video creating his own Pokédex.
Although I'm not the biggest Pokémon fan, I thought it would be cool to give it a shot, since I had just started using Flutter and I wandted to try Flet. 

This is a very simple project, just one file was necessary. 

# How does it work?

Well, this project is quite simple.
Flet lets you build a UI, in whih I implemented whe widgets and styles for it to look like a Retro Pokédex.
The better part in my opinion is being able to make requests to an API (The PokéAPI), and turning the results of the petition into visible content in the screen (Text, images...)

For this part, we use asynchronous functions, which make the program able to run whilst the functions is running on the background.
Otherwise, the program would just wait until the function is done and keep udating the UI (Which is not what we want).



# Dependencies

To be able to run this in your local PC, you first need to download Python interpreter, then also get the following libraries:

+ Flet
+ Asyncio
+ AIOHTTP

you can install them by typing this on your terminal:
```
pip install flet
pip install asyncio
pip install aiohttp
```

## Acknowledgements

Linkfy was the original author of this idea.

https://www.youtube.com/@Linkfydev

I recommend checking his channel if you were interested in this project.