from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `course` ADD `teacher_id` INT NOT NULL;
        ALTER TABLE `course` ADD CONSTRAINT `fk_course_teacher_2de38fe7` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`id`) ON DELETE CASCADE;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `course` DROP FOREIGN KEY `fk_course_teacher_2de38fe7`;
        ALTER TABLE `course` DROP COLUMN `teacher_id`;"""
