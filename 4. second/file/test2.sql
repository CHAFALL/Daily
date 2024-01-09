-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema ssafy_web_db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema ssafy_web_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `ssafy_web_db` DEFAULT CHARACTER SET utf8 ;
USE `ssafy_web_db` ;

-- -----------------------------------------------------
-- Table `ssafy_web_db`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ssafy_web_db`.`user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `department` VARCHAR(45) NULL,
  `position` VARCHAR(45) NULL,
  `name` VARCHAR(45) NULL,
  `user_id` VARCHAR(45) NULL,
  `password` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ssafy_web_db`.`conference_category`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ssafy_web_db`.`conference_category` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ssafy_web_db`.`conference`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ssafy_web_db`.`conference` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `call_start_time` DATETIME NULL DEFAULT now(),
  `call_end_time` DATETIME NULL DEFAULT now(),
  `thumbnail_url` VARCHAR(45) NULL,
  `title` VARCHAR(45) NULL,
  `description` VARCHAR(45) NULL,
  `is_active` TINYINT NULL,
  `conference_category` INT NOT NULL,
  `owner_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_conference_conference_category1_idx` (`conference_category` ASC) VISIBLE,
  INDEX `fk_conference_user1_idx` (`owner_id` ASC) VISIBLE,
  CONSTRAINT `fk_conference_conference_category1`
    FOREIGN KEY (`conference_category`)
    REFERENCES `ssafy_web_db`.`conference_category` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_conference_user1`
    FOREIGN KEY (`owner_id`)
    REFERENCES `ssafy_web_db`.`user` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ssafy_web_db`.`user_conference`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ssafy_web_db`.`user_conference` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `conference_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_user_conference_user_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_user_conference_conference1_idx` (`conference_id` ASC) VISIBLE,
  CONSTRAINT `fk_user_conference_user`
    FOREIGN KEY (`user_id`)
    REFERENCES `ssafy_web_db`.`user` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_user_conference_conference1`
    FOREIGN KEY (`conference_id`)
    REFERENCES `ssafy_web_db`.`conference` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ssafy_web_db`.`conference_history`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ssafy_web_db`.`conference_history` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `action` SMALLINT NULL,
  `inserted_time` DATETIME NULL DEFAULT now(),
  `user_id` INT NOT NULL,
  `conference_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_conference_history_user1_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_conference_history_conference1_idx` (`conference_id` ASC) VISIBLE,
  CONSTRAINT `fk_conference_history_user1`
    FOREIGN KEY (`user_id`)
    REFERENCES `ssafy_web_db`.`user` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_conference_history_conference1`
    FOREIGN KEY (`conference_id`)
    REFERENCES `ssafy_web_db`.`conference` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
