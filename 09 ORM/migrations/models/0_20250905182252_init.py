from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `clas` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(32) NOT NULL COMMENT 'Class Name'
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `course` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(32) NOT NULL COMMENT 'Course Name'
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `student` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(32) NOT NULL COMMENT 'Student Name',
    `pwd` VARCHAR(32) NOT NULL COMMENT 'Student Password',
    `stud_num` INT NOT NULL COMMENT 'Student Number',
    `clas_id` INT NOT NULL,
    CONSTRAINT `fk_student_clas_4be9b492` FOREIGN KEY (`clas_id`) REFERENCES `clas` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `teacher` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(32) NOT NULL COMMENT 'Teacher Name',
    `pwd` VARCHAR(32) NOT NULL COMMENT 'Teacher Password',
    `teac_num` INT NOT NULL COMMENT 'Teacher Number'
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `student_course` (
    `student_id` INT NOT NULL,
    `course_id` INT NOT NULL,
    FOREIGN KEY (`student_id`) REFERENCES `student` (`id`) ON DELETE CASCADE,
    FOREIGN KEY (`course_id`) REFERENCES `course` (`id`) ON DELETE CASCADE,
    UNIQUE KEY `uidx_student_cou_student_0d222b` (`student_id`, `course_id`)
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
