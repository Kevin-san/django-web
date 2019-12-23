use alvin;

create table IF NOT EXISTS `LessonDetails`(
	`Id` INT UNSIGNED AUTO_INCREMENT,
	`TitleHref` VARCHAR(100) NOT NULL,
	`Index` INT NOT NULL,
	`Type` VARCHAR(100) NOT NULL,
	`Text` VARCHAR(8000) character set utf8 NOT NULL,
	`DeleteFlag` TINYINT NOT NULL DEFAULT 0,   
	`submission_user` VARCHAR(30),
	`submission_date` DATE,
	PRIMARY KEY ( `Id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
