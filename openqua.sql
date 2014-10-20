SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;


CREATE TABLE IF NOT EXISTS `repeater` (
  `callsign` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `rx` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `tx` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `to` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `mo` varchar(60) COLLATE utf8_unicode_ci NOT NULL,
  `ml` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `lo` varchar(60) COLLATE utf8_unicode_ci NOT NULL,
  `ke` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `lat` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `lon` varchar(15) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
