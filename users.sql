-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 03-04-2023 a las 01:30:56
-- Versión del servidor: 10.4.27-MariaDB
-- Versión de PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `users`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `data_users`
--

CREATE TABLE `data_users` (
  `id` int(11) NOT NULL,
  `first_surname` varchar(20) DEFAULT NULL,
  `first_name` varchar(20) DEFAULT NULL,
  `other_name` varchar(50) DEFAULT NULL,
  `country` varchar(20) DEFAULT NULL,
  `email` varchar(300) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `data_users`
--

INSERT INTO `data_users` (`id`, `first_surname`, `first_name`, `other_name`, `country`, `email`) VALUES
(51, 'PEREZ', 'JUAN', 'CARLOS', 'Colombia', 'juan.perez@cidenet.com.co'),
(74, 'PEREZ', 'JUAN', 'DAVID', 'Colombia', 'juan.perez.2@cidenet.com.co'),
(75, 'PEREZ', 'JUAN', 'ANDRES', 'Colombia', 'juan.perez.3@cidenet.com.co'),
(79, 'DE LA CALLE', 'JUAN', 'GUILLERMO', 'Colombia', 'juan.delacalle@cidenet.com.co'),
(81, 'DE LA CALLE', 'JUAN', 'JOSE', 'Colombia', 'juan.delacalle.2@cidenet.com.co'),
(82, 'PEREZ', 'JUAN', 'CARLOS', 'Estados Unidos', 'juan.perez@cidenet.com.us'),
(83, 'PEREZ', 'JUAN', 'DAVID', 'Estados Unidos', 'juan.perez.2@cidenet.com.us'),
(84, 'PEREZ', 'JUAN', 'ANDRES', 'Estados Unidos', 'juan.perez.3@cidenet.com.us'),
(85, 'DE LA CALLE', 'JUAN', 'GUILLERMO', 'Estados Unidos', 'juan.delacalle@cidenet.com.us'),
(86, 'DE LA CALLE', 'JUAN', 'JOSE', 'Estados Unidos', 'juan.delacalle.2@cidenet.com.us'),
(112, 'PAGINACION', 'TEST', '', 'Colombia', 'test.paginacion@cidenet.com.co'),
(113, 'PAGINACION', 'TEST', 'SEGUNDO', 'Colombia', 'test.paginacion.2@cidenet.com.co'),
(117, 'LAST', 'TEST', 'NO OTHER NAME', 'Colombia', 'test.last@cidenet.com.co'),
(118, 'PEREZ', 'JUAN', 'CARLOS', 'Colombia', 'juan.perez.4@cidenet.com.co'),
(119, 'PEREZ', 'JUAN', 'DAVID', 'Colombia', 'juan.perez.5@cidenet.com.co'),
(120, 'PEREZ', 'JUAN', 'ANDRES', 'Colombia', 'juan.perez.6@cidenet.com.co'),
(121, 'DE LA CALLE', 'JUAN', 'GUILLERMO', 'Colombia', 'juan.delacalle.3@cidenet.com.co'),
(122, 'DE LA CALLE', 'JUAN', 'JOSE', 'Colombia', 'juan.delacalle.4@cidenet.com.co');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `data_users`
--
ALTER TABLE `data_users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `data_users`
--
ALTER TABLE `data_users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=123;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
