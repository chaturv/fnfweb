/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

DELETE FROM `calc_parameters`;
/*!40000 ALTER TABLE `calc_parameters` DISABLE KEYS */;
INSERT INTO `calc_parameters` (`id`, `name`, `value`, `description`) VALUES
	(1, 'tax_rate', 0.070, 'GST'),
	(2, 'online_store_prct', 0.034, 'Online store percentage charge on total amount'),
	(3, 'online_store_markup', 0.500, 'Online store flat markup ');
/*!40000 ALTER TABLE `calc_parameters` ENABLE KEYS */;

DELETE FROM `delivery_partner`;
/*!40000 ALTER TABLE `delivery_partner` DISABLE KEYS */;
INSERT INTO `delivery_partner` (`id`, `govt_issued_id`, `name`, `billing_rate`, `billing_unit_id`) VALUES
	(1, '201409568C', 'GOGOVAN SINGAPORE PTE. LTD.', 15.00, 3);
/*!40000 ALTER TABLE `delivery_partner` ENABLE KEYS */;

DELETE FROM `delivery_status`;
/*!40000 ALTER TABLE `delivery_status` DISABLE KEYS */;
INSERT INTO `delivery_status` (`id`, `name`) VALUES
	(1, 'ASSIGNED'),
	(2, 'DELIVERED'),
	(3, 'FAILED');
/*!40000 ALTER TABLE `delivery_status` ENABLE KEYS */;

DELETE FROM `dish`;
/*!40000 ALTER TABLE `dish` DISABLE KEYS */;
INSERT INTO `dish` (`id`, `name`, `description`, `portion_weight`, `portion_count`, `unit_id`) VALUES
	(1, 'Pizza Sauce', 'Roast Tomato & Veg Pasta & Pizza Sauce', 400.00, 4, 1),
	(2, 'Hummus', '', 70.00, 1, 1),
	(3, 'Avocado Pesto', '', 70.00, 1, 1),
	(4, 'Chicken Patty', 'Sweet Potato- Quinoa & Chicken Patty', 330.00, 6, 1),
	(5, 'Chicken Meatballs', 'Chicken, Carrot & Spinach Meatballs', 300.00, 12, 1),
	(6, 'Quinoa Patty', 'Sweet Potato- Beet & Quinoa Patties', 330.00, 6, 1),
	(7, 'Tempeh balls', 'Vegetarian Tempeh Balls', 300.00, 12, 1),
	(8, 'Blackbean Brownie', '', 300.00, 6, 1),
	(9, 'Chia Cookie', 'Almond-Oat & Chia Cookie', 240.00, 12, 1);
/*!40000 ALTER TABLE `dish` ENABLE KEYS */;

