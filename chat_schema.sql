BEGIN TRANSACTION;

----
-- Table structure for users
----
CREATE TABLE users (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	-- Should be VARCHAR instead, but VARCHAR is not supported by the SQLite3
	name TEXT NOT NULL
);

----
-- Data dump for users, a total of 2 rows
----
INSERT INTO "users" ("id","name") VALUES ('1','Anthony');
INSERT INTO "users" ("id","name") VALUES ('2','Yan');

----
-- Table structure for chats
----
CREATE TABLE chats (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	-- Should be VARCHAR instead, but VARCHAR is not supported by the SQLite3
	name TEXT NOT NULL,
	user1_id INTEGER NOT NULL,
	user2_id INTEGER NOT NULL,
	FOREIGN KEY (user1_id)
      REFERENCES users (id)
         ON DELETE CASCADE
         ON UPDATE NO ACTION
);

----
-- Data dump for chats, a total of 2 rows
----
INSERT INTO "chats" ("id","name","user1_id","user2_id") VALUES ('1','First chat','1','2');
INSERT INTO "chats" ("id","name","user1_id","user2_id") VALUES ('2','Second chat','2','1');

----
-- Table structure for chat_messages
----
CREATE TABLE 'chat_messages' (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	-- Should be VARCHAR instead, but VARCHAR is not supported by the SQLite3
	text TEXT NOT NULL,
	user_id INTEGER NOT NULL, 'datetime'  DATETIME NOT NULL  , 'chat_id'  INTEGER NOT NULL  ,
	FOREIGN KEY (user_id)
      REFERENCES users (id)
         ON DELETE CASCADE
         ON UPDATE NO ACTION
);

----
-- Data dump for chat_messages, a total of 4 rows
----
INSERT INTO "chat_messages" ("id","text","user_id","datetime","chat_id") VALUES ('1','How are you ...???
What are you doing tomorrow?
Can we come up a bar?','1','1594552652','1');
INSERT INTO "chat_messages" ("id","text","user_id","datetime","chat_id") VALUES ('2','Okay. We will go on sunday?','2','1594552686','1');
INSERT INTO "chat_messages" ("id","text","user_id","datetime","chat_id") VALUES ('3','That''s awesome!
I will meet you Sandon Square sharp at 10 AM','1','1594552722','1');
INSERT INTO "chat_messages" ("id","text","user_id","datetime","chat_id") VALUES ('4','Are you still there? I can not come today','2','1594552751','2');

----
-- structure for index User1 on table chats
----
CREATE INDEX 'User1' ON "chats" ("user1_id");

----
-- structure for index User2 on table chats
----
CREATE INDEX 'User2' ON "chats" ("user2_id");

----
-- structure for index User on table chat_messages
----
CREATE INDEX 'User' ON "chat_messages" ("user_id");
COMMIT;
