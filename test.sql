CREATE TABLE study(
   id int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '学生id号',
   username varchar(30) NOT NULL DEFAULT '' COMMENT '学生名字',
  class tinyint(3) unsigned NOT NULL,
  sex enum('男','女','保密')  CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '保密' COMMENT '性别',
  addtime int(10) NOT NULL DEFAULT '0',
   PRIMARY KEY (id)
)ENGINE=InnoDB  COMMENT = '学生表';
insert into study (username,class,sex)VALUES('小王',1,'男'),('小四',2,'女');
select * from study;