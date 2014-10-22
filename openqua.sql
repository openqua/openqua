SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

CREATE DATABASE IF NOT EXISTS `openqua` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `openqua`;

CREATE TABLE IF NOT EXISTS `station` (
  `callsign` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `operator` int(11) DEFAULT NULL,
  `keeper` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `lastupdate` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' ON UPDATE CURRENT_TIMESTAMP,
  `source` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE IF NOT EXISTS `station_repeater` (
  `callsign` varchar(10) CHARACTER SET latin1 NOT NULL,
  `ssid` varchar(3) CHARACTER SET latin1 NOT NULL,
  `mode` enum('FMVOICE','DSTAR','DMR','PACKET','ATV') CHARACTER SET latin1 NOT NULL,
  `tx` decimal(7,4) NOT NULL,
  `rx` decimal(7,4) NOT NULL,
  `carrier` tinyint(1) NOT NULL,
  `burst` tinyint(1) NOT NULL,
  `ctcss` decimal(4,1) DEFAULT NULL,
  `dcs` int(11) DEFAULT NULL,
  `town` varchar(255) CHARACTER SET latin1 NOT NULL,
  `locator` varchar(10) CHARACTER SET latin1 NOT NULL,
  `lat` decimal(15,10) NOT NULL,
  `lon` decimal(15,10) NOT NULL,
  `lastupdated` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' ON UPDATE CURRENT_TIMESTAMP,
  `source` varchar(255) CHARACTER SET latin1 NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;


ALTER TABLE `station`
 ADD PRIMARY KEY (`callsign`), ADD KEY `operator` (`operator`);

ALTER TABLE `station_repeater`
 ADD PRIMARY KEY (`callsign`,`ssid`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
