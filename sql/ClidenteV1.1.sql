CREATE DATABASE  IF NOT EXISTS `clidente` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `clidente`;
-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: localhost    Database: clidente
-- ------------------------------------------------------
-- Server version	8.0.20

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cita`
--

DROP TABLE IF EXISTS `cita`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cita` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user` varchar(45) DEFAULT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `apellido` varchar(45) DEFAULT NULL,
  `correo` varchar(45) DEFAULT NULL,
  `telefono` varchar(45) DEFAULT NULL,
  `motivo` varchar(500) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `hora` time DEFAULT NULL,
  `estado` varchar(45) DEFAULT 'Agendada',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cita`
--

LOCK TABLES `cita` WRITE;
/*!40000 ALTER TABLE `cita` DISABLE KEYS */;
INSERT INTO `cita` VALUES (16,'tat','Tatiana','Barahona','tat@gmail.com','75510220','Extracción de cordales','2021-08-12','10:00:00','Finalizada'),(17,'gil','Gil','López','gil@gmail.com','78872121','Dolor de muelas','2021-08-12','13:00:00','Agendada'),(18,'erick','Erick','Olmedo','erick@gmail.com','74829889','Blanqueamiento dental','2021-08-16','15:00:00','Agendada'),(19,'jesus','Jesús','Barahona','jesus@gmail.com','72238712','Inflamación de encías','2021-08-13','11:00:00','Agendada'),(20,'alexia','Alexia','Avelar','alexia@gmail.com','71128920','Revisión periódica','2021-08-17','13:00:00','Agendada'),(21,'sofia','Sofía','Gómez','sofia@gmail.com','72134323','Revisión de caries','2021-08-19','09:00:00','Agendada');
/*!40000 ALTER TABLE `cita` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tratamiento`
--

DROP TABLE IF EXISTS `tratamiento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tratamiento` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  `descripcion` varchar(500) DEFAULT NULL,
  `imagen` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tratamiento`
--

LOCK TABLES `tratamiento` WRITE;
/*!40000 ALTER TABLE `tratamiento` DISABLE KEYS */;
INSERT INTO `tratamiento` VALUES (8,'Prótesis dental','Una prótesis dental es un elemento artificial que sirve para restaurar la anatomía de uno o varios dientes.','https://lh3.googleusercontent.com/proxy/cYPm_M2wF9YIK4-zM_tu3Wi2ss0_UfDMk9geA6KExgzyI2pgFQQM55bqvFGKlaFMfQSrc3U0RWFpYi3fRGB_v4I4Avc6eWSCSzJ3o124yuj37RoMspvuEfG8RJAIsII9HzNfkUQ-9vcYeRzXv3HmQiIv-ohYpfTIC04n'),(9,'Implantes dentales','Es un componente de titanio en forma de tornillo que sustituye a la raíz de un diente natural.','https://belenperezdental.com/wp-content/uploads/2020/04/implante-dental.jpg'),(10,'Periodoncia','Tratamiento de las enfermedades de las encías y del hueso que sostiene los dientes.','https://clinicadentalnovadent.com/wp-content/uploads/2021/01/gingivitis-1.jpg'),(11,'Férula dental','Colocación de placa que se ajusta a todas las piezas dentales para amortiguar la mordida y descansar los músculos de la mandíbula. ','https://www.topdoctors.es/files/Image/large/b5591480dec2e100a884c42748da903f.jpg'),(12,'Carillas bucales de porcelana','Implantación de unas fundas estéticas compuestas por porcelana y elaboradas con resinas dentales que se colocan sobre los dientes simulando su apariencia.','https://i.pinimg.com/originals/12/c6/00/12c600cb9e8559d8b27ae93a8ab1871f.jpg'),(13,'Empaste dental','Consiste en eliminar la caries de una pieza dental para que esta enfermedad no avance y afecte al nervio del diente.','https://1.bp.blogspot.com/-RzpqahDXx-Q/XSXbkw9luMI/AAAAAAAB198/6szQYG2q0-4ZqauLBF1f_cswP8X-2848ACLcBGAs/s1600/empastes%2Bantibacterianos.jpg');
/*!40000 ALTER TABLE `tratamiento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_name` varchar(45) NOT NULL,
  `user_email` varchar(50) NOT NULL,
  `password` varchar(60) NOT NULL,
  `salt` varchar(30) NOT NULL,
  `role` varchar(10) DEFAULT 'cliente',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'bal','bal@gmail.com','$2b$14$59g5vuXMdhEp96eUf4QrgObVy1x1Tkx3C1H7zwofQ74qqhANtf3cK','$2b$14$59g5vuXMdhEp96eUf4QrgO','admin'),(4,'bal1','balbino@hotmail.com','$2b$14$qPPeFGBcnTNOmd7Q3b76lO9VHYWF8YLmC6gYhB.voBbJTxxVEGLIm','$2b$14$qPPeFGBcnTNOmd7Q3b76lO','admin'),(5,'guille1','guille@gmail.com','$2b$14$yfWenVaqtlx7.WhGo02jAuy/8zANnbMwoJgvwL0Y81qQBhbZxRBUK','$2b$14$yfWenVaqtlx7.WhGo02jAu','admin'),(7,'sofi','sofi@gmail.com','$2b$14$t0leYI7oUT8120FirfkbqONBjyO/RuTS5f4N7RRNU4iV9qNLnxk26','$2b$14$t0leYI7oUT8120FirfkbqO','admin'),(8,'tat','tat@gmail.com','$2b$14$CdYjvnPWexXf2npfShEDFOu33zjR8ijd7CDSfgUYI7qE/epv6aS2W','$2b$14$CdYjvnPWexXf2npfShEDFO','cliente'),(9,'gil','gil@gmail.com','$2b$14$LVHekDUOxzMFgRm7KCwPi.LQgeoJoouwU9pKJwvK7UmiFbhp1QpJm','$2b$14$LVHekDUOxzMFgRm7KCwPi.','cliente'),(11,'jesus','jesus@gmail.com','$2b$14$XpGTBOx8WC5CKn1OkOrvCO7RTOa2n3qSHDgO4VBHOZuuL9C5CwlNy','$2b$14$XpGTBOx8WC5CKn1OkOrvCO','cliente'),(12,'alexia','alexia@gmail.com','$2b$14$JTGk8K008PwlUCkvM4h89ORWAWhYBVYHUkpZ0JVvwR3ShJn7ipV4i','$2b$14$JTGk8K008PwlUCkvM4h89O','cliente'),(13,'sofia','sofia@gmail.com','$2b$14$5nrBqp8SlICr2wmYWhOz7e6BWyfhQYj2CZRRxdBabppmpUl8d2biC','$2b$14$5nrBqp8SlICr2wmYWhOz7e','cliente');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-08-10  1:56:29
