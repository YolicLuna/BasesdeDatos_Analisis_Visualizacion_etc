USE Alumnos_titulados;

-- Crear la tabla info_titulados
CREATE TABLE info_titulados (
    id_titulado INT PRIMARY KEY AUTO_INCREMENT,
    nombre_universidad VARCHAR(50),
    estado VARCHAR(50),
    nombre_alumno VARCHAR(30),
    carrera VARCHAR(30),
    promedio DECIMAL(3,2),
    ciclo_escolar DATE,
    fecha_inicio DATE,
    fecha_finalizacion DATE
);

-- Crear la tabla alumnos con llave foránea
CREATE TABLE alumnos (
    id_alumno INT PRIMARY KEY AUTO_INCREMENT,
    id_titulado INT,
    nombre_completo VARCHAR(50),
    edad INT,
    telefono VARCHAR(15),
    email VARCHAR(50),
    direccion VARCHAR(100),
    genero ENUM('M', 'F'),
    FOREIGN KEY (id_titulado) REFERENCES info_titulados(id_titulado)
);

-- Insertar 50 registros en la tabla info_titulados
INSERT INTO info_titulados (nombre_universidad, estado, nombre_alumno, carrera, promedio, ciclo_escolar, fecha_inicio, fecha_finalizacion) VALUES
('Universidad Nacional Autónoma de México', 'CDMX', 'María González Pérez', 'Ingeniería en Sistemas', 9.15, '2020-08-01', '2020-08-15', '2024-12-15'),
('Instituto Tecnológico de Monterrey', 'Nuevo León', 'Carlos Rodríguez López', 'Administración de Empresas', 8.87, '2019-08-01', '2019-08-20', '2023-12-10'),
('Universidad de Guadalajara', 'Jalisco', 'Ana Martínez Silva', 'Medicina', 9.45, '2018-08-01', '2018-08-10', '2024-06-20'),
('Instituto Politécnico Nacional', 'CDMX', 'José Luis Hernández', 'Ingeniería Mecánica', 7.92, '2020-08-01', '2020-09-01', '2024-12-20'),
('Universidad Autónoma de Nuevo León', 'Nuevo León', 'Laura Sánchez Morales', 'Psicología', 9.23, '2019-08-01', '2019-08-15', '2023-12-05'),
('Universidad Veracruzana', 'Veracruz', 'Miguel Ángel Torres', 'Derecho', 8.76, '2020-08-01', '2020-08-25', '2024-12-18'),
('Universidad Autónoma de Yucatán', 'Yucatán', 'Sofía Ramírez Castro', 'Arquitectura', 9.01, '2019-08-01', '2019-09-05', '2024-06-15'),
('Universidad de Sonora', 'Sonora', 'Roberto Jiménez Vega', 'Ingeniería Industrial', 5.89, '2020-08-01', '2020-08-30', '2024-12-12'),
('Universidad Autónoma de Sinaloa', 'Sinaloa', 'Gabriela Flores Ruiz', 'Contaduría Pública', 9.34, '2019-08-01', '2019-08-18', '2023-12-08'),
('Universidad de Guanajuato', 'Guanajuato', 'Fernando Castro Mendoza', 'Ingeniería Civil', 5.95, '2020-08-01', '2020-09-10', '2024-12-22'),
('Universidad Autónoma de Chihuahua', 'Chihuahua', 'Valeria Moreno Aguilar', 'Comunicación', 9.12, '2019-08-01', '2019-08-22', '2023-12-15'),
('Universidad Michoacana de San Nicolás', 'Michoacán', 'Diego Vargas Herrera', 'Ingeniería Química', 8.83, '2020-08-01', '2020-08-28', '2024-12-10'),
('Universidad Autónoma de Puebla', 'Puebla', 'Camila Ortega Delgado', 'Biología', 6.27, '2019-08-01', '2019-09-02', '2023-12-20'),
('Universidad Autónoma de San Luis Potosí', 'San Luis Potosí', 'Alejandro Ramos Peña', 'Fisioterapia', 8.91, '2020-08-01', '2020-08-16', '2024-12-14'),
('Universidad de Colima', 'Colima', 'Isabella Cruz Navarro', 'Veterinaria', 9.18, '2019-08-01', '2019-08-25', '2024-06-18'),
('Universidad Autónoma de Querétaro', 'Querétaro', 'Sebastián Medina Rojas', 'Ingeniería en Software', 7.05, '2020-08-01', '2020-09-05', '2024-12-25'),
('Universidad Autónoma de Coahuila', 'Coahuila', 'Natalia Guerrero Ibarra', 'Enfermería', 6.97, '2019-08-01', '2019-08-14', '2023-12-12'),
('Universidad Juárez Autónoma de Tabasco', 'Tabasco', 'Mateo Espinoza Luna', 'Agronomía', 8.88, '2020-08-01', '2020-08-20', '2024-12-08'),
('Universidad Autónoma de Tamaulipas', 'Tamaulipas', 'Valentina Castillo Soto', 'Odontología', 9.31, '2019-08-01', '2019-09-01', '2024-06-25'),
('Universidad Autónoma de Nayarit', 'Nayarit', 'Santiago Morales Rivera', 'Turismo', 8.94, '2020-08-01', '2020-08-18', '2024-12-16'),
('Universidad de Quintana Roo', 'Quintana Roo', 'Emilia Herrera Campos', 'Negocios Internacionales', 9.08, '2019-08-01', '2019-08-28', '2023-12-18'),
('Universidad Autónoma de Baja California', 'Baja California', 'Nicolás Mendoza Reyes', 'Ingeniería Electrónica', 8.86, '2020-08-01', '2020-09-08', '2024-12-20'),
('Universidad Autónoma de Campeche', 'Campeche', 'Regina Vázquez García', 'Nutrición', 9.25, '2019-08-01', '2019-08-12', '2023-12-22'),
('Universidad de Occidente', 'Sinaloa', 'Maximiliano Silva Córdoba', 'Mercadotecnia', 8.79, '2020-08-01', '2020-08-24', '2024-12-11'),
('Universidad Autónoma del Estado de México', 'Estado de México', 'Luciana Peña Maldonado', 'Trabajo Social', 9.19, '2019-08-01', '2019-09-04', '2023-12-25'),
('Universidad Autónoma de Zacatecas', 'Zacatecas', 'Emiliano Acosta Villanueva', 'Minería', 8.93, '2020-08-01', '2020-08-26', '2024-12-13'),
('Universidad Autónoma de Tlaxcala', 'Tlaxcala', 'Victoria Domínguez Salinas', 'Educación', 9.02, '2019-08-01', '2019-08-19', '2023-12-14'),
('Universidad Autónoma de Aguascalientes', 'Aguascalientes', 'Patricio Romero Valdez', 'Sistemas Computacionales', 9.11, '2020-08-01', '2020-09-12', '2024-12-24'),
('Universidad Autónoma de Morelos', 'Morelos', 'Antonella Figueroa Ortiz', 'Química', 8.98, '2019-08-01', '2019-08-16', '2023-12-19'),
('Universidad Autónoma de Hidalgo', 'Hidalgo', 'Leonardo Aguilar Montoya', 'Gastronomía', 8.85, '2020-08-01', '2020-08-22', '2024-12-17'),
('Universidad Autónoma de Durango', 'Durango', 'Renata Cabrera Escobar', 'Diseño Gráfico', 9.07, '2019-08-01', '2019-08-30', '2023-12-16'),
('Universidad Autónoma de Guerrero', 'Guerrero', 'Joaquín Maldonado Herrera', 'Filosofía', 8.91, '2020-08-01', '2020-09-06', '2024-12-19'),
('Universidad Autónoma de Oaxaca', 'Oaxaca', 'Mariana Sandoval Téllez', 'Antropología', 9.29, '2019-08-01', '2019-08-26', '2024-06-22'),
('Universidad Autónoma de Chiapas', 'Chiapas', 'Tadeo Cervantes Muñoz', 'Ingeniería Forestal', 8.87, '2020-08-01', '2020-08-14', '2024-12-21'),
('Universidad del Valle de México', 'CDMX', 'Ariadna Lara Jiménez', 'Relaciones Internacionales', 9.16, '2019-08-01', '2019-09-09', '2023-12-11'),
('Universidad Anáhuac', 'CDMX', 'Gael Medrano Contreras', 'Finanzas', 8.99, '2020-08-01', '2020-08-17', '2024-12-23'),
('Universidad Iberoamericana', 'CDMX', 'Alexa Paredes Vega', 'Diseño Industrial', 6.22, '2019-08-01', '2019-08-21', '2023-12-17'),
('Universidad La Salle', 'CDMX', 'Benjamín Ruiz Moreno', 'Ingeniería Biomédica', 9.04, '2020-08-01', '2020-09-11', '2024-12-26'),
('Universidad Panamericana', 'CDMX', 'Clara Ramírez Guerrero', 'Periodismo', 8.96, '2019-08-01', '2019-08-13', '2023-12-13'),
('Universidad del Claustro de Sor Juana', 'CDMX', 'Thiago Álvarez Ramos', 'Literatura', 9.13, '2020-08-01', '2020-08-19', '2024-12-15'),
('Universidad Tecnológica de México', 'CDMX', 'Daniela Chávez Fernández', 'Logística', 7.84, '2019-08-01', '2019-08-27', '2023-12-21'),
('Universidad Intercontinental', 'CDMX', 'Ian Serrano Pacheco', 'Criminalística', 9.09, '2020-08-01', '2020-09-03', '2024-12-18'),
('Universidad del Pedregal', 'CDMX', 'Zoe Morales Castañeda', 'Terapia Física', 8.92, '2019-08-01', '2019-08-15', '2023-12-24'),
('Universidad Marista', 'Guadalajara', 'Enzo Delgado Herrera', 'Teología', 9.20, '2020-08-01', '2020-08-21', '2024-12-12'),
('Universidad del Valle de Atemajac', 'Jalisco', 'Aitana Rivera Mendoza', 'Publicidad', 6.81, '2019-08-01', '2019-09-07', '2023-12-20'),
('Universidad Autónoma de Guadalajara', 'Jalisco', 'Gabriel Peña Morales', 'Medicina Veterinaria', 9.26, '2020-08-01', '2020-08-23', '2024-12-14'),
('Universidad de Monterrey', 'Nuevo León', 'Emma Solís Jiménez', 'Ingeniería Ambiental', 9.00, '2019-08-01', '2019-08-29', '2023-12-15'),
('Universidad Regiomontana', 'Nuevo León', 'Liam Vargas Delgado', 'Ciencias de la Comunicación', 8.90, '2020-08-01', '2020-09-02', '2024-12-22'),
('Universidad de las Américas Puebla', 'Puebla', 'Mía Ortega Santos', 'Relaciones Públicas', 7.17, '2019-08-01', '2019-08-11', '2023-12-23'),
('Universidad Popular Autónoma del Estado de Puebla', 'Puebla', 'Noah Guerrero Luna', 'Ingeniería Mecatrónica', 8.95, '2020-08-01', '2020-08-27', '2024-12-16'),
('Universidad Nacional Autónoma de México', 'CDMX', 'Ana Morales Jiménez', 'Ingeniería en Computación', 8.95, '2021-08-01', '2021-08-20', '2025-12-15'),
('Universidad Nacional Autónoma de México', 'CDMX', 'Ricardo Vega Santana', 'Psicología', 9.12, '2020-08-01', '2020-08-18', '2024-12-10'),
('Universidad Nacional Autónoma de México', 'CDMX', 'Paola Herrera Díaz', 'Filosofía', 8.78, '2019-08-01', '2019-08-25', '2023-12-20'),
('Instituto Tecnológico de Monterrey', 'Nuevo León', 'Andrés Castillo Ramírez', 'Ingeniería Industrial', 9.23, '2021-08-01', '2021-09-05', '2025-12-18'),
('Instituto Tecnológico de Monterrey', 'Nuevo León', 'Carmen López Fernández', 'Negocios Internacionales', 8.86, '2020-08-01', '2020-08-22', '2024-12-12'),
('Instituto Tecnológico de Monterrey', 'Nuevo León', 'Pablo Ruiz García', 'Ingeniería en Software', 9.34, '2019-08-01', '2019-08-15', '2023-12-14'),
('Universidad de Guadalajara', 'Jalisco', 'Mónica Álvarez Torres', 'Enfermería', 8.91, '2021-08-01', '2021-08-28', '2025-12-20'),
('Universidad de Guadalajara', 'Jalisco', 'Jorge Mendoza Silva', 'Ingeniería Civil', 9.07, '2020-08-01', '2020-09-02', '2024-12-16'),
('Universidad de Guadalajara', 'Jalisco', 'Elena Vargas Moreno', 'Nutrición', 8.83, '2019-08-01', '2019-08-19', '2023-12-18'),
('Universidad de Guadalajara', 'Jalisco', 'Héctor Ramírez Cruz', 'Administración', 9.15, '2021-08-01', '2021-08-16', '2025-12-22'),
('Instituto Politécnico Nacional', 'CDMX', 'Alejandra Peña Gutiérrez', 'Ingeniería Biomédica', 8.97, '2020-08-01', '2020-08-24', '2024-12-14'),
('Instituto Politécnico Nacional', 'CDMX', 'Manuel Santos Ortega', 'Ingeniería en Sistemas', 9.19, '2021-08-01', '2021-09-01', '2025-12-19'),
('Universidad Autónoma de Nuevo León', 'Nuevo León', 'Cristina Flores Herrera', 'Medicina', 9.28, '2020-08-01', '2020-08-17', '2026-06-15'),
('Universidad Autónoma de Nuevo León', 'Nuevo León', 'Daniel Morales López', 'Ingeniería Mecánica', 8.92, '2021-08-01', '2021-08-21', '2025-12-17'),
('Universidad Veracruzana', 'Veracruz', 'Patricia García Ramos', 'Arquitectura', 8.85, '2020-08-01', '2020-08-26', '2024-12-21'),
('Universidad Autónoma de Yucatán', 'Yucatán', 'Alberto Jiménez Castillo', 'Ingeniería Química', 9.03, '2021-08-01', '2021-08-23', '2025-12-24'),
('Universidad de Sonora', 'Sonora', 'Raquel Hernández Vega', 'Biología', 8.88, '2020-08-01', '2020-09-03', '2024-12-23'),
('Universidad Autónoma de Sinaloa', 'Sinaloa', 'Fernando Silva Morales', 'Derecho', 9.11, '2021-08-01', '2021-08-18', '2025-12-13'),
('Universidad de Guanajuato', 'Guanajuato', 'Lorena Castro Delgado', 'Química', 8.94, '2020-08-01', '2020-08-29', '2024-12-11'),
('Universidad Autónoma de Chihuahua', 'Chihuahua', 'Gabriel Torres Sánchez', 'Comunicación', 9.06, '2021-08-01', '2021-09-04', '2025-12-26'),
('Universidad Michoacana de San Nicolás', 'Michoacán', 'Vanessa Ruiz Mendoza', 'Contaduría', 8.79, '2020-08-01', '2020-08-31', '2024-12-25'),
('Universidad Autónoma de Puebla', 'Puebla', 'Rodrigo Vázquez Herrera', 'Ingeniería Industrial', 9.17, '2021-08-01', '2021-08-19', '2025-12-15'),
('Universidad Autónoma de San Luis Potosí', 'San Luis Potosí', 'Isabel Guerrero Ramírez', 'Psicología', 8.90, '2020-08-01', '2020-09-06', '2024-12-12'),
('Universidad de Colima', 'Colima', 'Javier Moreno García', 'Veterinaria', 9.24, '2021-08-01', '2021-08-27', '2026-06-20'),
('Universidad Autónoma de Querétaro', 'Querétaro', 'Claudia López Torres', 'Ingeniería en Software', 8.96, '2020-08-01', '2020-08-20', '2024-12-18'),
('Universidad Nacional Autónoma de México', 'CDMX', 'Sergio Fernández Cruz', 'Economía', 9.21, '2021-08-01', '2021-08-24', '2025-12-21'),
('Universidad Nacional Autónoma de México', 'CDMX', 'Natalia Sandoval Pérez', 'Sociología', 8.87, '2020-08-01', '2020-08-16', '2024-12-19'),
('Instituto Tecnológico de Monterrey', 'Nuevo León', 'Miguel Ramos Jiménez', 'Ingeniería Mecatrónica', 9.29, '2021-08-01', '2021-09-07', '2025-12-23'),
('Universidad de Guadalajara', 'Jalisco', 'Ana Belén Cortés Vega', 'Diseño Gráfico', 8.93, '2020-08-01', '2020-08-27', '2024-12-24'),
('Universidad de Guadalajara', 'Jalisco', 'Carlos Alberto Méndez Silva', 'Ingeniería en Sistemas', 9.14, '2021-08-01', '2021-08-30', '2025-12-27'),
('Instituto Politécnico Nacional', 'CDMX', 'Mariana Aguilar Morales', 'Ingeniería Civil', 8.98, '2020-08-01', '2020-09-05', '2024-12-22'),
('Universidad Autónoma de Nuevo León', 'Nuevo León', 'Francisco Herrera López', 'Administración', 9.08, '2021-08-01', '2021-08-22', '2025-12-14'),
('Universidad Veracruzana', 'Veracruz', 'Lucía Ramírez Castillo', 'Comunicación', 8.84, '2020-08-01', '2020-08-25', '2024-12-26'),
('Universidad Autónoma de Yucatán', 'Yucatán', 'Eduardo Torres Hernández', 'Ingeniería Civil', 9.02, '2021-08-01', '2021-08-26', '2025-12-18'),
('Universidad de Sonora', 'Sonora', 'Rosa Elena Vega Morales', 'Nutrición', 8.89, '2020-08-01', '2020-09-01', '2024-12-20'),
('Universidad Autónoma de Sinaloa', 'Sinaloa', 'Antonio García Delgado', 'Ingeniería Química', 9.16, '2021-08-01', '2021-08-28', '2025-12-25'),
('Universidad de Guanajuato', 'Guanajuato', 'Beatriz Moreno Sánchez', 'Biología', 8.91, '2020-08-01', '2020-08-23', '2024-12-17'),
('Universidad Autónoma de Chihuahua', 'Chihuahua', 'Raúl Silva Fernández', 'Derecho', 9.05, '2021-08-01', '2021-09-02', '2025-12-19'),
('Universidad Michoacana de San Nicolás', 'Michoacán', 'Sofía Guerrero Jiménez', 'Psicología', 8.86, '2020-08-01', '2020-08-21', '2024-12-15'),
('Universidad Autónoma de Puebla', 'Puebla', 'Diego Herrera Ramos', 'Ingeniería Mecánica', 9.13, '2021-08-01', '2021-08-25', '2025-12-22'),
('Universidad Autónoma de San Luis Potosí', 'San Luis Potosí', 'Carmen Vázquez Torres', 'Arquitectura', 8.95, '2020-08-01', '2020-09-04', '2024-12-24'),
('Universidad de Colima', 'Colima', 'Alejandro Morales Cruz', 'Ingeniería Industrial', 9.20, '2021-08-01', '2021-08-29', '2025-12-16'),
('Universidad Autónoma de Querétaro', 'Querétaro', 'Valeria Sánchez López', 'Comunicación', 8.92, '2020-08-01', '2020-08-19', '2024-12-21'),
('Universidad Nacional Autónoma de México', 'CDMX', 'Óscar Ramírez García', 'Ingeniería Eléctrica', 9.18, '2021-08-01', '2021-08-31', '2025-12-28'),
('Instituto Tecnológico de Monterrey', 'Nuevo León', 'Isabella Fernández Moreno', 'Mercadotecnia', 8.99, '2020-08-01', '2020-08-18', '2024-12-13'),
('Universidad de Guadalajara', 'Jalisco', 'Emilio García Vega', 'Medicina', 9.31, '2021-08-01', '2021-08-17', '2027-06-18'),
('Instituto Politécnico Nacional', 'CDMX', 'Adriana López Herrera', 'Ingeniería Química', 8.97, '2020-08-01', '2020-09-08', '2024-12-27'),
('Universidad Autónoma de Nuevo León', 'Nuevo León', 'Sebastián Torres Silva', 'Ingeniería en Software', 9.25, '2021-08-01', '2021-08-20', '2025-12-29'),
('Universidad Veracruzana', 'Veracruz', 'Camila Morales Jiménez', 'Trabajo Social', 8.88, '2020-08-01', '2020-08-28', '2024-12-28'),
('Universidad de Guadalajara', 'Jalisco', 'Matías Hernández Cruz', 'Ingeniería Ambiental', 9.09, '2021-08-01', '2021-09-03', '2025-12-30'),
('Universidad Nacional Autónoma de México', 'CDMX', 'Luna García Ramírez', 'Ciencias Políticas', 8.94, '2020-08-01', '2020-08-24', '2024-12-30');



