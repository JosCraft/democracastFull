-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         8.0.30 - MySQL Community Server - GPL
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para democracast
CREATE DATABASE IF NOT EXISTS `democracast` /*!40100 DEFAULT CHARACTER SET armscii8 COLLATE armscii8_bin */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `democracast`;

-- Volcando estructura para tabla democracast.candidato
CREATE TABLE IF NOT EXISTS `candidato` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `numero_cartelera` int NOT NULL,
  `cantidad_votos` int NOT NULL,
  `eleccion_id` bigint NOT NULL,
  `persona_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `eleccion_id` (`eleccion_id`),
  KEY `persona_id` (`persona_id`),
  CONSTRAINT `candidato_ibfk_1` FOREIGN KEY (`eleccion_id`) REFERENCES `eleccion` (`id`),
  CONSTRAINT `candidato_ibfk_2` FOREIGN KEY (`persona_id`) REFERENCES `persona` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=armscii8 COLLATE=armscii8_bin;

-- Volcando datos para la tabla democracast.candidato: ~0 rows (aproximadamente)

-- Volcando estructura para tabla democracast.eleccion
CREATE TABLE IF NOT EXISTS `eleccion` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) COLLATE armscii8_bin NOT NULL,
  `fecha` date NOT NULL,
  `estado_id` bigint NOT NULL,
  `votospermitidos` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_eleccion_estado` (`estado_id`),
  CONSTRAINT `eleccion_ibfk_1` FOREIGN KEY (`estado_id`) REFERENCES `estado` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=armscii8 COLLATE=armscii8_bin;

-- Volcando datos para la tabla democracast.eleccion: ~0 rows (aproximadamente)

-- Volcando estructura para tabla democracast.estado
CREATE TABLE IF NOT EXISTS `estado` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) COLLATE armscii8_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=armscii8 COLLATE=armscii8_bin;

-- Volcando datos para la tabla democracast.estado: ~2 rows (aproximadamente)
INSERT INTO `estado` (`id`, `nombre`) VALUES
	(1, 'OFFLINE'),
	(2, 'ONLINE');

-- Volcando estructura para tabla democracast.persona
CREATE TABLE IF NOT EXISTS `persona` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) COLLATE armscii8_bin NOT NULL,
  `apellido` varchar(255) COLLATE armscii8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=armscii8 COLLATE=armscii8_bin;

-- Volcando datos para la tabla democracast.persona: ~0 rows (aproximadamente)

-- Volcando estructura para tabla democracast.rol
CREATE TABLE IF NOT EXISTS `rol` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) COLLATE armscii8_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=armscii8 COLLATE=armscii8_bin;

-- Volcando datos para la tabla democracast.rol: ~0 rows (aproximadamente)
INSERT INTO `rol` (`id`, `nombre`) VALUES
	(1, 'ADMIN'),
	(3, 'MACHINE'),
	(2, 'USER');

-- Volcando estructura para tabla democracast.usuario
CREATE TABLE IF NOT EXISTS `usuario` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `usuario` varchar(255) COLLATE armscii8_bin NOT NULL,
  `password` varchar(255) COLLATE armscii8_bin NOT NULL,
  `rol_id` bigint NOT NULL,
  `estado_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `estado_id` (`estado_id`),
  KEY `idx_usuario_rol` (`rol_id`),
  CONSTRAINT `usuario_ibfk_1` FOREIGN KEY (`rol_id`) REFERENCES `rol` (`id`),
  CONSTRAINT `usuario_ibfk_2` FOREIGN KEY (`estado_id`) REFERENCES `estado` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=armscii8 COLLATE=armscii8_bin;

-- Volcando datos para la tabla democracast.usuario: ~1 rows (aproximadamente)
INSERT INTO `usuario` (`id`, `usuario`, `password`, `rol_id`, `estado_id`) VALUES
	(1, 'administrador', '$2b$12$DPWC4buH6pLx7DVEj9Z3XOH/nYRa.d8ziet5pjX10ysymbM/.7pnO', 1, 1);

-- Volcando estructura para tabla democracast.voto
CREATE TABLE IF NOT EXISTS `voto` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `eleccion_id` bigint NOT NULL,
  `candidato_id` bigint NOT NULL,
  `numero_votos` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `eleccion_id` (`eleccion_id`),
  KEY `candidato_id` (`candidato_id`),
  CONSTRAINT `voto_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `usuario` (`id`),
  CONSTRAINT `voto_ibfk_2` FOREIGN KEY (`eleccion_id`) REFERENCES `eleccion` (`id`),
  CONSTRAINT `voto_ibfk_3` FOREIGN KEY (`candidato_id`) REFERENCES `candidato` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=armscii8 COLLATE=armscii8_bin;

-- Volcando datos para la tabla democracast.voto: ~0 rows (aproximadamente)

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
