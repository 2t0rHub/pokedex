

#Comando para entrar en el Entorno virtual : .\venv\Scripts\activate   

'''--- SI QUIERES COMPRIMIRLO A UN .exe, HAZ LO SIGUIENTE: ---'''

#  pip install pyinstaller
#  flet pack .\main.py 

import flet as ft
import math
import aiohttp
import asyncio

pokemon_actual = 0

async def main(page: ft.Page):
    page.window.width = 360
    page.window.height = 640
    page.window.resizable = False
    page.padding = 0
    page.fonts = { # Fuente retro de pokémon
        "zpix" : "https://github.com/SolidZORO/zpix-pixel-font/releases/download/v3.1.8/zpix.ttf"
    }

    page.theme = ft.Theme(font_family = "zpix")


    '''--- DEFINICIÓN DE LAS FUNCIONES ---'''

    async def parpadeo_boton_azul():
        while True:
            await asyncio.sleep(0.7)
            boton_azul.bgcolor = ft.colors.LIGHT_BLUE_ACCENT_400
            page.update()
            await asyncio.sleep(0.3)
            boton_azul.bgcolor = ft.colors.BLUE
            page.update()
            

    async def peticion(url):
        # Devuelve un GET en formato JSON a una URL
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.json()

    async def evento_get_pokemon(e: ft.ContainerTapEvent):

        global pokemon_actual # Consulta el valor de la variable global 

        if e.control == flecha_sup:
            pokemon_actual += 1
        else:
            pokemon_actual -= 1

        numero = (pokemon_actual % 150) +1
        resultado = await peticion(f"https://pokeapi.co/api/v2/pokemon/{numero}")
        # print(resultado)

        nombre = f"Name: {resultado['name'].capitalize()}"

        info = f"Abilities: "
        for elemento in resultado['abilities']:
            habilidad = elemento['ability']['name'].capitalize()
            info += f"\n  {habilidad}"
        
        info += "\nTypes: "
        for elemento in resultado['types']:
            tipo = elemento['type']['name'].capitalize()
            info += f"\n  {tipo}"

        info += f"\nHeight: {resultado['height']}"

        nombre_pokemon.value = nombre
        info_pokemon.value = info # Cambia el texto de la Pokédex

        sprite_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{numero}.png"
        imagen.src = sprite_url
        page.update()

    '''--- CREACIÓN DE LAS COLUMNAS ---'''

    #Columna superior con los items

    boton_azul = ft.Container(width = 35, height = 35, left = 2.5, top = 2.5, bgcolor = ft.colors.BLUE, border_radius = 25)

    boton_grande = ft.Stack([
        ft.Container(width = 40, height = 40, bgcolor = ft.colors.WHITE, border_radius = 25), #  Borde blanco del Botón
        boton_azul
        ]
    )

    items_superior = [
        ft.Container(boton_grande, width = 40, height = 40),
        ft.Container(width = 20, height = 20, bgcolor = ft.colors.RED, border_radius = 25),        
        ft.Container(width = 20, height = 20, bgcolor = ft.colors.YELLOW, border_radius = 25),        
        ft.Container(width = 20, height = 20, bgcolor = ft.colors.GREEN, border_radius = 25),        
    ]

    superior =ft.Container(content = ft.Row(items_superior), width = 300, height=40, margin = ft.margin.only(top = 40), 
                           bgcolor = ft.colors.BLUE_GREY_200, border_radius = 10)
    

    # Columna del medio con los items

    sprite_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/0.png"

    imagen = ft.Image(src = sprite_url,
                 height = 25, width = 25, scale = 7.5, top = 175/2, left = 275/2)

    stack_centro = ft.Stack([
        ft.Container(width = 300, height = 200, bgcolor = ft.colors.WHITE),
        ft.Container(width = 275, height = 175, top = 12.5, left = 12.5, bgcolor = ft.colors.BLACK, border_radius = 10),
        imagen,
    ])
    
    centro =ft.Container(content = stack_centro, width = 300, height=200, margin = ft.margin.only(top = 40), 
                         bgcolor = ft.colors.BLUE_GREY_200, border_radius = 10)
    
    # Columna inferior

    # ANTIGUO CÓDIGO FLECHAS, HECHO CON UN CANVAS, NO ES LA MEJOR OPCIÓN.

    # triangulo = ft.canvas.Canvas([
    #     ft.canvas.Path([
    #         ft.canvas.Path.MoveTo(17.5, 0),
    #         ft.canvas.Path.LineTo(0, 35),
    #         ft.canvas.Path.LineTo(35, 35),
    #         ft.canvas.Path.Close()
    #         ],
    #         paint = ft.Paint(
    #             style = ft.PaintingStyle.FILL,
    #             stroke_width = 80,
    #             stroke_join = ft.StrokeJoin.ROUND
    #             ),
    #         ),
    # ],
    # width = 40,
    # height = 25,
    # )

    # flechas = ft.Column(controls = [
    #     ft.Container(triangulo, width = 40, height = 40, border = ft.border.all()), # Flecha arriba
    #     ft.Container(triangulo, rotate = ft.Rotate(angle = math.pi), width = 40, height = 40, border = ft.border.all()), # Flecha abajo
    # ],
    # spacing = 0 # Muy importante que no haya espacio entre elementos
    # )

    flecha_sup = ft.IconButton(icon = ft.icons.PLAY_ARROW_ROUNDED, width = 40, height = 40, 
                      rotate = ft.Rotate(1.5 *math.pi), on_click = evento_get_pokemon)
                      
    flecha_inf = ft.IconButton(icon = ft.icons.PLAY_ARROW_ROUNDED, width = 40, height = 40, 
                      rotate = ft.Rotate(math.pi / 2), on_click = evento_get_pokemon)
   
    flechas = ft.Column(controls = [
        flecha_sup,
        flecha_inf
    ],
    spacing = 0
    )

    # Campos de texto
    nombre_pokemon = ft.Text(
        value = "...",
        size = 18,
        )
    
    info_pokemon = ft.Text(
        value = "",
        size = 12
    )

    datos =ft.Row([
        ft.Container(width = 5),
        ft.Column(controls= [
            nombre_pokemon,
            info_pokemon
            ],
            spacing = 0
        )
    ] 
    )

    items_inferior = [
        ft.Container(width = 20), # Margen izquierdo
        ft.Container(datos, width = 200, height = 150,
                    bgcolor = ft.colors.GREEN, border = ft.border.all(), border_radius = 10), # Gran contenedor verde
        ft.Container(width = 10), # Margen derecho
        ft.Container(flechas, width = 40, height = 80),
    ]

    inferior =ft.Container(content = ft.Row(items_inferior, spacing= 5), width = 300, height=200, margin = ft.margin.only(top = 40), border=ft.border.all(), 
                           bgcolor = ft.colors.BLUE_GREY_200, border_radius = 10)

    columnas = ft.Column(spacing = 0, controls = [
        superior,
        centro,
        inferior,
    ])

    #Creación del contenedor
    contenedor = ft.Container(columnas, width = 360, height = 640, bgcolor = ft.colors.BLUE_GREY, 
                               alignment = ft.alignment.top_center)

    page.add(contenedor)
    await parpadeo_boton_azul()

ft.app(target = main)