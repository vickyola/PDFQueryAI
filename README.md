# PDFQueryAI: RAG-Lösung ohne Speichern

Dieses Tool ermöglicht die Beantwortung technischer Fragen basierend auf Informationen aus PDF-Dokumenten. Es verwendet eine Retrieval-Augmented Generation (RAG)-Pipeline mit modernen Language Models (LLMs). Die Dokumente werden ohne explizites Speichern in einem Dateisystem verarbeitet, und das System kann direkt über eingebettete Vektoren auf die Inhalte zugreifen.

---

## Voraussetzungen

Stellen Sie sicher, dass die folgenden Abhängigkeiten installiert sind:

- Python 3.8 oder neuer
- Notwendige Python-Pakete (siehe `requirements.txt`)

---

## Einrichtung

### 1. Datenpfad und API-Key

- **Pfad zum Dataset:** Legen Sie den Pfad zu Ihrem Dataset (PDF-Dateien) in einer Umgebungsvariablen `DATASET_PATH` fest.
- **OpenAI API-Key:** Setzen Sie den OpenAI API-Key in einer Umgebungsvariablen `OPENAI_API_KEY`.

Beispiel für `.env` oder direkte Shell-Befehle:

```
export DATASET_PATH="/pfad/zu/ihren/pdf-dokumenten" export OPENAI_API_KEY="Ihr-OpenAI-API-Key"
```

##  Installation der Abhängigkeiten

Installieren Sie die notwendigen Bibliotheken mit folgendem Befehl:

```
pip install -r requirements.txt
```


## Skalierung

Der Aufbau von RAG-Systemen für mehrere Dokumente ist schwierig, vor allem, wenn sichergestellt werden soll, dass das LLM Antworten mit einer bestimmten Detailtiefe liefert und nicht nur eine allgemeine Zusammenfassung.

### Persistenter Vectorindex (database)
Die vorgestellte RAG-Implementierungen stößt bei wachsenden Datenmengen an ihre Grenzen und erfordert alternative Ansätze zur effizienten Datenhaltung und -verarbeitung. Ein Schritt ist die Auslagerung des Vektorspeichers in persistente Speichersysteme.

### Multi-Agent-Architektur
Ein besonders effektiver Ansatz zur Bewältigung großer Dokumentenmengen ist eine Multi-Agent-Architektur. Dabei übernimmt ein übergeordneter Agent (Top-Agent) die Orchestrierung verschiedener spezialisierter Agenten, die als Werkzeuge für spezifische Aufgaben dienen. Diese Architektur ermöglicht es, je nach Benutzeranfrage die am besten geeignete Suchmethode auszuwählen. 

### Indexierungsstrategien
Es können hybride Indexierungsmethoden, beispielsweise semantische Suchen (Vectorindex) mit Keyword Suche oder Dokumentenzusammenfassungen (Summaryindex) eingesetzt werden, um bestmögliche Ergebnisse zu erzielen.

### Chunking-Strategien
Die Entwicklung ausgefeilter Methoden zur Dokumentensegmentierung ist entscheidend für die Qualität der Ergebnisse. Hierarchische Chunking-Ansätze können helfen, sowohl lokale Details als auch übergreifende Zusammenhänge zu erhalten.

### Caching-Mechanismen

Die Implementierung intelligenter Caching-Strategien kann die Performance deutlich verbessern, indem häufig abgefragte Informationen im Schnellzugriff zur Verfügung gestellt werden.

### Embedding Models 

Meine Recherchen haben aufgezeigt, dass ein Feintuning des Embedding Models vielversprechend sein könnte.
Der Wechsel vom langchain OpenAIEmbeddings Standardmodell (text-embedding-ada-002) zum Modell "text-embedding-3-large" hat in diesem Suchtool zu signifikanten Verbesserungen geführt. 
Für größere Daten Mengen gibt es weitere Embedding Modelle die eine Verbesserung des Context Verständnis versprechen.

### Knowledge Graphs
Eine weitere interessante Entwicklung im Bereich der RAG-Systeme, die ich mir bei Gelegenheit näher ansehen möchte, ist die Integration von Knowledge Graphs. Diese ermöglichen eine semantisch reichere Darstellung von Dokumenteninhalten und deren Beziehungen untereinander. Die Kombination von Knowledge Graphen mit RAG-Systemen verspricht eine verbesserte Kontextualisierung und Präzision bei der Informationsextraktion.
