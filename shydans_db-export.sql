-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: db
-- Generation Time: Sep 29, 2023 at 06:57 AM
-- Server version: 11.1.2-MariaDB-1:11.1.2+maria~ubu2204
-- PHP Version: 8.2.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `shydans_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `accounting_alembic_version`
--

CREATE TABLE `accounting_alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `accounting_alembic_version`
--

INSERT INTO `accounting_alembic_version` (`version_num`) VALUES
('2e54d7602cc7');

-- --------------------------------------------------------

--
-- Table structure for table `accounting_charts`
--

CREATE TABLE `accounting_charts` (
  `id` int(11) NOT NULL,
  `frame_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `account_type` varchar(255) NOT NULL,
  `code` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `accounting_charts`
--

INSERT INTO `accounting_charts` (`id`, `frame_id`, `name`, `account_type`, `code`, `created_at`) VALUES
(1, 1, 'Cash On Hand', 'Asset', '1', '2023-09-22 04:05:01'),
(2, 1, 'Petty Cash Fund', 'Asset', '2', '2023-09-25 07:55:11'),
(3, 1, 'Cash in Bank-Security Bank-Shydans', 'Asset', '3', '2023-09-25 07:55:33'),
(4, 1, 'Cash in Bank-Security Bank-Baustark', 'Asset', '4', '2023-09-25 07:55:54'),
(5, 1, 'Cash in Bank-BDO-Shydans', 'Asset', '5', '2023-09-25 07:57:11'),
(6, 1, 'Cash in Bank-BDO-Baustark', 'Asset', '6', '2023-09-25 07:57:37'),
(7, 1, 'Gcash', 'Asset', '7', '2023-09-25 07:57:58'),
(8, 3, 'Raw Materials Inventory', 'Asset', '1', '2023-09-25 08:10:19'),
(9, 3, 'Work in Process Inventory', 'Asset', '2', '2023-09-25 08:10:27'),
(10, 3, 'Finished Goods Inventory', 'Asset', '3', '2023-09-25 08:10:34'),
(11, 3, 'Office Supplies Inventory', 'Asset', '4', '2023-09-25 08:10:40'),
(12, 3, 'Accountable Forms Inventory', 'Asset', '5', '2023-09-25 08:10:46'),
(13, 3, 'Food Inventory', 'Asset', '6', '2023-09-25 08:10:52'),
(14, 3, 'Drugs and Medicines Inventory', 'Asset', '7', '2023-09-25 08:10:59'),
(15, 3, 'Gasoline, Oil, and Lubricants', 'Asset', '8', '2023-09-25 08:11:06'),
(16, 3, 'Other Supplies', 'Asset', '9', '2023-09-25 08:11:13'),
(17, 4, 'Prepaid Rent', 'Asset', '1', '2023-09-25 08:11:23'),
(18, 4, 'Prepaid Insurance', 'Asset', '2', '2023-09-25 08:11:29'),
(19, 4, 'Advances To Contractors', 'Asset', '3', '2023-09-25 08:11:40'),
(20, 4, 'Other Prepaid Expenses', 'Asset', '4', '2023-09-25 08:11:45'),
(21, 5, 'Sinking Fund', 'Asset', '1', '2023-09-25 08:09:05'),
(22, 6, 'Land', 'Asset', '1', '2023-09-25 08:15:14'),
(23, 6, 'Land and Improvements', 'Asset', '2', '2023-09-25 08:15:14'),
(24, 6, 'Equipment', 'Asset', '3', '2023-09-25 08:15:14'),
(25, 6, 'Buildings', 'Asset', '4', '2023-09-25 08:15:14'),
(26, 6, 'Other Structure', 'Asset', '5', '2023-09-25 08:15:14'),
(27, 6, 'Leasehold Improvements, Land', 'Asset', '6', '2023-09-25 08:15:14'),
(28, 6, 'Accumulated Depreciation', 'Asset', '7', '2023-09-25 08:15:14'),
(29, 7, 'Machineries', 'Asset', '1', '2023-09-25 08:18:08'),
(30, 7, 'Accumulated Depreciation-Machineries', 'Asset', '2', '2023-09-25 08:18:08'),
(31, 7, 'Communication Equipment', 'Asset', '3', '2023-09-25 08:18:08'),
(32, 7, 'Accumulated Depreciation-Equipment', 'Asset', '4', '2023-09-25 08:18:08'),
(33, 7, 'Construction and Heavy Equipment', 'Asset', '5', '2023-09-25 08:18:08'),
(34, 7, 'Accumulated Depreciation-Construction and Heavy Equipment', 'Asset', '6', '2023-09-25 08:18:08'),
(35, 7, 'Firefighting Equipment and Accessories', 'Asset', '7', '2023-09-25 08:18:08'),
(36, 7, 'Accumulated Depreciation-Firefighting Equipment and Accessories', 'Asset', '8', '2023-09-25 08:18:08'),
(37, 8, 'Motor Vehicles', 'Asset', '1', '2023-09-25 08:20:06'),
(38, 8, 'Accumulated Depreciation-Motor Vehicles', 'Asset', '2', '2023-09-25 08:20:06'),
(39, 8, 'Watercrafts', 'Asset', '3', '2023-09-25 08:20:06'),
(40, 8, 'Accumulated Depreciation-Watercrafts', 'Asset', '4', '2023-09-25 08:20:06'),
(41, 8, 'Other Transportation Equipment', 'Asset', '5', '2023-09-25 08:20:06'),
(42, 8, 'Accumulated Depreciation-Other Transportation Equipment', 'Asset', '6', '2023-09-25 08:20:06'),
(43, 9, 'Other Property, Plant and Equipment', 'Asset', '1', '2023-09-25 08:23:30'),
(44, 9, 'Accumulated Depreciation-Other Property, Plant and Equipment', 'Asset', '2', '2023-09-25 08:23:30'),
(45, 10, 'Accounts Payable', 'Liabilities', '1', '2023-09-25 08:25:27'),
(46, 10, 'Notes Payable', 'Liabilities', '2', '2023-09-25 08:25:27'),
(47, 10, 'Interest Payable', 'Liabilities', '3', '2023-09-25 08:25:27'),
(48, 11, 'Mortgage', 'Liabilities', '1', '2023-09-25 08:27:17'),
(49, 11, 'Loans Payable', 'Liabilities', '2', '2023-09-25 08:27:17'),
(50, 11, 'Other Long Term Liabilities', 'Liabilities', '3', '2023-09-25 08:27:17'),
(51, 12, 'Capital Stocks', 'Equity', '1', '2023-09-25 08:29:01'),
(52, 12, 'Retained Earnings', 'Equity', '2', '2023-09-25 08:29:01'),
(53, 13, 'Sales', 'Operating Revenue', '1', '2023-09-25 08:31:08'),
(54, 13, 'Sales Return & Allowances', 'Operating Revenue', '2', '2023-09-25 08:31:08'),
(55, 13, 'Discount and Allowances', 'Operating Revenue', '3', '2023-09-25 08:31:08'),
(56, 14, 'Cost of Goods Sold', 'Expense', '1', '2023-09-25 08:32:00'),
(57, 15, 'Salaries & Wages', 'Expense', '1', '2023-09-25 08:32:28'),
(58, 16, '13th Month Pay Expense', 'Expense', '1', '2023-09-25 08:34:59'),
(59, 16, 'Clothing Allowance', 'Expense', '2', '2023-09-25 08:34:59'),
(60, 16, 'Transportation Allowance', 'Expense', '3', '2023-09-25 08:34:59'),
(61, 16, 'Overtime and Night Pay', 'Expense', '4', '2023-09-25 08:34:59'),
(62, 16, 'Service Charge', 'Expense', '5', '2023-09-25 08:34:59'),
(63, 17, 'SSS Contributions Expense', 'Expense', '1', '2023-09-25 08:36:32'),
(64, 17, 'Pag-Ibig Contributions Expense', 'Expense', '2', '2023-09-25 08:36:32'),
(65, 17, 'Philhealth Contributions Expense', 'Expense', '3', '2023-09-25 08:36:32'),
(66, 17, 'Insurance Expensey', 'Expense', '4', '2023-09-25 08:36:32'),
(67, 18, 'Travel Expenses', 'Expense', '1', '2023-09-25 08:37:30'),
(68, 19, 'Trainings & Seminars Expense', 'Expense', '1', '2023-09-25 08:38:03'),
(69, 20, 'Office Supplies Expense', 'Expense', '1', '2023-09-25 08:41:38'),
(70, 20, 'Accountable Form Expense', 'Expense', '2', '2023-09-25 08:41:38'),
(71, 20, 'Food Supplies Expense', 'Expense', '3', '2023-09-25 08:41:38'),
(72, 20, 'Drugs and Medicines Expense', 'Expense', '4', '2023-09-25 08:41:38'),
(73, 20, 'Gasoline, Oil and Lubricants', 'Expense', '5', '2023-09-25 08:41:38'),
(74, 20, 'Construction Materials', 'Expense', '6', '2023-09-25 08:41:38'),
(75, 20, 'Other Supplies Expense', 'Expense', '7', '2023-09-25 08:41:38'),
(76, 21, 'Water Expense', 'Expense', '1', '2023-09-25 08:42:35'),
(77, 21, 'Electricity Expense', 'Expense', '2', '2023-09-25 08:42:35'),
(78, 21, 'Cooking Gas Expense', 'Expense', '3', '2023-09-25 08:42:35'),
(79, 22, 'Internet Expense', 'Expense', '1', '2023-09-25 08:43:26'),
(80, 22, 'Telephone Expense-Mobile Load', 'Expense', '2', '2023-09-25 08:43:26'),
(81, 22, 'Advertising Expense', 'Expense', '3', '2023-09-25 08:43:26'),
(82, 23, 'Rental Expense', 'Expense', '1', '2023-09-25 08:43:58'),
(83, 24, 'Professional Fee', 'Expense', '1', '2023-09-25 08:44:25'),
(84, 24, 'Legal Fees', 'Expense', '2', '2023-09-25 08:44:49'),
(85, 25, 'Land Improvements', 'Expense', '1', '2023-09-25 08:47:43'),
(86, 25, 'Buildings Expense', 'Expense', '2', '2023-09-25 08:47:43'),
(87, 25, 'Office Equipments', 'Expense', '3', '2023-09-25 08:47:43'),
(88, 25, 'Furniture & Fixture', 'Expense', '4', '2023-09-25 08:47:43'),
(89, 25, 'Machineries', 'Expense', '5', '2023-09-25 08:47:43'),
(90, 25, 'Construction & Heavy Equipment', 'Expense', '6', '2023-09-25 08:47:43'),
(91, 25, 'Transportation Vehicles-Watercrafts', 'Expense', '7', '2023-09-25 08:47:43'),
(92, 25, 'Transportation Vehicles-Motor Vehicles', 'Expense', '8', '2023-09-25 08:47:43'),
(93, 25, 'Other Transportation Equipment', 'Expense', '9', '2023-09-25 08:47:43'),
(94, 25, 'Other Property Plant & Equipment', 'Expense', '10', '2023-09-25 08:47:43'),
(95, 26, 'Other Maintenance & Operating Expense', 'Expense', '1', '2023-09-25 08:48:05'),
(96, 28, 'Depreciation Expense\"', 'Expense', '1', '2023-09-25 08:48:26'),
(97, 29, 'Business Permit & Licenses', 'Expense', '1', '2023-09-25 08:48:45'),
(98, 29, 'Taxes Expense', 'Expense', '2', '2023-09-25 08:49:06'),
(99, 27, 'Bank Charges', 'Expense', '1', '2023-09-25 08:50:38'),
(100, 27, 'Interest Expense', 'Expense', '2', '2023-09-25 08:50:38'),
(101, 27, 'Documentary Stamps', 'Expense', '3', '2023-09-25 08:50:38'),
(102, 27, 'Other Financial Charges', 'Expense', '4', '2023-09-25 08:50:38'),
(103, 2, 'Accounts Receivable', 'Asset', '1', '2023-09-27 01:22:06'),
(104, 2, 'Other Receivables', 'Asset', '2', '2023-09-27 02:23:45');

-- --------------------------------------------------------

--
-- Table structure for table `accounting_company`
--

CREATE TABLE `accounting_company` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `code` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `accounting_company`
--

INSERT INTO `accounting_company` (`id`, `name`, `code`, `created_at`) VALUES
(1, 'Erfinder', '5', '2023-09-29 03:37:50'),
(2, 'Shydan\'s Resort', '3', '2023-09-29 03:38:20');

-- --------------------------------------------------------

--
-- Table structure for table `accounting_credit_balance`
--

CREATE TABLE `accounting_credit_balance` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `credit` float NOT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `accounting_debit_balance`
--

CREATE TABLE `accounting_debit_balance` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `debit` float NOT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `accounting_department`
--

CREATE TABLE `accounting_department` (
  `id` int(11) NOT NULL,
  `company_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `code` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `accounting_department`
--

INSERT INTO `accounting_department` (`id`, `company_id`, `name`, `code`, `created_at`) VALUES
(1, 1, 'Software Development', '1', '2023-09-29 03:38:52');

-- --------------------------------------------------------

--
-- Table structure for table `accounting_frame`
--

CREATE TABLE `accounting_frame` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `report_type` varchar(255) NOT NULL,
  `code` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `accounting_frame`
--

INSERT INTO `accounting_frame` (`id`, `name`, `report_type`, `code`, `created_at`) VALUES
(1, 'Cash & Banks', 'Balance Sheet', '10', '2023-09-25 07:40:16'),
(2, 'Receivables', 'Balance Sheet', '11', '2023-09-25 07:41:00'),
(3, 'Inventories', 'Balance Sheet', '12', '2023-09-25 07:54:18'),
(4, 'Prepayments', 'Balance Sheet', '13', '2023-09-25 07:54:18'),
(5, 'Investments', 'Balance Sheet', '14', '2023-09-25 07:54:18'),
(6, 'Property, Plant & Equipment', 'Balance Sheet', '15', '2023-09-25 07:54:18'),
(7, 'Machineries and Equipment', 'Balance Sheet', '16', '2023-09-25 07:54:18'),
(8, 'Transportation Equipment', 'Balance Sheet', '17', '2023-09-25 07:54:18'),
(9, 'Other Property, Plant and Equipment', 'Balance Sheet', '18', '2023-09-25 07:54:18'),
(10, 'Payable Accounts', 'Balance Sheet', '20', '2023-09-25 07:54:18'),
(11, 'Long Term Liabilities', 'Balance Sheet', '24', '2023-09-25 07:54:18'),
(12, 'Equity', 'Balance Sheet', '28', '2023-09-25 07:54:18'),
(13, 'Revenue', 'Income Statement', '30', '2023-09-25 07:54:18'),
(14, 'Costs of Sales', 'Income Statement', '40', '2023-09-25 07:54:18'),
(15, 'Personnel Services', 'Income Statement', '50', '2023-09-25 07:54:18'),
(16, 'Other Compensation', 'Income Statement', '51', '2023-09-25 07:54:18'),
(17, 'Personnel Benefits Contributions', 'Income Statement', '52', '2023-09-25 07:54:18'),
(18, 'Travel Expense', 'Income Statement', '60', '2023-09-25 07:54:18'),
(19, 'Trainings & Seminars Expense', 'Income Statement', '61', '2023-09-25 07:54:18'),
(20, 'Supplies and Materials Expense', 'Income Statement', '62', '2023-09-25 07:54:18'),
(21, 'Utility Expense', 'Income Statement', '63', '2023-09-25 07:54:18'),
(22, 'Communication Expense', 'Income Statement', '64', '2023-09-25 07:54:18'),
(23, 'Rent Expense', 'Income Statement', '65', '2023-09-25 07:54:18'),
(24, 'Professional Services Expense', 'Income Statement', '66', '2023-09-25 07:54:18'),
(25, 'Repairs & Maintenance Expense', 'Income Statement', '67', '2023-09-25 07:54:18'),
(26, 'Other Maintenance & Operating Expense', 'Income Statement', '68', '2023-09-25 07:54:18'),
(27, 'Financial Expense', 'Income Statement', '69', '2023-09-25 07:54:18'),
(28, 'Depreciation Expense', 'Income Statement', '70', '2023-09-25 07:54:18'),
(29, 'Permits, Licenses & Taxes Expense', 'Income Statement', '89', '2023-09-25 07:54:18'),
(32, 'TEST[FRAME]', 'Balance Sheet', '69', '2023-09-28 09:15:09');

-- --------------------------------------------------------

--
-- Table structure for table `accounting_journal`
--

CREATE TABLE `accounting_journal` (
  `id` int(11) NOT NULL,
  `supplier_id` int(11) DEFAULT NULL,
  `company_id` int(11) DEFAULT NULL,
  `department_id` int(11) DEFAULT NULL,
  `reference_no` varchar(255) DEFAULT NULL,
  `date` datetime NOT NULL,
  `notes` varchar(255) DEFAULT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `is_supplier` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `accounting_journal`
--

INSERT INTO `accounting_journal` (`id`, `supplier_id`, `company_id`, `department_id`, `reference_no`, `date`, `notes`, `created_at`, `is_supplier`) VALUES
(1, 1, 1, 1, '000001', '2023-09-29 03:39:48', 'Test ni Nikko', '2023-09-29 03:40:27', 0);

-- --------------------------------------------------------

--
-- Table structure for table `accounting_supplier`
--

CREATE TABLE `accounting_supplier` (
  `id` int(11) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `business_type` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `contact_number` varchar(255) DEFAULT NULL,
  `tel_number` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `tin` varchar(255) DEFAULT NULL,
  `sec` varchar(255) DEFAULT NULL,
  `dti` varchar(255) DEFAULT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `accounting_supplier`
--

INSERT INTO `accounting_supplier` (`id`, `first_name`, `last_name`, `business_type`, `email`, `contact_number`, `tel_number`, `address`, `tin`, `sec`, `dti`, `created_at`) VALUES
(1, 'Nikko', 'Ranara', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2023-09-29 03:39:33');

-- --------------------------------------------------------

--
-- Table structure for table `accounting_transaction`
--

CREATE TABLE `accounting_transaction` (
  `id` int(11) NOT NULL,
  `journal_id` int(11) NOT NULL,
  `chart_id` int(11) NOT NULL,
  `amount` float DEFAULT NULL,
  `is_type` int(11) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `accounting_transaction`
--

INSERT INTO `accounting_transaction` (`id`, `journal_id`, `chart_id`, `amount`, `is_type`, `created_at`) VALUES
(1, 1, 53, 2000, 1, '2023-09-29 03:42:25');

-- --------------------------------------------------------

--
-- Table structure for table `dashboard_alembic_version`
--

CREATE TABLE `dashboard_alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `dashboard_alembic_version`
--

INSERT INTO `dashboard_alembic_version` (`version_num`) VALUES
('310d8733a7eb');

-- --------------------------------------------------------

--
-- Table structure for table `dashboard_apps`
--

CREATE TABLE `dashboard_apps` (
  `id` int(11) NOT NULL,
  `app_id` int(11) DEFAULT NULL,
  `platform_id` int(11) DEFAULT NULL,
  `app_architecture` int(11) DEFAULT NULL,
  `app_version` int(11) DEFAULT NULL,
  `app_name` varchar(255) DEFAULT NULL,
  `app_zip` varchar(255) DEFAULT NULL,
  `download_url` varchar(255) DEFAULT NULL,
  `compressed_size` varchar(255) DEFAULT NULL,
  `version_notes` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `dashboard_apps`
--

INSERT INTO `dashboard_apps` (`id`, `app_id`, `platform_id`, `app_architecture`, `app_version`, `app_name`, `app_zip`, `download_url`, `compressed_size`, `version_notes`) VALUES
(1, 0, 3, 2, 1820, 'ClimeoCRM', 'ClimeoCRM.zip', '/apps/dl/mac/ClimeoCRM1820.zip', NULL, NULL),
(2, 1, 3, 2, 2613, 'ClimeoInventory', 'ClimeoInventory.zip', '/apps/dl/mac/ClimeoInventory2613.zip', NULL, NULL),
(3, 2, 3, 2, 3385, 'ClimeoSales', 'ClimeoSales.zip', '/apps/dl/mac/ClimeoSales3385.zip', NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `dashboard_users`
--

CREATE TABLE `dashboard_users` (
  `id` int(11) NOT NULL,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `role` int(11) DEFAULT NULL,
  `fname` varchar(255) DEFAULT NULL,
  `lname` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `contact` varchar(255) DEFAULT NULL,
  `image` varchar(255) DEFAULT NULL,
  `apps` varchar(255) DEFAULT NULL,
  `country` int(11) DEFAULT NULL,
  `creation_date` date NOT NULL,
  `creation_update` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `is_superuser` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `dashboard_users`
--

INSERT INTO `dashboard_users` (`id`, `username`, `password`, `role`, `fname`, `lname`, `email`, `contact`, `image`, `apps`, `country`, `creation_date`, `creation_update`, `is_superuser`) VALUES
(32, 'erfinder', '213944FBEFF2AF2F260B6C35500B34575A1967F97C636E73A356F523816CF5B4', 0, 'Erfinder', 'Tester', 'hello@erfinderstore.com', 'N/A', '1617700447.4160442erfinderlogon.png', '111110', 4, '2020-09-19', '2023-08-23 08:49:25', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accounting_alembic_version`
--
ALTER TABLE `accounting_alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Indexes for table `accounting_charts`
--
ALTER TABLE `accounting_charts`
  ADD PRIMARY KEY (`id`),
  ADD KEY `frame_id` (`frame_id`);

--
-- Indexes for table `accounting_company`
--
ALTER TABLE `accounting_company`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `accounting_credit_balance`
--
ALTER TABLE `accounting_credit_balance`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `accounting_debit_balance`
--
ALTER TABLE `accounting_debit_balance`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `accounting_department`
--
ALTER TABLE `accounting_department`
  ADD PRIMARY KEY (`id`),
  ADD KEY `company_id` (`company_id`);

--
-- Indexes for table `accounting_frame`
--
ALTER TABLE `accounting_frame`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `accounting_journal`
--
ALTER TABLE `accounting_journal`
  ADD PRIMARY KEY (`id`),
  ADD KEY `supplier_id` (`supplier_id`),
  ADD KEY `company_id` (`company_id`),
  ADD KEY `department_id` (`department_id`);

--
-- Indexes for table `accounting_supplier`
--
ALTER TABLE `accounting_supplier`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `accounting_transaction`
--
ALTER TABLE `accounting_transaction`
  ADD PRIMARY KEY (`id`),
  ADD KEY `journal_id` (`journal_id`),
  ADD KEY `chart_id` (`chart_id`);

--
-- Indexes for table `dashboard_alembic_version`
--
ALTER TABLE `dashboard_alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Indexes for table `dashboard_apps`
--
ALTER TABLE `dashboard_apps`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `dashboard_users`
--
ALTER TABLE `dashboard_users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `accounting_charts`
--
ALTER TABLE `accounting_charts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=106;

--
-- AUTO_INCREMENT for table `accounting_company`
--
ALTER TABLE `accounting_company`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `accounting_credit_balance`
--
ALTER TABLE `accounting_credit_balance`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `accounting_debit_balance`
--
ALTER TABLE `accounting_debit_balance`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `accounting_department`
--
ALTER TABLE `accounting_department`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `accounting_frame`
--
ALTER TABLE `accounting_frame`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT for table `accounting_journal`
--
ALTER TABLE `accounting_journal`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `accounting_supplier`
--
ALTER TABLE `accounting_supplier`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `accounting_transaction`
--
ALTER TABLE `accounting_transaction`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `dashboard_apps`
--
ALTER TABLE `dashboard_apps`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `dashboard_users`
--
ALTER TABLE `dashboard_users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `accounting_charts`
--
ALTER TABLE `accounting_charts`
  ADD CONSTRAINT `accounting_charts_ibfk_1` FOREIGN KEY (`frame_id`) REFERENCES `accounting_frame` (`id`);

--
-- Constraints for table `accounting_department`
--
ALTER TABLE `accounting_department`
  ADD CONSTRAINT `accounting_department_ibfk_1` FOREIGN KEY (`company_id`) REFERENCES `accounting_company` (`id`);

--
-- Constraints for table `accounting_journal`
--
ALTER TABLE `accounting_journal`
  ADD CONSTRAINT `accounting_journal_ibfk_1` FOREIGN KEY (`supplier_id`) REFERENCES `accounting_supplier` (`id`),
  ADD CONSTRAINT `accounting_journal_ibfk_2` FOREIGN KEY (`company_id`) REFERENCES `accounting_company` (`id`),
  ADD CONSTRAINT `accounting_journal_ibfk_3` FOREIGN KEY (`department_id`) REFERENCES `accounting_department` (`id`);

--
-- Constraints for table `accounting_transaction`
--
ALTER TABLE `accounting_transaction`
  ADD CONSTRAINT `accounting_transaction_ibfk_1` FOREIGN KEY (`journal_id`) REFERENCES `accounting_journal` (`id`),
  ADD CONSTRAINT `accounting_transaction_ibfk_2` FOREIGN KEY (`chart_id`) REFERENCES `accounting_charts` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