DELETE FROM `dish_ingredient`;
/*!40000 ALTER TABLE `dish_ingredient` DISABLE KEYS */;
INSERT INTO `dish_ingredient` (`id`, `ingredient_weight`, `dish_id`, `ingredient_id`, `unit_id`) VALUES
	(1, 225.00, 5, 30, 1),
	(2, 30.00, 5, 31, 1),
	(3, 25.00, 5, 13, 1),
	(4, 25.00, 5, 5, 1),
	(5, 30.00, 5, 32, 1),
	(6, 30.00, 5, 33, 1),
	(7, 12.00, 5, 34, 1),
	(8, 5.00, 5, 64, 1),
	(9, 1.00, 5, 19, 1),
	(10, 1.00, 5, 56, 1),
	(11, 50.00, 5, 58, 1),
	(12, 40.00, 4, 28, 1),
	(13, 150.00, 4, 26, 1),
	(14, 100.00, 4, 27, 1),
	(15, 75.00, 4, 5, 1),
	(16, 5.00, 4, 64, 1),
	(17, 15.00, 4, 38, 1),
	(18, 20.00, 4, 29, 1),
	(19, 1.00, 4, 19, 1),
	(20, 50.00, 4, 58, 1),
	(21, 35.00, 2, 20, 1),
	(22, 5.00, 2, 17, 1),
	(23, 1.00, 2, 64, 1),
	(24, 1.00, 2, 21, 1),
	(25, 1.00, 2, 19, 1),
	(26, 15.00, 2, 57, 1),
	(27, 15.00, 2, 59, 2),
	(28, 100.00, 3, 24, 1),
	(29, 14.00, 3, 25, 1),
	(30, 2.00, 3, 64, 1),
	(31, 3.00, 3, 17, 1),
	(32, 0.50, 3, 19, 1),
	(33, 15.00, 3, 57, 1),
	(34, 400.00, 1, 60, 1),
	(35, 50.00, 1, 61, 1),
	(36, 85.00, 1, 62, 1),
	(37, 30.00, 1, 13, 1),
	(38, 65.00, 1, 63, 1),
	(39, 120.00, 1, 5, 1),
	(40, 15.00, 1, 64, 1),
	(41, 60.00, 1, 17, 1),
	(42, 1.50, 1, 18, 1),
	(43, 1.00, 1, 19, 1),
	(44, 1.00, 1, 56, 1),
	(45, 90.00, 9, 52, 1),
	(46, 23.00, 9, 44, 1),
	(47, 12.00, 9, 45, 1),
	(48, 20.00, 9, 51, 1),
	(49, 8.00, 9, 53, 1),
	(50, 25.00, 9, 47, 1),
	(51, 35.00, 9, 48, 1),
	(52, 35.00, 9, 54, 1),
	(53, 2.00, 9, 50, 1),
	(54, 0.50, 9, 19, 1),
	(55, 65.00, 8, 43, 1),
	(56, 25.00, 8, 44, 1),
	(57, 6.00, 8, 46, 1),
	(58, 50.00, 8, 45, 1),
	(59, 50.00, 8, 47, 1),
	(60, 55.00, 8, 48, 1),
	(61, 0.50, 8, 19, 1),
	(62, 1.00, 8, 50, 1),
	(63, 5.00, 8, 49, 1),
	(64, 150.00, 6, 26, 1),
	(65, 50.00, 6, 36, 1),
	(66, 50.00, 6, 37, 1),
	(67, 25.00, 6, 28, 1),
	(68, 45.00, 6, 5, 1),
	(69, 20.00, 6, 38, 1),
	(70, 35.00, 6, 29, 1),
	(71, 5.00, 6, 64, 1),
	(72, 1.00, 6, 19, 1),
	(73, 1.00, 6, 56, 1),
	(74, 50.00, 6, 58, 1),
	(75, 200.00, 7, 39, 1),
	(76, 45.00, 7, 40, 1),
	(77, 75.00, 7, 5, 1),
	(78, 7.00, 7, 64, 1),
	(79, 20.00, 7, 41, 1),
	(80, 20.00, 7, 59, 2),
	(81, 1.00, 7, 42, 1),
	(82, 1.00, 7, 19, 1),
	(83, 50.00, 7, 58, 1);
/*!40000 ALTER TABLE `dish_ingredient` ENABLE KEYS */;

DELETE FROM `employee`;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;

DELETE FROM `employee_role`;
/*!40000 ALTER TABLE `employee_role` DISABLE KEYS */;
INSERT INTO `employee_role` (`id`, `name`) VALUES
	(2, 'ASSISTANT'),
	(1, 'HEAD CHEF');
/*!40000 ALTER TABLE `employee_role` ENABLE KEYS */;

DELETE FROM `facility`;
/*!40000 ALTER TABLE `facility` DISABLE KEYS */;
INSERT INTO `facility` (`id`, `name`, `contact`, `phone_number`, `email`, `address_line_1`, `address_line_2`, `unit_number`, `pin_code`, `billing_rate`, `notes`, `billing_unit_id`) VALUES
	(1, 'Cravings', 'Cynthia Tan', 86858786, '', '6 TEBING LANE', '', '#01-05', 828835, 15.00, '', 4);
/*!40000 ALTER TABLE `facility` ENABLE KEYS */;

