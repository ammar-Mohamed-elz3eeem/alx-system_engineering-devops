GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
SHOW GRANTS FOR 'holberton_user'@'localhost';
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
SELECT user, Repl_slave_priv FROM mysql.user
