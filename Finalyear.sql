-- phpMyAdmin SQL Dump
-- version 4.6.6deb5ubuntu0.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jan 02, 2021 at 11:08 AM
-- Server version: 5.7.32-0ubuntu0.18.04.1
-- PHP Version: 7.2.24-0ubuntu0.18.04.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Finalyear`
--

-- --------------------------------------------------------

--
-- Table structure for table `RoadDetails`
--

CREATE TABLE `RoadDetails` (
  `ID` int(10) NOT NULL,
  `Area` varchar(20) NOT NULL,
  `Paved` varchar(20) NOT NULL,
  `Traffic` varchar(20) NOT NULL,
  `Traffic_Flow` varchar(20) NOT NULL,
  `Pothole` varchar(30) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `RoadDetails`
--

INSERT INTO `RoadDetails` (`ID`, `Area`, `Paved`, `Traffic`, `Traffic_Flow`, `Pothole`, `created_at`) VALUES
(1, 'Mawanda Road', 'Gravel', 'High', 'two-way', 'Potholes Detected', '2021-01-02 11:32:18');

-- --------------------------------------------------------

--
-- Table structure for table `Users`
--

CREATE TABLE `Users` (
  `ID` int(10) NOT NULL,
  `Firstname` varchar(30) NOT NULL,
  `Lastname` varchar(30) NOT NULL,
  `Username` varchar(30) NOT NULL,
  `Email` varchar(30) NOT NULL,
  `Password` varchar(30) NOT NULL,
  `Role` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Users`
--

INSERT INTO `Users` (`ID`, `Firstname`, `Lastname`, `Username`, `Email`, `Password`, `Role`) VALUES
(1, 'timothy', 'masiko', 'timo', 'masikotimo@gmail.com', 'timo', 1),
(2, 'timothy', 'masiko', 'timo', 'masikotimo@gmail.com', 'timo', 1),
(3, 'kisiga', 'tim', 'tkisiga', 'mickeygerman1@gmail.com', '4ee1__hb5r8795kx', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `RoadDetails`
--
ALTER TABLE `RoadDetails`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `Users`
--
ALTER TABLE `Users`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `RoadDetails`
--
ALTER TABLE `RoadDetails`
  MODIFY `ID` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `Users`
--
ALTER TABLE `Users`
  MODIFY `ID` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
