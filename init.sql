-- 建立 test 資料庫
CREATE DATABASE IF NOT EXISTS test;

-- 使用 test 資料庫
USE test;

-- 建立 user 資料表
CREATE TABLE `user` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `points` INT,
  `cash` FLOAT
);

-- 建立 product 資料表
CREATE TABLE `product` (
  `id` VARCHAR(1) PRIMARY KEY,
  `name` VARCHAR(255) NOT NULL,
  `price` INT NOT NULL,
  `points` INT NOT NULL,
  `can_be_exchanged` TINYINT(1) NOT NULL
);

-- 插入產品資料
INSERT INTO `product` (id, name, price, points, can_be_exchanged)
VALUES
  ('A', 'Product A', 1000, 5, 0),
  ('B', 'Product B', 2000, 3, 0),
  ('C', 'Product C', 4000, 8, 0),
  ('D', 'Product D', 1200, 5, 0),
  ('E', 'Product E', 0, 10, 1),
  ('F', 'Product F', 0, 20, 1);
