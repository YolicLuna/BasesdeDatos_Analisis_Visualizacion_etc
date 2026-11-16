CREATE DATABASE IF NOT EXISTS Practicas;

USE Practicas;

CREATE TABLE IF NOT EXISTS Pixar (
    id INT AUTO_INCREMENT PRIMARY KEY,
    film VARCHAR(50) NOT NULL,
    release_date DATE NOT NULL,
    runtime INT,
    film_rating VARCHAR(10)
)

LOAD DATA INFILE '/var/lib/mysql-files/pixar_films.csv'  -- Ruta del archivo CSV en el servidor MySQL
INTO TABLE Pixar    -- Nombre de la tabla a la que se importarán los datos
FIELDS TERMINATED BY ','    -- Separador de campos en el archivo CSV
ENCLOSED BY '"'     -- Carácter que encierra los campos del archivo CSV
LINES TERMINATED BY '\n'    -- Separador de líneas en el archivo CSV
IGNORE 1 ROWS   -- Ignorar la primera fila (encabezados)
(@id, @film, @release_date, @runtime, @film_rating)   -- Variables temporales para almacenar los datos importados
SET     -- Asignar los valores a las columnas de la tabla, manejando valores nulos
runtime = NULLIF(@runtime, 'NA'), -- Convertir 'NA' a NULL para la columna runtime
film = @film,       -- Asignar el valor de la variable temporal a la columna film
release_date = @release_date,   -- Asignar el valor de la variable temporal a la columna release_date
film_rating = @film_rating;     -- Asignar el valor de la variable temporal a la columna film_rating


SELECT * FROM Pixar;    -- Verificar que los datos se hayan importado correctamente


 -- Consultar películas con duración entre 90 y 100 minutos
SELECT film 
FROM Pixar 
WHERE runtime 
BETWEEN 90 AND 100;


-- Consultar las 5 películas con menor duración en las que la duración no sea un valor nulo
SELECT film, release_date, runtime 
FROM Pixar
WHERE runtime IS NOT NULL
ORDER BY runtime 
ASC LIMIT 5;


-- Consultar películas estrenadas entre 1990 y 2000 con clasificación 'G', ordenadas por duración descendente
SELECT film, runtime, film_rating
FROM Pixar
WHERE release_date > '1990-01-01' AND release_date < '2000-12-31'
ORDER BY runtime DESC;


-- Consultar las diferentes clasificaciones de películas disponibles en la tabla Pixar
SELECT DISTINCT film_rating
FROM Pixar;


-- Consultar películas cuyo título contenga la palabra 'TOY'
SELECT * 
FROM Pixar
WHERE film LIKE '%TOY%';


-- Contar el número de películas por cada clasificación de película
SELECT COUNT(*) AS total_movies, film_rating
FROM Pixar
GROUP BY film_rating;

-- Verificar si la película 'Cars' está disponible en la tabla
SELECT IF (
    EXISTS(SELECT film FROM Pixar WHERE film = "Cars"),
    'Disponible',
    'No disponible'
) AS Resultado;


DROP TABLE IF EXISTS Pixar; -- Eliminar la tabla Pixar después de las consultas