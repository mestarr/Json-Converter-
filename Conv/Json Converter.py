import pdfplumber
import json
import os
import docx

def pdf_to_json(pdf_path, output_path):
    """
    Konvertiert eine PDF-Datei in JSON, indem sie den Text jedes PDF-Seite extrahiert.

    :param pdf_path: Pfad zur Eingabe-PDF
    :param output_path: Pfad zur Ausgabe-JSON
    """
    data = {"pages": []}  # JSON-Struktur vorbereiten
    
    try:
        # Öffne die PDF-Datei
        with pdfplumber.open(pdf_path) as pdf:
            for page_number, page in enumerate(pdf.pages, start=1):
                # Extrahiere Text von jeder Seite
                text = page.extract_text()
                if text:  # Falls Inhalt gefunden wurde
                    data["pages"].append({
                        "page_number": page_number,
                        "content": text
                    })
                else:
                    data["pages"].append({
                        "page_number": page_number,
                        "content": "Diese Seite enthält keinen Text."
                    })

        # Speichere als JSON
        with open(output_path, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)

        print(f"Die PDF wurde erfolgreich in JSON umgewandelt: {output_path}")

    except FileNotFoundError:
        print(f"Die Datei {pdf_path} wurde nicht gefunden!")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")

def docx_to_json(docx_path, output_path):
    """
    Konvertiert eine DOCX-Datei in JSON, indem sie den Text extrahiert.

    :param docx_path: Pfad zur Eingabe-DOCX
    :param output_path: Pfad zur Ausgabe-JSON
    """
    data = {"pages": []}  # JSON-Struktur vorbereiten
    
    try:
        # Öffne die DOCX-Datei
        doc = docx.Document(docx_path)
        
        # Extrahiere den Text aus jedem Absatz
        paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
        
        # Speichere alle Absätze als eine einzelne "Seite"
        data["pages"].append({
            "page_number": 1,
            "content": "\n".join(paragraphs)
        })

        # Speichere als JSON
        with open(output_path, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)

        print(f"Die DOCX wurde erfolgreich in JSON umgewandelt: {output_path}")

    except FileNotFoundError:
        print(f"Die Datei {docx_path} wurde nicht gefunden!")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")

def convert_to_json(input_path, output_path=None):
    """
    Konvertiert eine PDF- oder DOCX-Datei in JSON, basierend auf der Dateiendung.

    :param input_path: Pfad zur Eingabedatei (PDF oder DOCX)
    :param output_path: Pfad zur Ausgabe-JSON (optional)
    """
    # Überprüfe, ob die Datei existiert
    if not os.path.exists(input_path):
        print(f"Die Datei {input_path} wurde nicht gefunden!")
        return
    
    # Wenn kein Ausgabepfad angegeben, erstelle einen basierend auf dem Eingabepfad
    if output_path is None:
        file_name = os.path.splitext(os.path.basename(input_path))[0]
        output_path = f"{file_name}_ausgabe.json"
    
    # Bestimme den Dateityp anhand der Dateiendung
    file_extension = os.path.splitext(input_path)[1].lower()
    
    if file_extension == ".pdf":
        pdf_to_json(input_path, output_path)
    elif file_extension == ".docx":
        docx_to_json(input_path, output_path)
    else:
        print(f"Nicht unterstütztes Dateiformat: {file_extension}")
        print("Unterstützte Formate: PDF, DOCX")


# ---- Hauptprogramm ----
if __name__ == "__main__":
    # Dateipfade anpassen (Eingangs-Datei und Ausgabe-JSON)
    input_file = "C:/Users/paun/Desktop/phy/REST-JUnit-JSON.pdf"   # Pfad zur Eingabedatei
    output_json = "REST-JUnit-JSON_ausgabe.json"  # Pfad zur Ausgabe-JSON-Datei

    convert_to_json(input_file, output_json)