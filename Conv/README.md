# Dokument zu JSON Konverter

Dieses Skript ermöglicht die Konvertierung von PDF- und DOCX-Dateien in das JSON-Format.

## Voraussetzungen

Bevor Sie das Skript verwenden können, stellen Sie sicher, dass Sie die erforderlichen Python-Bibliotheken installiert haben:

```
pip install pdfplumber python-docx
```

## Verwendung

### 1. Als importiertes Modul

Sie können die Funktionen aus dem Skript importieren und in Ihrem eigenen Code verwenden:

```python
from pdf_to_json import convert_to_json

# Konvertieren einer PDF-Datei
convert_to_json("pfad/zur/datei.pdf", "ausgabe.json")

# Konvertieren einer DOCX-Datei
convert_to_json("pfad/zur/datei.docx", "ausgabe.json")

# Ohne Angabe eines Ausgabepfads (automatische Benennung)
convert_to_json("pfad/zur/datei.pdf")  # Erzeugt "datei_ausgabe.json"
```

### 2. Direkte Ausführung

Sie können das Skript auch direkt ausführen:

1. Öffnen Sie die Datei `pdf_to_json.py` in einem Texteditor.
2. Passen Sie die folgenden Zeilen an, um Ihre Eingabe- und Ausgabedatei festzulegen:

```python
input_file = "Pfad/zur/Eingabedatei.pdf"  # oder .docx
output_json = "Ausgabedatei.json"
```

3. Speichern Sie die Datei und führen Sie sie über die Kommandozeile aus:

```
python pdf_to_json.py
```

## Ausgabeformat

Die JSON-Ausgabe hat folgendes Format:

```json
{
    "pages": [
        {
            "page_number": 1,
            "content": "Text der ersten Seite..."
        },
        {
            "page_number": 2,
            "content": "Text der zweiten Seite..."
        },
        ...
    ]
}
```

Bei DOCX-Dateien wird der gesamte Inhalt als eine einzelne "Seite" dargestellt.

## Unterstützte Dateiformate

- PDF (.pdf)
- Microsoft Word (.docx)

## Fehlerbehebung

- Wenn die Datei nicht gefunden werden kann, überprüfen Sie den Pfad.
- Stellen Sie sicher, dass die Datei nicht beschädigt ist.
- Bei Problemen mit der Textextraktion, versuchen Sie, die Datei in ein anderes Format zu konvertieren. 