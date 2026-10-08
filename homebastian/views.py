from django.shortcuts import render


def inicio(request):
    datos_peliculas = [
        {'titulo': 'viernes 13', 'año': 1980, 'imagen': 'images/viernes.PNG', 'genero': 'Slasher'},
        {'titulo': 'terrifier', 'año': 2016, 'imagen': 'images/terrifier.PNG', 'genero': 'Terror'},
        {'titulo': 'SAW', 'año': 2004, 'imagen': 'images/jigsaw.PNG', 'genero': 'Terror'},
        {'titulo': 'alien', 'año': 1979, 'imagen': 'images/alien.PNG', 'genero': 'Ciencia ficción'},
        {'titulo': 'halloween', 'año': 1978, 'imagen': 'images/hallo.PNG', 'genero': 'Slasher'},
        {'titulo': 'pesadilla en la calle elm', 'año': 1984, 'imagen': 'images/pesadilla.PNG', 'genero': 'Terror'},
        {'titulo': 'freddry vs jason', 'año': 2003, 'imagen': 'images/freddyjason.PNG', 'genero': 'Slasher'},
        {'titulo': 'scary movie', 'año': 2000, 'imagen': 'images/scarymovie.PNG', 'genero': 'Comedia'},
        {'titulo': 'predator', 'año': 1987, 'imagen': 'images/preda.PNG', 'genero': 'Acción'},
        {'titulo': 'masacre en texas', 'año': 1974, 'imagen': 'images/texas.PNG', 'genero': 'Terror'},
    ]

    generos = [
        {
            'ancla': 'terror',
            'nombre': 'Terror clásico',
            'descripcion': 'Películas de miedo',
            'peliculas': [
                pelicula for pelicula in datos_peliculas
                if pelicula['genero'] in {'Terror', 'Ciencia ficción', 'Acción', 'Comedia'}
            ],
        },
        {
            'ancla': 'slasher',
            'nombre': 'Slasher',
            'descripcion': 'Sangre, suspense y asesinos que dejan huella en la historia del cine.',
            'peliculas': [
                pelicula for pelicula in datos_peliculas
                if pelicula['genero'] == 'Slasher'
            ],
        },
    ]

    return render(request, 'homebastian.html', {'generos': generos})