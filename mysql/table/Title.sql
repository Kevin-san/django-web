use alvin;

create table IF NOT EXISTS `Title`(
   `Id` INT UNSIGNED AUTO_INCREMENT,
   `Type` VARCHAR(100) character set utf8 NOT NULL,
   `Href` VARCHAR(100) NOT NULL,
   `Title` VARCHAR(100) character set utf8 NOT NULL,
   `DeleteFlag` TINYINT NOT NULL DEFAULT 0,
   `submission_user` VARCHAR(30),
   `submission_date` DATE,
   PRIMARY KEY ( `id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;