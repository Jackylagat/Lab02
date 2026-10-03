import csv


def carica_da_file(file_path):
    try:
        with open(file_path) as file:
            reader = list(csv.DictReader(file,skipinitialspace=True))
        return reader
    except FileNotFoundError:
        return None




def aggiungi_foto(album, codice, titolo, autore, mese, anno, file_path):
   nuova_foto = {
       "codice": codice,
       "titolo": titolo,
       "autore": autore,
       "mese": mese,
       "anno": anno,
   }

   for canzone in album:
       if canzone["codice"] == codice:
           return None
   if mese > 12 or mese < 1:
       return None

   else:
       album.append(nuova_foto)
       riga_csv = ','.join(str(valore) for valore in nuova_foto.values())+ '\n'
       try:
           with open(file_path, 'a', encoding="utf-8") as file:
               file.write(riga_csv)
           return True
       except FileNotFoundError:
           return None



def cerca_foto(album, codice):
    for canzone in album:
        if canzone["codice"] == codice:
            risultato = ', '.join(str(v) for v in canzone.values())
            return risultato
    return None




def elenco_foto_anno_per_titolo(album, anno):
    lista_foto = []

    for foto in album:
        if foto['anno'] == str(anno):
            lista_foto.append(foto['titolo'])

    lista_foto.sort()
    if lista_foto:
        return lista_foto
    else:
        return None


def main():
    album = []
    file_path = "album_fotografico.csv"

    while True:
        print("\n--- MENU ALBUM FOTOGRAFICO ---")
        print("1. Carica album da file")
        print("2. Aggiungi una nuova foto")
        print("3. Cerca una foto per codice")
        print("4. Elenco foto di un anno (ordinato per titolo)")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                album = carica_da_file(file_path)
                if album is not None:
                    break

        elif scelta == "2":
            if not album:
                print("Prima carica l'album da file.")
                continue

            codice = input("Codice della foto: ").strip()
            titolo = input("Titolo: ").strip()
            autore = input("Autore: ").strip()
            try:
                mese = int(input("Mese (1-12): ").strip())
                anno = int(input("Anno: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per mese e anno.")
                continue

            foto = aggiungi_foto(album, codice, titolo, autore, mese, anno, file_path)
            if foto:
                print(f"Foto aggiunta con successo!")
            else:
                print("Non è stato possibile aggiungere la foto.")

        elif scelta == "3":
            if not album:
                print("L'album è vuoto.")
                continue

            codice = input("Inserisci il codice della foto da cercare: ").strip()
            risultato = cerca_foto(album, codice)
            if risultato:
                print(f"Foto trovata: {risultato}")
            else:
                print("Foto non trovata.")

        elif scelta == "4":
            if not album:
                print("L'album è vuoto.")
                continue

            try:
                anno = int(input("Inserisci l'anno da consultare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_foto_anno_per_titolo(album, anno)
            if titoli is not None:
                print(f'\nFoto del {anno}:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))
            else:
                print(f"Nessuna foto trovata per l'anno {anno}.")

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()




