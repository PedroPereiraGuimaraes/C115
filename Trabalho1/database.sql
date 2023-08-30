DROP DATABASE IF EXISTS c115;
CREATE DATABASE c115;

USE c115;

CREATE TABLE questions(
   id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
   question VARCHAR(500),
   a VARCHAR(50),
   b VARCHAR(50),
   c VARCHAR(50),
   d VARCHAR(50),
   answer VARCHAR(1)
);

INSERT INTO questions() 
VALUES(default, "Qual é a capital do Brasil?", "Rio de Janeiro","São Paula","Brasília","Salvador","c");
INSERT INTO questions() 
VALUES(default, "Qual é a fórmula química da água?", "H2O","CO2","NaCl","C12H22O11","a");
INSERT INTO questions() 
VALUES(default, "Quem escreveu o livro “Dom Casmurro”", "Machado de Assis","José de Alencar","Guimarães Rosa","Clarice Lispector","a");
INSERT INTO questions() 
VALUES(default, "Qual é o maior planeta do sistema solar?", "Terra","Marte","Júpiter","Saturno","c");
