document.getElementById('linkSubirManga').addEventListener('click', function(event) {
    event.preventDefault();
    document.getElementById('formularioSubirManga').style.display = 'block';
});

document.getElementById('btnCancelar').addEventListener('click', function() {
    document.getElementById('formularioSubirManga').style.display = 'none';
});

document.getElementById('formSubirManga').addEventListener('submit', function(event) {
    event.preventDefault(); // Evitar el envío del formulario

    // Obtener datos del formulario
    var titulo = document.getElementById('titulo').value;
    var capitulos = document.getElementById('capitulos').value;
    var estado = document.getElementById('estado').value;
    var imagen = document.getElementById('imagen').files[0];

    // Validar los datos (aquí puedes agregar tus propias validaciones)

    // Guardar los datos en el Local Storage
    var manga = {
        titulo: titulo,
        capitulos: capitulos,
        estado: estado,
        imagen: imagen.name // Guardar solo el nombre de la imagen para referencia
    };
    var mangas = JSON.parse(localStorage.getItem('mangas')) || [];
    mangas.push(manga);
    localStorage.setItem('mangas', JSON.stringify(mangas));

    // Subir la imagen a través de AJAX o realizar otras acciones necesarias

    // Limpiar el formulario o hacer otras acciones necesarias
    document.getElementById('formSubirManga').reset();
    document.getElementById('formularioSubirManga').style.display = 'none'; // Ocultar el formulario de subida

    // Mostrar los mangas en el contenedor
    mostrarMangas();

    alert('Manga subido exitosamente.');
});

function mostrarMangas() {
    var mangas = JSON.parse(localStorage.getItem('mangas')) || [];
    var mangasContainer = document.getElementById('mangasContainer');
    mangasContainer.innerHTML = ''; // Limpiar el contenedor

    mangas.forEach(function(manga, index) {
        var mangaElement = document.createElement('div');
        mangaElement.classList.add('manga');
        mangaElement.innerHTML = `
            <h3>${manga.titulo}</h3>
            <p>Número de Capítulos: ${manga.capitulos}</p>
            <p>Estado del Manga: ${manga.estado}</p>
            <img src="${manga.imagen}" alt="${manga.titulo}"/>
            <button onclick="editarManga(${index})">Editar</button>
            <button onclick="eliminarManga(${index})">Eliminar</button>
        `;
        mangasContainer.appendChild(mangaElement);
    });
}

function editarManga(index) {
    var mangas = JSON.parse(localStorage.getItem('mangas')) || [];
    var manga = mangas[index];
    if (manga) {
        document.getElementById('titulo').value = manga.titulo;
        document.getElementById('capitulos').value = manga.capitulos;
        document.getElementById('estado').value = manga.estado;
        document.getElementById('imagen').value = ''; // Limpiar el campo de imagen
        mangas.splice(index, 1); // Eliminar el manga antiguo
        localStorage.setItem('mangas', JSON.stringify(mangas));
        document.getElementById('formularioSubirManga').style.display = 'block'; // Mostrar el formulario para editar
    }
}

function eliminarManga(index) {
    var mangas = JSON.parse(localStorage.getItem('mangas')) || [];
    mangas.splice(index, 1); // Eliminar el manga
    localStorage.setItem('mangas', JSON.stringify(mangas));
    mostrarMangas(); // Mostrar los mangas actualizados
    alert('Manga eliminado exitosamente.');
}

// Mostrar mangas al cargar la página
document.addEventListener('DOMContentLoaded', mostrarMangas);
