/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table candidatos
# ------------------------------------------------------------

DROP TABLE IF EXISTS `candidatos`;

CREATE TABLE `candidatos` (
  `COD_CAND` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Id de candidato ',
  `COD_ELEC` int(11) DEFAULT NULL COMMENT 'Id de la elección',
  `COD_ZONA` int(11) DEFAULT NULL COMMENT 'Id de la zona  ',
  `CAN_ORDEN` int(11) DEFAULT NULL COMMENT 'Posición en el voto  ',
  `GLOSA_CAND` text COMMENT 'Nombre completo  ',
  `COD_PART` int(11) DEFAULT NULL COMMENT 'Id del partido  ',
  `COD_PACTO` int(11) DEFAULT NULL COMMENT 'Id del pacto  ',
  `COD_SUBP` int(11) DEFAULT NULL COMMENT 'Id del Sub pacto',
  `COD_IND` tinyint(1) DEFAULT NULL COMMENT 'S: Independiente N: No Independiente',
  `CAN_PAGINA` int(11) DEFAULT NULL COMMENT 'Número de página en el acta ',
  `GLOSA_NOMBRE` text COMMENT 'Nombre del Candidato',
  `GLOSA_APELLIDO` text COMMENT 'Apellido del Candidato',
  PRIMARY KEY (`COD_CAND`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



# Dump of table pactos
# ------------------------------------------------------------

DROP TABLE IF EXISTS `pactos`;

CREATE TABLE `pactos` (
  `COD_PACTO` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Id del Pacto ',
  `LETRA_PACTO` text COMMENT 'Id del Pacto (A, B, C, etc.)  ',
  `GLOSA_PACTO` text COMMENT 'Glosa del Pacto   ',
  PRIMARY KEY (`COD_PACTO`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



# Dump of table partidos
# ------------------------------------------------------------

DROP TABLE IF EXISTS `partidos`;

CREATE TABLE `partidos` (
  `COD_PART` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `GLOSA_PART` text,
  `SIGLA_PART` text,
  PRIMARY KEY (`COD_PART`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



# Dump of table subpactos
# ------------------------------------------------------------

DROP TABLE IF EXISTS `subpactos`;

CREATE TABLE `subpactos` (
  `COD_SUBP` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Id del Sub Pacto',
  `COD_PACTO` int(11) DEFAULT NULL COMMENT 'Id del Pacto ',
  `GLOSA_SUBP` text COMMENT 'Glosa del Sub Pacto',
  PRIMARY KEY (`COD_SUBP`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



# Dump of table votaciones
# ------------------------------------------------------------

DROP TABLE IF EXISTS `votaciones`;

CREATE TABLE `votaciones` (
  `COD_ELEC` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Id de la eleccion',
  `AMBITO` int(11) DEFAULT NULL COMMENT '1) Votación Pactos (2) Votación Sub Pactos (3) Votación Partidos (4) Votación Candidatos (5) Votos Nulos (7) Votos Válidamente Emitidos ',
  `COD_AMBITO` int(11) DEFAULT NULL COMMENT 'Pacto: Codigo_pacto Sub Pacto: Codigo_subpacto Partido: Codigo_partido Candidato: Codigo_candidato (los siguientes se identifican por ámbito) \\nVotos Nulos:1 Votos en Blanco:1 Votos Válidamente  Emitidos:1',
  `COD_ZONA` int(11) DEFAULT NULL COMMENT 'codigo zona',
  `PORCENTAJE_VOTOS` text COMMENT '?99,99? cuyos 2 últimos dígitos corresponden a los decimales truncado y no redondeado.  Porcentaje de Pacto, Sub Pacto, Partidos y Candidatos se calcula respecto al total de votos válidamente emitidos.  Porcentaje de Votos Nulos, en Blanco y Válidamente Emitidos se calcula al total de votos válidamente emitidos.',
  PRIMARY KEY (`COD_ELEC`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



# Dump of table zonas
# ------------------------------------------------------------

DROP TABLE IF EXISTS `zonas`;

CREATE TABLE `zonas` (
  `COD_ZONA` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Id de la zona ',
  `GLOSA_ZONA` text COMMENT 'Glosa de la zona',
  `TIPO_ZONA` text COMMENT 'G = Global P = País R = Región Q = Provincia S = Circunscripción Senatorial  D = Distrito V = Circunscripción Provincial  C = Comuna  E = Circunscripción Electoral I = Distribución N = Continente U = Consulados L = Local Votación ',
  `ORDEN_ZONA` int(11) DEFAULT NULL COMMENT 'Indica el orden dentro de las zonas con el mismo tipo_zona ',
  PRIMARY KEY (`COD_ZONA`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



# Dump of table zonaspadre
# ------------------------------------------------------------

DROP TABLE IF EXISTS `zonaspadre`;

CREATE TABLE `zonaspadre` (
  `COD_ZONA` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Id de la zona ',
  `TIPO_ZONA` text COMMENT 'P = País R = Región Q = Provincia S = Circunscripción Senatorial  D = Distrito V = Circunscripción Provincial  C = Comuna  E = Circunscripción Electoral I = Distribución N = Continente U = Consulados L = Local Votación',
  `COD_ZONA_PAD` int(11) DEFAULT NULL COMMENT 'Id de la zona padre',
  `TIPO_ZONA_PAD` int(11) DEFAULT NULL COMMENT 'G = Global P = País  R = Región  Q = Provincia  S = Circunscripción Senatorial D = Distrito V = Circunscripción Provincial  C = Comuna  E = Circunscripción Electoral  I = Distribución N = Continente U = Consulados',
  PRIMARY KEY (`COD_ZONA`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;




/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
