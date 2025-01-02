# MySQL

# SQL - Structured Query Language
# MSSql, Postgre,
"""
# Baze (Database)
    # Tabele (Tables)

# Baza (WebProdavnica)
    # Tabele: 
        Korisnici
            id - broj -jedinstveni broj
            name - ime
        
        kupovine
            id
            name
            price
            
            
Query:
>> upit ka bazi za neke podatke
    >> SELECT: Uzmi podatke            
        >> SELECT name FROM users >> uzmi imena od korisnika
    
    >> INSERT INTO: Upisemo podatke u bazu
        >> INSERT INTO users >> napravi novog korisnika
        
    >> DELETE: brisemo podatke iz base
        DELETE FROM users WHERE name = "Toma : Brisemo iz tabele korisnika "Toma"
        
    >> UPDATE: Updatovali ili azurirali neki podatak
        >> Menjamo ime nekog user-a
        
    
    
    
PROGRAMI - NACINI ZA KONEKCIJU

    >> PyCharm
    >> MySQL Workbench
    >> Datagrip
    >> terminala >> komandne linije
    

"""

# Napravio bazu sa imenom "python_db_test", napravio tabelu "users" sa kolonama ["id", "username", "password", "age"]