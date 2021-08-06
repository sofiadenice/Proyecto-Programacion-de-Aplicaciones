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
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cita`
--

LOCK TABLES `cita` WRITE;
/*!40000 ALTER TABLE `cita` DISABLE KEYS */;
INSERT INTO `cita` VALUES (1,'gil','Gil','López','gil@gil.com','12345678','Limpieza tipo 234567','2021-08-11','14:36:00'),(2,'gil','Gil','López','gil@gil.com','12345678','dolor de diente','2021-08-19','12:21:00'),(3,'bal','hola','sdfghjk','xfcgvhj','cvbnm','cfgvhjkl;','2021-08-12','09:00:00'),(4,'guille','hola','sdfghjk','xfcgvhj','cvbnm','w2qwqweqwq','2021-08-14','09:00:00'),(5,'guille','hola','sdfghjk','xfcgvhj','cvbnm','w2qwqweqwq','2021-08-14','09:00:00'),(6,'guille','ortodoncia','garcia','guille@guille.com','77772121','dolor','2021-08-19','11:00:00'),(7,'guille','ortodoncia','gomez','guill1e@guille.1com','22290899','no se la verdad','2021-08-13','14:00:00'),(8,'guille','ortodoncia','tolodo','guill1e@guille.1com','22290899','no se la verdad','2021-08-18','14:00:00'),(9,'guille','ortodoncia','tolodo','guill1e@guille.1com','22290899','no se la verdad','2021-08-18','14:00:00'),(10,'guille','ortodoncia','tolodo','guill1e@guille.1com','22290899','no se la verdad','2021-08-18','14:00:00'),(11,'guille','ortodoncia','tolodo','guill1e@guille.1com','22290899','no se la verdad','2021-08-18','14:00:00'),(12,'guille','ortodoncia','tolodo','guill1e@guille.1com','22290899','no se la verdad','2021-08-18','14:00:00'),(13,'guille','hola','sdfghjk','guill1e@guille.1com','klnj','b nm','2021-08-13','09:00:00'),(14,'guille','2wqe2q','tolodooooooo','vbhnm,','vgbhnm,','gvhbjnkm','2021-08-12','14:00:00');
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
  `imagen` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tratamiento`
--

LOCK TABLES `tratamiento` WRITE;
/*!40000 ALTER TABLE `tratamiento` DISABLE KEYS */;
INSERT INTO `tratamiento` VALUES (1,'hola','hola','hola'),(4,'ortodoncia','foto de ortodoncia','https://q5g4e3i5.rocketcdn.me/app/uploads/7-fases-ortodoncia-640x300.jpg'),(6,'relleno','relleno de una muela 4-5','https://tudentista.mx/wp-content/uploads/2016/09/dra-verdugo-rellenos-dentales.jpg');
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
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'bal','bal@bal.com','$2b$14$59g5vuXMdhEp96eUf4QrgObVy1x1Tkx3C1H7zwofQ74qqhANtf3cK','$2b$14$59g5vuXMdhEp96eUf4QrgO','admin'),(3,'guille','guillermo-nieves@hotmail.com','$2b$14$qSG9e2AkrZlTZtLWfApXgesqBzuspz0IpdHUg5xVtAxPuynLlmzba','$2b$14$qSG9e2AkrZlTZtLWfApXge','cliente'),(4,'bal1','121@hot.com','$2b$14$qPPeFGBcnTNOmd7Q3b76lO9VHYWF8YLmC6gYhB.voBbJTxxVEGLIm','$2b$14$qPPeFGBcnTNOmd7Q3b76lO','admin'),(5,'guille1','guille@guille1.com','$2b$14$yfWenVaqtlx7.WhGo02jAuy/8zANnbMwoJgvwL0Y81qQBhbZxRBUK','$2b$14$yfWenVaqtlx7.WhGo02jAu','admin'),(7,'sofi','sofi@sofi.com','$2b$14$t0leYI7oUT8120FirfkbqONBjyO/RuTS5f4N7RRNU4iV9qNLnxk26','$2b$14$t0leYI7oUT8120FirfkbqO','admin');
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

-- Dump completed on 2021-08-06 15:03:18
