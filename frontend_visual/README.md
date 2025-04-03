Este proyecto es una interfaz visual para la gestión de reservas de vuelos. Está desarrollado utilizando HTML, CSS y JavaScript para ofrecer una experiencia de usuario sencilla e intuitiva.

Índice
Descripción del Proyecto

Estructura del Proyecto

Requisitos Previos

Instalación y Ejecución

Tecnologías Utilizadas

Funcionalidades Principales

Estructura de Archivos

Contribución

Licencia

Descripción del Proyecto
El Sistema de Gestión de Reservas Aéreas permite a los usuarios buscar vuelos ingresando una ciudad de origen, un destino y una fecha específica. La interfaz proporciona una experiencia de usuario amigable y moderna, con un diseño atractivo y accesible.

Este sistema es una solución visual que más adelante puede integrarse con un backend en FastAPI para gestionar las reservas de manera dinámica.

Estructura del Proyecto
El proyecto está organizado de la siguiente manera:

graphql
Copiar
Editar
frontend_visual/
│── assets/            # Contiene imágenes y recursos estáticos
│── scripts/           # Archivos JavaScript con la lógica de la aplicación
│   ├── main.js        # Archivo principal con la lógica de búsqueda
│── styles.css         # Archivo de estilos CSS
│── index.html         # Página principal de la aplicación
│── README.md          # Documentación del proyecto
Requisitos Previos
Antes de ejecutar la aplicación, asegúrate de cumplir con los siguientes requisitos:

Tener instalado Node.js (v14 o superior). Puedes verificarlo con:

sh
Copiar
Editar
node -v
Tener npm instalado (v6 o superior). Puedes verificarlo con:

sh
Copiar
Editar
npm -v
Instalación y Ejecución
Para ejecutar la aplicación localmente, sigue estos pasos:

Clonar el repositorio (si aplica):

sh
Copiar
Editar
git clone https://github.com/tu-usuario/gestion-reservas-aereas.git
cd gestion-reservas-aereas/frontend_visual
Abrir la terminal y dirigirse al directorio del frontend:

sh
Copiar
Editar
cd C:\Users\xioma\OneDrive\Documentos\GestionReservasAereas\frontend_visual
Ejecutar un servidor local con npx serve:

sh
Copiar
Editar
npx serve
Si no tienes serve, instálalo con:

sh
Copiar
Editar
npm install -g serve
Abrir en el navegador:
Una vez que el servidor esté en ejecución, abre tu navegador y visita:

arduino
Copiar
Editar
http://localhost:3000/
Tecnologías Utilizadas
El proyecto ha sido desarrollado con las siguientes tecnologías:

HTML5: Para la estructura de la interfaz.

CSS3: Para los estilos y el diseño visual.

JavaScript (ES6+): Para agregar interactividad.

Funcionalidades Principales
Búsqueda de vuelos mediante la selección de:

Ciudad de origen

Ciudad de destino

Fecha del vuelo

Interfaz amigable y responsive.

Estructura modular para facilitar futuras integraciones con un backend.

Estructura de Archivos
1. index.html
Este archivo contiene la estructura principal de la página web, incluyendo los formularios para la búsqueda de vuelos y la referencia a los archivos CSS y JavaScript.

2. styles.css
Define los estilos visuales de la aplicación, asegurando una apariencia limpia y moderna.

3. scripts/main.js
Maneja la lógica de la búsqueda de vuelos y las interacciones del usuario.

4. assets/
Carpeta que almacena imágenes y otros recursos gráficos utilizados en la aplicación.

Contribución
Si deseas contribuir a este proyecto, sigue estos pasos:

Haz un fork del repositorio.

Crea una nueva rama con el nombre de tu funcionalidad o corrección.

Realiza los cambios y haz un commit con una descripción clara.

Envía un pull request para revisión.