DELETE FROM `ingredient`;
/*!40000 ALTER TABLE `ingredient` DISABLE KEYS */;
INSERT INTO `ingredient` (`id`, `name`, `brand_name`, `cost_price`, `measure`, `notes`, `category_id`, `source_id`, `unit_id`) VALUES
	(4, 'Tomato (Organic)', NULL, 1.25, 100.00, '', 2, 3, 1),
	(5, 'Onion, Red', NULL, 0.15, 100.00, '', 2, 1, 1),
	(6, 'Bell Pepper, Red  (Organic)', NULL, 2.50, 100.00, '', 2, 3, 1),
	(8, 'Broccoli (Organic)', NULL, 2.30, 100.00, '', 2, 3, 1),
	(12, 'Bell Pepper, Green (Organic)', NULL, 2.25, 100.00, '', 2, 3, 1),
	(13, 'Carrot', NULL, 0.18, 100.00, '', 2, 1, 1),
	(15, 'Garlic (Organic)', NULL, 2.25, 100.00, '', 2, 3, 1),
	(17, 'Oil, EVOO', NULL, 1.50, 100.00, 'Extra Virgin Olive Oil', 1, 1, 1),
	(18, 'Basil, Dried ', NULL, 23.80, 100.00, '', 2, 1, 1),
	(19, 'Sea Salt', 'Origins Healthfood', 0.47, 100.00, '', 1, 1, 1),
	(20, 'Garbanzo Beans', NULL, 0.20, 100.00, '', 1, 6, 1),
	(21, 'Cumin, Ground', NULL, 1.00, 100.00, '', 1, 6, 1),
	(24, 'Avocado', NULL, 1.08, 100.00, '', 2, 1, 1),
	(25, 'Basil, Fresh (Organic)', 'Oh farms sweet basil', 10.83, 100.00, '', 2, 1, 1),
	(26, 'Potato, Sweet Orange', '', 0.75, 100.00, '', 2, 3, 1),
	(27, 'Chicken Fillet (Kee Song)', '', 2.22, 100.00, '', 4, 4, 1),
	(28, 'Quinoa', 'Bob\'s Red Mill', 2.20, 100.00, '', 1, 6, 1),
	(29, 'Wheatgerm', NULL, 0.83, 100.00, '', 1, 1, 1),
	(30, 'Chicken Minced', '', 1.03, 100.00, '', 4, 4, 1),
	(31, 'Spinach', NULL, 1.60, 100.00, '', 2, 3, 1),
	(32, 'Bread', 'Fairprice Wholemeal', 0.38, 100.00, 'One packet of 450 gms. Each slice 30 gm.', 3, 1, 1),
	(33, 'Whole Milk', 'Magnolia', 0.46, 100.00, '', 3, 1, 1),
	(34, 'Tomato Paste', 'Delmonte', 0.73, 100.00, '', 1, 1, 1),
	(36, 'Potato, Russet', NULL, 0.20, 100.00, '', 2, 1, 1),
	(37, 'Beetroot', NULL, 1.20, 100.00, '', 2, 1, 1),
	(38, 'Coriander', NULL, 2.40, 100.00, '', 2, 1, 1),
	(39, 'Tempeh', NULL, 0.65, 100.00, '', 3, 1, 1),
	(40, 'Parmesan Cheese, Grated', 'Perfect Italian', 5.60, 100.00, '', 3, 1, 1),
	(41, 'Garbanzo Flour', 'Rajdhani', 0.45, 100.00, '', 1, 6, 1),
	(42, 'Oregano, Dried', NULL, 31.50, 100.00, '', 1, 1, 1),
	(43, 'Black Beans, Dried', NULL, 0.70, 100.00, '', 1, 6, 1),
	(44, 'Oats, Whole Rolled', 'Origins Healthfood', 0.90, 100.00, '', 1, 1, 1),
	(45, 'Chocolate Chips, Semi-sweet ', 'Redman @ PH', 0.72, 100.00, '', 1, 1, 1),
	(46, 'Cocoa Powder', 'Hersheys', 2.90, 100.00, '', 1, 1, 1),
	(47, 'Honey', 'Origins Healthfood', 2.10, 100.00, '', 1, 1, 1),
	(48, 'Oil, Coconut', 'Medella', 0.93, 100.00, '', 1, 1, 1),
	(49, 'Vanilla Extract', 'Heilala, NZ (Mustafa)', 15.90, 100.00, '', 1, 1, 1),
	(50, 'Baking Powder', 'Bake King', 1.71, 100.00, '', 1, 1, 1),
	(51, 'Almonds, Whole ', 'Gold Ribbon', 3.65, 100.00, '', 1, 1, 1),
	(52, 'Almonds, Ground ', 'Redman @ PH', 1.76, 100.00, '', 1, 1, 1),
	(53, 'Chia Seeds', 'Phoon huat', 2.80, 100.00, '', 1, 1, 1),
	(54, 'Banana', 'Delmonte', 0.18, 100.00, '', 2, 1, 1),
	(56, 'Pepper, Black', 'Fairprice', 3.60, 100.00, '', 1, 1, 1),
	(57, 'Lime Juice', NULL, 0.56, 100.00, '', 2, 1, 1),
	(58, 'Oil, Canola', 'Fairprice', 0.33, 100.00, 'For brushing', 1, 1, 1),
	(59, 'Water', '', 0.00, 0.00, '', 5, 7, 2),
	(60, 'Tomato', '', 0.30, 100.00, '', 2, 1, 1),
	(61, 'Bell Pepper, Green', '', 0.39, 100.00, '', 2, 1, 1),
	(62, 'Bell Pepper, Red', '', 1.73, 100.00, '', 2, 1, 1),
	(63, 'Broccoli', '', 1.26, 100.00, '', 2, 1, 1),
	(64, 'Garlic', '', 1.15, 100.00, '', 2, 1, 1);