-- Insertar registros en la tabla alumnos basados en los nombres de info_titulados
INSERT INTO alumnos (id_titulado, nombre_completo, edad, telefono, email, direccion, genero) VALUES
(1, 'María González Pérez', 24, '555-0101', 'maria.gonzalez@email.com', 'Av. Universidad 123, CDMX', 'F'),
(2, 'Carlos Rodríguez López', 25, '555-0102', 'carlos.rodriguez@email.com', 'Calle Tecnológico 456, Monterrey, NL', 'M'),
(3, 'Ana Martínez Silva', 26, '555-0103', 'ana.martinez@email.com', 'Blvd. Médico 789, Guadalajara, Jal', 'F'),
(4, 'José Luis Hernández', 23, '555-0104', 'jose.hernandez@email.com', 'Av. Politécnico 321, CDMX', 'M'),
(5, 'Laura Sánchez Morales', 24, '555-0105', 'laura.sanchez@email.com', 'Calle Psicología 654, Monterrey, NL', 'F'),
(6, 'Miguel Ángel Torres', 25, '555-0106', 'miguel.torres@email.com', 'Av. Derecho 987, Veracruz, Ver', 'M'),
(7, 'Sofía Ramírez Castro', 26, '555-0107', 'sofia.ramirez@email.com', 'Calle Arquitectura 147, Mérida, Yuc', 'F'),
(8, 'Roberto Jiménez Vega', 24, '555-0108', 'roberto.jimenez@email.com', 'Blvd. Industrial 258, Hermosillo, Son', 'M'),
(9, 'Gabriela Flores Ruiz', 25, '555-0109', 'gabriela.flores@email.com', 'Av. Contaduría 369, Culiacán, Sin', 'F'),
(10, 'Fernando Castro Mendoza', 23, '555-0110', 'fernando.castro@email.com', 'Calle Ingeniería 741, Guanajuato, Gto', 'M'),
(11, 'Valeria Moreno Aguilar', 24, '555-0111', 'valeria.moreno@email.com', 'Av. Comunicación 852, Chihuahua, Chih', 'F'),
(12, 'Diego Vargas Herrera', 25, '555-0112', 'diego.vargas@email.com', 'Blvd. Química 963, Morelia, Mich', 'M'),
(13, 'Camila Ortega Delgado', 26, '555-0113', 'camila.ortega@email.com', 'Calle Biología 159, Puebla, Pue', 'F'),
(14, 'Alejandro Ramos Peña', 23, '555-0114', 'alejandro.ramos@email.com', 'Av. Fisioterapia 357, San Luis Potosí, SLP', 'M'),
(15, 'Isabella Cruz Navarro', 24, '555-0115', 'isabella.cruz@email.com', 'Calle Veterinaria 468, Colima, Col', 'F'),
(16, 'Sebastián Medina Rojas', 25, '555-0116', 'sebastian.medina@email.com', 'Blvd. Software 579, Querétaro, Qro', 'M'),
(17, 'Natalia Guerrero Ibarra', 26, '555-0117', 'natalia.guerrero@email.com', 'Av. Enfermería 681, Saltillo, Coah', 'F'),
(18, 'Mateo Espinoza Luna', 23, '555-0118', 'mateo.espinoza@email.com', 'Calle Agronomía 792, Villahermosa, Tab', 'M'),
(19, 'Valentina Castillo Soto', 24, '555-0119', 'valentina.castillo@email.com', 'Av. Odontología 183, Tampico, Tamps', 'F'),
(20, 'Santiago Morales Rivera', 25, '555-0120', 'santiago.morales@email.com', 'Blvd. Turismo 294, Tepic, Nay', 'M'),
(21, 'Emilia Herrera Campos', 26, '555-0121', 'emilia.herrera@email.com', 'Calle Negocios 315, Cancún, QRoo', 'F'),
(22, 'Nicolás Mendoza Reyes', 23, '555-0122', 'nicolas.mendoza@email.com', 'Av. Electrónica 426, Tijuana, BC', 'M'),
(23, 'Regina Vázquez García', 24, '555-0123', 'regina.vazquez@email.com', 'Calle Nutrición 537, Campeche, Camp', 'F'),
(24, 'Maximiliano Silva Córdoba', 25, '555-0124', 'maximiliano.silva@email.com', 'Blvd. Mercadotecnia 648, Los Mochis, Sin', 'M'),
(25, 'Luciana Peña Maldonado', 26, '555-0125', 'luciana.pena@email.com', 'Av. Trabajo Social 759, Toluca, Edo Mex', 'F'),
(26, 'Emiliano Acosta Villanueva', 23, '555-0126', 'emiliano.acosta@email.com', 'Calle Minería 861, Zacatecas, Zac', 'M'),
(27, 'Victoria Domínguez Salinas', 24, '555-0127', 'victoria.dominguez@email.com', 'Av. Educación 972, Tlaxcala, Tlax', 'F'),
(28, 'Patricio Romero Valdez', 25, '555-0128', 'patricio.romero@email.com', 'Blvd. Sistemas 183, Aguascalientes, Ags', 'M'),
(29, 'Antonella Figueroa Ortiz', 26, '555-0129', 'antonella.figueroa@email.com', 'Calle Química 294, Cuernavaca, Mor', 'F'),
(30, 'Leonardo Aguilar Montoya', 23, '555-0130', 'leonardo.aguilar@email.com', 'Av. Gastronomía 315, Pachuca, Hgo', 'M'),
(31, 'Renata Cabrera Escobar', 24, '555-0131', 'renata.cabrera@email.com', 'Calle Diseño 426, Durango, Dgo', 'F'),
(32, 'Joaquín Maldonado Herrera', 25, '555-0132', 'joaquin.maldonado@email.com', 'Blvd. Filosofía 537, Chilpancingo, Gro', 'M'),
(33, 'Mariana Sandoval Téllez', 26, '555-0133', 'mariana.sandoval@email.com', 'Av. Antropología 648, Oaxaca, Oax', 'F'),
(34, 'Tadeo Cervantes Muñoz', 23, '555-0134', 'tadeo.cervantes@email.com', 'Calle Forestal 759, Tuxtla Gutiérrez, Chis', 'M'),
(35, 'Ariadna Lara Jiménez', 24, '555-0135', 'ariadna.lara@email.com', 'Av. Relaciones 861, CDMX', 'F'),
(36, 'Gael Medrano Contreras', 25, '555-0136', 'gael.medrano@email.com', 'Blvd. Finanzas 972, CDMX', 'M'),
(37, 'Alexa Paredes Vega', 26, '555-0137', 'alexa.paredes@email.com', 'Calle Diseño Industrial 183, CDMX', 'F'),
(38, 'Benjamín Ruiz Moreno', 23, '555-0138', 'benjamin.ruiz@email.com', 'Av. Biomédica 294, CDMX', 'M'),
(39, 'Clara Ramírez Guerrero', 24, '555-0139', 'clara.ramirez@email.com', 'Calle Periodismo 315, CDMX', 'F'),
(40, 'Thiago Álvarez Ramos', 25, '555-0140', 'thiago.alvarez@email.com', 'Blvd. Literatura 426, CDMX', 'M'),
(41, 'Daniela Chávez Fernández', 26, '555-0141', 'daniela.chavez@email.com', 'Av. Logística 537, CDMX', 'F'),
(42, 'Ian Serrano Pacheco', 23, '555-0142', 'ian.serrano@email.com', 'Calle Criminalística 648, CDMX', 'M'),
(43, 'Zoe Morales Castañeda', 24, '555-0143', 'zoe.morales@email.com', 'Av. Terapia Física 759, CDMX', 'F'),
(44, 'Enzo Delgado Herrera', 25, '555-0144', 'enzo.delgado@email.com', 'Blvd. Teología 861, Guadalajara, Jal', 'M'),
(45, 'Aitana Rivera Mendoza', 26, '555-0145', 'aitana.rivera@email.com', 'Calle Publicidad 972, Guadalajara, Jal', 'F'),
(46, 'Gabriel Peña Morales', 23, '555-0146', 'gabriel.pena@email.com', 'Av. Veterinaria 183, Guadalajara, Jal', 'M'),
(47, 'Emma Solís Jiménez', 24, '555-0147', 'emma.solis@email.com', 'Calle Ambiental 294, Monterrey, NL', 'F'),
(48, 'Liam Vargas Delgado', 25, '555-0148', 'liam.vargas@email.com', 'Blvd. Comunicación 315, Monterrey, NL', 'M'),
(49, 'Mía Ortega Santos', 26, '555-0149', 'mia.ortega@email.com', 'Av. Relaciones Públicas 426, Puebla, Pue', 'F'),
(50, 'Noah Guerrero Luna', 23, '555-0150', 'noah.guerrero@email.com', 'Calle Mecatrónica 537, Puebla, Pue', 'M'),
(51, 'Andrea Morales Jiménez', 25, '555-0151', 'andrea.morales@email.com', 'Av. Computación 648, CDMX', 'F'),
(52, 'Ricardo Vega Santana', 26, '555-0152', 'ricardo.vega@email.com', 'Calle Psicología 759, CDMX', 'M'),
(53, 'Paola Herrera Díaz', 24, '555-0153', 'paola.herrera@email.com', 'Blvd. Filosofía 861, CDMX', 'F'),
(54, 'Andrés Castillo Ramírez', 23, '555-0154', 'andres.castillo@email.com', 'Av. Industrial 972, Monterrey, NL', 'M'),
(55, 'Carmen López Fernández', 25, '555-0155', 'carmen.lopez@email.com', 'Calle Negocios 183, Monterrey, NL', 'F'),
(56, 'Pablo Ruiz García', 26, '555-0156', 'pablo.ruiz@email.com', 'Blvd. Software 294, Monterrey, NL', 'M'),
(57, 'Mónica Álvarez Torres', 24, '555-0157', 'monica.alvarez@email.com', 'Av. Enfermería 315, Guadalajara, Jal', 'F'),
(58, 'Jorge Mendoza Silva', 23, '555-0158', 'jorge.mendoza@email.com', 'Calle Civil 426, Guadalajara, Jal', 'M'),
(59, 'Elena Vargas Moreno', 25, '555-0159', 'elena.vargas@email.com', 'Blvd. Nutrición 537, Guadalajara, Jal', 'F'),
(60, 'Héctor Ramírez Cruz', 26, '555-0160', 'hector.ramirez@email.com', 'Av. Administración 648, Guadalajara, Jal', 'M'),
(61, 'Alejandra Peña Gutiérrez', 24, '555-0161', 'alejandra.pena@email.com', 'Calle Biomédica 759, CDMX', 'F'),
(62, 'Manuel Santos Ortega', 23, '555-0162', 'manuel.santos@email.com', 'Blvd. Sistemas 861, CDMX', 'M'),
(63, 'Cristina Flores Herrera', 25, '555-0163', 'cristina.flores@email.com', 'Av. Medicina 972, Monterrey, NL', 'F'),
(64, 'Daniel Morales López', 26, '555-0164', 'daniel.morales@email.com', 'Calle Mecánica 183, Monterrey, NL', 'M'),
(65, 'Patricia García Ramos', 24, '555-0165', 'patricia.garcia@email.com', 'Blvd. Arquitectura 294, Veracruz, Ver', 'F'),
(66, 'Alberto Jiménez Castillo', 23, '555-0166', 'alberto.jimenez@email.com', 'Av. Química 315, Mérida, Yuc', 'M'),
(67, 'Raquel Hernández Vega', 25, '555-0167', 'raquel.hernandez@email.com', 'Calle Biología 426, Hermosillo, Son', 'F'),
(68, 'Fernando Silva Morales', 26, '555-0168', 'fernando.silva@email.com', 'Blvd. Derecho 537, Culiacán, Sin', 'M'),
(69, 'Lorena Castro Delgado', 24, '555-0169', 'lorena.castro@email.com', 'Av. Química 648, Guanajuato, Gto', 'F'),
(70, 'Gabriel Torres Sánchez', 23, '555-0170', 'gabriel.torres@email.com', 'Calle Comunicación 759, Chihuahua, Chih', 'M'),
(71, 'Vanessa Ruiz Mendoza', 25, '555-0171', 'vanessa.ruiz@email.com', 'Blvd. Contaduría 861, Morelia, Mich', 'F'),
(72, 'Rodrigo Vázquez Herrera', 26, '555-0172', 'rodrigo.vazquez@email.com', 'Av. Industrial 972, Puebla, Pue', 'M'),
(73, 'Isabel Guerrero Ramírez', 24, '555-0173', 'isabel.guerrero@email.com', 'Calle Psicología 183, San Luis Potosí, SLP', 'F'),
(74, 'Javier Moreno García', 23, '555-0174', 'javier.moreno@email.com', 'Blvd. Veterinaria 294, Colima, Col', 'M'),
(75, 'Claudia López Torres', 25, '555-0175', 'claudia.lopez@email.com', 'Av. Software 315, Querétaro, Qro', 'F'),
(76, 'Sergio Fernández Cruz', 26, '555-0176', 'sergio.fernandez@email.com', 'Calle Economía 426, CDMX', 'M'),
(77, 'Natalia Sandoval Pérez', 24, '555-0177', 'natalia.sandoval@email.com', 'Blvd. Sociología 537, CDMX', 'F'),
(78, 'Miguel Ramos Jiménez', 23, '555-0178', 'miguel.ramos@email.com', 'Av. Mecatrónica 648, Monterrey, NL', 'M'),
(79, 'Ana Belén Cortés Vega', 25, '555-0179', 'anabelen.cortes@email.com', 'Calle Diseño 759, Guadalajara, Jal', 'F'),
(80, 'Carlos Alberto Méndez Silva', 26, '555-0180', 'carlosalberto.mendez@email.com', 'Blvd. Sistemas 861, Guadalajara, Jal', 'M'),
(81, 'Mariana Aguilar Morales', 24, '555-0181', 'mariana.aguilar@email.com', 'Av. Civil 972, CDMX', 'F'),
(82, 'Francisco Herrera López', 23, '555-0182', 'francisco.herrera@email.com', 'Calle Administración 183, Monterrey, NL', 'M'),
(83, 'Lucía Ramírez Castillo', 25, '555-0183', 'lucia.ramirez@email.com', 'Blvd. Comunicación 294, Veracruz, Ver', 'F'),
(84, 'Eduardo Torres Hernández', 26, '555-0184', 'eduardo.torres@email.com', 'Av. Civil 315, Mérida, Yuc', 'M'),
(85, 'Rosa Elena Vega Morales', 24, '555-0185', 'rosaelena.vega@email.com', 'Calle Nutrición 426, Hermosillo, Son', 'F'),
(86, 'Antonio García Delgado', 23, '555-0186', 'antonio.garcia@email.com', 'Blvd. Química 537, Culiacán, Sin', 'M'),
(87, 'Beatriz Moreno Sánchez', 25, '555-0187', 'beatriz.moreno@email.com', 'Av. Biología 648, Guanajuato, Gto', 'F'),
(88, 'Raúl Silva Fernández', 26, '555-0188', 'raul.silva@email.com', 'Calle Derecho 759, Chihuahua, Chih', 'M'),
(89, 'Sofía Guerrero Jiménez', 24, '555-0189', 'sofia.guerrero@email.com', 'Blvd. Psicología 861, Morelia, Mich', 'F'),
(90, 'Diego Herrera Ramos', 23, '555-0190', 'diego.herrera@email.com', 'Av. Mecánica 972, Puebla, Pue', 'M'),
(91, 'Carmen Vázquez Torres', 25, '555-0191', 'carmen.vazquez@email.com', 'Calle Arquitectura 183, San Luis Potosí, SLP', 'F'),
(92, 'Alejandro Morales Cruz', 26, '555-0192', 'alejandro.morales@email.com', 'Blvd. Industrial 294, Colima, Col', 'M'),
(93, 'Valeria Sánchez López', 24, '555-0193', 'valeria.sanchez@email.com', 'Av. Comunicación 315, Querétaro, Qro', 'F'),
(94, 'Óscar Ramírez García', 23, '555-0194', 'oscar.ramirez@email.com', 'Calle Eléctrica 426, CDMX', 'M'),
(95, 'Isabella Fernández Moreno', 25, '555-0195', 'isabella.fernandez@email.com', 'Blvd. Mercadotecnia 537, Monterrey, NL', 'F'),
(96, 'Emilio García Vega', 26, '555-0196', 'emilio.garcia@email.com', 'Av. Medicina 648, Guadalajara, Jal', 'M'),
(97, 'Adriana López Herrera', 24, '555-0197', 'adriana.lopez@email.com', 'Calle Química 759, CDMX', 'F'),
(98, 'Sebastián Torres Silva', 23, '555-0198', 'sebastian.torres@email.com', 'Blvd. Software 861, Monterrey, NL', 'M'),
(99, 'Camila Morales Jiménez', 25, '555-0199', 'camila.morales@email.com', 'Av. Trabajo Social 972, Veracruz, Ver', 'F'),
(100, 'Matías Hernández Cruz', 26, '555-0200', 'matias.hernandez@email.com', 'Calle Ambiental 183, Guadalajara, Jal', 'M'),
(101, 'Luna García Ramírez', 24, '555-0201', 'luna.garcia@email.com', 'Blvd. Políticas 294, CDMX', 'F');


