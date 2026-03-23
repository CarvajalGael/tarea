-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.4.28-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.15.0.7171
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para gestion
CREATE DATABASE IF NOT EXISTS `gestion` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci */;
USE `gestion`;

-- Volcando estructura para tabla gestion.tareas
CREATE TABLE IF NOT EXISTS `tareas` (
  `id_tarea` int(11) NOT NULL AUTO_INCREMENT,
  `id_usuario` int(11) NOT NULL,
  `titulo` varchar(200) NOT NULL,
  `descripcion` text NOT NULL,
  `fecha_creacion` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `fecha_limite` date NOT NULL,
  `hora_limite` time NOT NULL,
  PRIMARY KEY (`id_tarea`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

-- Volcando datos para la tabla gestion.tareas: ~0 rows (aproximadamente)
DELETE FROM `tareas`;

-- Volcando estructura para tabla gestion.usuario
CREATE TABLE IF NOT EXISTS `usuario` (
  `id_usuario` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `contraseña` varchar(50) NOT NULL,
  `telefono` varchar(50) DEFAULT NULL,
  `fecha_registro` timestamp NULL DEFAULT NULL,
  `ultimo_acceso` timestamp NULL DEFAULT NULL,
  `activo` tinyint(4) DEFAULT NULL,
  `foto_perfil` varchar(225) DEFAULT NULL,
  PRIMARY KEY (`id_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

-- Volcando datos para la tabla gestion.usuario: ~0 rows (aproximadamente)
DELETE FROM `usuario`;

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