/*!40000 ALTER TABLE `ingredient` ENABLE KEYS */;

DELETE FROM `ingredient_category`;
/*!40000 ALTER TABLE `ingredient_category` DISABLE KEYS */;
INSERT INTO `ingredient_category` (`id`, `name`) VALUES
	(1, 'Dry Goods'),
	(2, 'Fruit/Veg'),
	(4, 'Meat'),
	(3, 'Perishables'),
	(5, 'Utilities');
/*!40000 ALTER TABLE `ingredient_category` ENABLE KEYS */;

DELETE FROM `ingredient_source`;
/*!40000 ALTER TABLE `ingredient_source` DISABLE KEYS */;
INSERT INTO `ingredient_source` (`id`, `name`) VALUES
	(1, 'Fair Price'),
	(4, 'Kee Song'),
	(5, 'Meat Club'),
	(3, 'Quan Fa'),
	(2, 'RedMart'),
	(7, 'Utilities'),
	(6, 'Wet Market');
/*!40000 ALTER TABLE `ingredient_source` ENABLE KEYS */;

DELETE FROM `measurement_unit`;
/*!40000 ALTER TABLE `measurement_unit` DISABLE KEYS */;
INSERT INTO `measurement_unit` (`id`, `name`) VALUES
	(3, 'COUNT'),
	(5, 'DAILY'),
	(1, 'GRAM'),
	(4, 'HOURLY'),
	(2, 'ML'),
	(6, 'MONTHLY'),
	(7, 'YEARLY');
/*!40000 ALTER TABLE `measurement_unit` ENABLE KEYS */;


DELETE FROM `order_status`;
/*!40000 ALTER TABLE `order_status` DISABLE KEYS */;
INSERT INTO `order_status` (`id`, `name`) VALUES
	(3, 'CANCELLED'),
	(1, 'COMPLETED'),
	(2, 'RECEIVED'),
	(4, 'ROLLED');
/*!40000 ALTER TABLE `order_status` ENABLE KEYS */;

DELETE FROM `package`;
/*!40000 ALTER TABLE `package` DISABLE KEYS */;
INSERT INTO `package` (`id`, `name`, `description`, `category_id`, `sales_price`) VALUES
	(1, 'Lunch Kit (Veg)', '', 1, 68.00),
	(2, 'Lunch Kit (Non Veg)', '', 1, 68.00);
/*!40000 ALTER TABLE `package` ENABLE KEYS */;

DELETE FROM `package_category`;
/*!40000 ALTER TABLE `package_category` DISABLE KEYS */;
INSERT INTO `package_category` (`id`, `name`) VALUES
	(2, 'Birthday Party'),
	(1, 'Lunch Kit');
/*!40000 ALTER TABLE `package_category` ENABLE KEYS */;

DELETE FROM `package_dish`;
/*!40000 ALTER TABLE `package_dish` DISABLE KEYS */;
INSERT INTO `package_dish` (`id`, `package_id`, `dish_id`) VALUES
	(7, 1, 1),
	(6, 1, 2),
	(2, 1, 3),
	(8, 1, 6),
	(9, 1, 7),
	(1, 1, 8),
	(5, 1, 9),
	(14, 2, 1),
	(11, 2, 2),
	(12, 2, 3),
	(13, 2, 4),
	(4, 2, 5),
	(3, 2, 8),
	(10, 2, 9);
/*!40000 ALTER TABLE `package_dish` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