SELECT * FROM info_titulados;

-- Obtener todos los alumnos que se hayan titulado en el año 2020.

SELECT *
FROM info_titulados
WHERE fecha_finalizacion >= '2020-01-01' 
    AND fecha_finalizacion < '2021-01-01';

-- Contar el total de alumnos que se inscribieron en el año 2018.
SELECT 
    COUNT(*)
FROM info_titulados
WHERE fecha_inicio >= '2018-01-01' 
    AND fecha_inicio < '2019-01-01';

-- Contar la cantidad de alumnos que se titularon en la Universidad del Valle.

SELECT
    COUNT(*)
FROM info_titulados
WHERE nombre_universidad = 'Universidad del Valle';

-- Contar y agrupar la cantidad de alumnos por carrera.

SELECT 
    carrera,
    COUNT(*) AS total_alumnos
FROM info_titulados
GROUP BY carrera;

-- Obtener los 5 alumnos con el promedio más alto.
SELECT *
FROM info_titulados
ORDER BY promedio 
    DESC
LIMIT 5;


-- Obtener el alumno con el promedio más bajo.
SELECT *
FROM info_titulados
ORDER BY promedio 
    ASC
LIMIT 1;

-- Obtener el promedio general de cada universidad y ordenarlo de mayor a menor.

