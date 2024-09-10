from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Configurazione per la connessione al database MySQL
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Ilfoggia1',
    'database': 'mydb'
}


# Funzione per connettersi al database e recuperare i dati
def get_all_data_from_db():
    conn = None
    cursor = None  # Inizializza il cursore come None
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Esecuzione della query per selezionare tutte le colonne
        query = "SELECT * FROM Orologi"
        cursor.execute(query)

        # Recupero di tutti i risultati della query
        results = cursor.fetchall()

        # Creazione di una lista di tuple, dove ogni tupla contiene i dati di una riga
        lista_valori = [row for row in results]

    except mysql.connector.Error as err:
        print(f"Errore: {err}")
        lista_valori = []

    finally:
        # Chiudi il cursore solo se è stato creato
        if cursor is not None:
            cursor.close()
        # Chiudi la connessione solo se è stata creata
        if conn is not None:
            conn.close()

    return lista_valori


# Definizione della rotta principale che restituisce i dati come JSON
@app.route('/')
def mostra_dati():
    dati = get_all_data_from_db()
    return jsonify(dati)


if __name__ == '__main__':
    app.run(debug=True)
