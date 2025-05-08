-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 08, 2025 at 10:52 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dbstm`
--

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `Roll_No` int(50) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Email` varchar(100) NOT NULL,
  `Gender` varchar(100) NOT NULL,
  `Contact` varchar(100) NOT NULL,
  `DOB` varchar(100) NOT NULL,
  `Grade` varchar(100) NOT NULL,
  `Address` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`Roll_No`, `Name`, `Email`, `Gender`, `Contact`, `DOB`, `Grade`, `Address`) VALUES
(0, 'Anil', 'a@gmail.com', 'Male', '781096010', '20-09--2002', 'Grade 7', 'Welimada\n\n\n\n'),
(1, 'Sanjula', 'snj@gmail.com', 'Female', '785674923', '25-08-2000', 'Grade 9', 'Matara\n\n\n'),
(2, 'Asanka', 'asn@gmail.com', 'Male', '754689823', '27-07-2000', 'Grade 9', 'Welimada\n\n\n'),
(3, 'Malshani', 'msh@gmail.com', 'Female', '762561290', '21-05-2000', 'Grade 9', 'Galle\n\n\n\n\n'),
(4, 'Joe', 'je@gmail.com', 'Male', '759016528', '12-05-2001', 'Grade 8', 'Kandy\n\n\n'),
(5, 'Yasas', 'Y@gmail.com', 'Male', '719342673', '30-08-2001', 'Grade 8', 'Hambantota\n\n\n\n'),
(6, 'Sajan', 'sja@gmail.com', 'Male', '762109827', '19-02-2003', 'Grade 6', 'Grade 7\n'),
(7, 'Dilini', 'dl@gmail.com', 'Female', '706719026', '04-11-2002', 'Grade 7', 'Jaffna\n\n\n'),
(8, 'Fahid', 'f@gmail.com', 'Male', '712018090', '29-09-2003', 'Grade 6', 'Matara\n\n\n\n'),
(9, 'Nikini', 'nk@gmail.com', 'Female', '712905618', '19-12-2002', 'Grade 7', 'Kandy\n\n\n'),
(10, 'Anne', 'an@gmail.com', 'Female', '785413490', '11-09-2003', 'Grade 6', 'Colombo\n\n\n\n'),
(11, 'Kasun', 'kn@gmail.com', 'Male', '711905024', '12-05-2003', 'Grade 6', 'Kandy\n\n\n\n\n\n'),
(12, 'Roshan', 'rsh@gmail.com', 'Male', '754901834', '21-10-2000', 'Grade 9', 'Jaffna\n\n\n'),
(13, 'Malin', 'ml@gmail.com', 'Male', '701825028', '12-05-2002', 'Grade 7', 'Matara\n\n\n\n\n'),
(14, 'Jane', 'jn@gmail.com', 'Female', '719216723', '23-08-2001', 'Grade 8', 'Welimada\n\n\n'),
(15, 'Piyal', 'pl@gmail.com', 'Male', '701984528', '31-03-2002', 'Grade 7', 'Hambantota\n\n\n\n'),
(16, 'Kamani', 'k@gmail.com', 'Female', '781462391', '17-09-2001', 'Grade 8', 'Colombo\n\n\n'),
(17, 'Priya', 'pr@gmail.com', 'Female', '728105629', '12-07-2003', 'Grade 6', 'Kandy\n\n\n\n'),
(18, 'Atul', 'atl@gmail.com', 'Male', '717813450', '21-12-2001', 'Grade 8', 'Trincomalee\n\n\n\n'),
(19, 'Sriya', 'sy@gmail.com', 'Female', '727193151', '11-06-2000', 'Grade 9', 'Welimada\n\n\n\n\n\n'),
(20, 'Kavita', 'kv@gmail.com', 'Female', '741094270', '17-09-2003', 'Grade 6', 'Galle\n\n\n\n\n'),
(21, 'Kamal', 'kl@gmail.com', 'Male', '713100921', '27-10-2002', 'Grade 7', 'Jaffna\n\n\n\n\n\n'),
(22, 'Sakuni', 'skn@gmail.com', 'Female', '761523490', '23-09-2002', 'Grade 7', 'Matara\n\n\n\n'),
(23, 'Mali', 'ml@gmail.com', 'Female', '701392012', '12-08-2000', 'Grade 9', 'Welimada\n');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`Roll_No`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
