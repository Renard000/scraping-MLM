DELIMITER //


CREATE PROCEDURE db_create()
BEGIN

   CREATE DATABASE IF NOT EXISTS UserDB;
   USE UserDB;

   CREATE TABLE IF NOT EXISTS User(
      id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
      product_name VARCHAR(100),
      member_price FLOAT UNSIGNED,
      retail_price FLOAT UNSIGNED,
      date_now VARCHAR(100),
      last_date VARCHAR(100)
   );
END //
DELIMITER ;

/*CREATE PROCEDURE write_in_db()

BEGIN
   INSERT INTO User(product_name, member_price, retail_price, date_now, last_date)
   VALUE ('%S', '%S', '%S', NOW(), NOW())
   ON DUPLICATE KEY UPDATE last_date = NOW()
   
END*/