SELECT
    nombre_universidad,
    AVG(promedio) AS promedio_general
FROM info_titulados
GROUP BY nombre_universidad
ORDER BY promedio_general DESC;


-- Obtener el nombre completo de cada alumno, la universidad donde curso, su edad y genero.

SELECT
    a.nombre_completo,
    i.nombre_universidad,
    a.edad,
    a.genero
FROM alumnos a 
JOIN info_titulados i ON a.id_titulado = i.id_titulado;

-- Obtener la cantidad de hombres 'M' y la cantidad de mujeres 'F' por universidad.

SELECT
    i.nombre_universidad,
    a.genero,
    COUNT(*) AS total_por_genero
FROM alumnos a
JOIN info_titulados i ON a.id_titulado = i.id_titulado
GROUP BY i.nombre_universidad, a.genero
ORDER BY total_por_genero DESC;

-- Obtener el promedio de edad de los alumnos en cada universidad.

SELECT
    i.nombre_universidad,
    AVG(a.edad) AS promedio_edad
FROM alumnos a
JOIN info_titulados i ON a.id_titulado = i.id_titulado
GROUP BY i.nombre_universidad
ORDER BY promedio_edad DESC;

-- Obtener la cantidad de alumnos que obtuvieron un promedio mayor a 8.5 y agruparlos por carrera.

SELECT
    carrera,
    COUNT(*) AS promedio_mayor_85
FROM info_titulados
WHERE promedio > 8.5
GROUP BY carrera
ORDER BY promedio_mayor_85 DESC;

-- Obtener los alumnos con promedio mayor a 9, su nombre completo, universidad edad y genero.

SELECT
    a.nombre_completo,
    i.nombre_universidad,
    a.edad,
    a.genero,
    i.promedio
FROM alumnos a
JOIN info_titulados i ON a.id_titulado = i.id_titulado
WHERE i.promedio > 9
ORDER BY i.promedio DESC
LIMIT 10;