
<!---

      ___       ___           ___           ___
     /\__\     /\  \         /\  \         /\  \
    /:/  /    /::\  \       /::\  \       /::\  \
   /:/  /    /:/\:\  \     /:/\:\  \     /:/\:\  \
  /:/  /    /::\~\:\  \   /:/  \:\  \   /:/  \:\  \
 /:/__/    /:/\:\ \:\__\ /:/__/_\:\__\ /:/__/ \:\__\
 \:\  \    \/__\:\/:/  / \:\  /\ \/__/ \:\  \ /:/  /
  \:\  \        \::/  /   \:\ \:\__\    \:\  /:/  /
   \:\  \       /:/  /     \:\/:/  /     \:\/:/  /
    \:\__\     /:/  /       \::/  /       \::/  /
     \/__/ __ _\/__/__ _ _ __\/____   ___ _\/__/ 
        | '_ ` _ \ / _` | '_ \| '_ \ / _ \ '__|
        | | | | | | (_| | |_) | |_) |  __/ |
        |_| |_| |_|\__,_| .__/| .__/ \___|_|
                        | |   | |
                        |_|   |_|

-->

## LAGO mapper

Realiza un mapa de los sitios del proyecto [LAGO](http://lagoproject.net/) en en America Latina, junto con la grafica que coresponde a la rigidez geomagnética local del sitio. 

## Uso

Desde la terminal correr:

``python LAGOmapa-sitios.py DATOS_DE_LOS_SITIOS.dat``

el formato del archivo DATOS_DE_LOS_SITIOS debe ser como el que se muestra en la cabecera del archivo ``DatosRC.dat``: Nombre, altura, Lat, Long, Status, R_U, R_C, R_L,

Los datos son ordenados por ``sorteador.py`` para que aparezcan segun su latitud

## Autor

Arturo Núñez, Versión original en: [este enlace](https://github.com/luturonunca/LAGOmaps.git)
