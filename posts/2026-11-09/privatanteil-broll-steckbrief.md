# Steckbrief · B-Roll-Reel Paar 26 Privatanteil (Praxismanagement), Mo 9.11.2026, Abend-Videostrom

- **Variante:** A „Eine Aussage“ (Vorlage `overlay-a-eine-aussage.html`, Fassung 2 mit Schutzzonen 260/1440/780), Hook im dunklen Kasten (`hook box`), weil der Clip hell ist (weiße Liege, helle Wand).
- **Clip:** `incoming/broll/broll-ultraschall-bauch-allgemeinmedizin.mp4` (720×1280, 24 fps, 10,03 s, eine ruhige Einstellung, Hand mit Schallkopf auf dem Bauch, Ultraschallmonitor unscharf im Hintergrund ohne lesbaren Text; kein Namensschild, kein Logo). Gebaut am 5.11.2026 als **stummes Video**, Länge 9,62 s (5 Takte micro-house-1 bei 124,7 BPM, beat 0,4812 s; Musik fehlt in der Cloud und wird auf dem Mac gemischt, deshalb kein beat.json und kein Mix). Datei 9,625 s (231 Frames).
- **Themen-Chip:** Privatanteil.
- **Hook (ab Frame 0, 70 px statt 80 px, 3 Zeilen):** „Im Schnitt kommen nur noch 16 % vom Umsatz von Privatpatienten.“ (10 Wörter; „16 %“ hellviolett; „Privatpatienten“ als Alltagswort wie im Paar-Doc-Hook, in der Fußzeile „Mittelwerte je Inhaber“.)
- **Zeile 1 (Takt 2, 3,85 s):** „Seit 2011 zahlt die Kasse je Praxisinhaber **39,6 %** mehr.“
- **Zeile 2 (Takt 3, 5,77 s):** „Die Privateinnahmen stiegen in der Zeit nur um **5,9 %**.“
- **Schluss (Takt 4, 7,70 s):** „Warum, steht in der Caption.“
- **Fußzeile (Takt 1, 1,92 s):** „Das Zi-Praxis-Panel nennt Mittelwerte je Inhaber über alle Fachgruppen, 2023 vorläufig, 2011 aus dem Jahresbericht 2015, nominal · keine Anlageberatung“
- **Feste Elemente (Frame 0):** Kopfzeile, KI-Schild rechts oben, Hook. Kein Logo.
- **Layout-Anpassung:** Hook 70 px statt 80 px (bei 80 px brach „nur“ in eine vierte Zeile um); Zeilenbreite gemessen 756 px bei 3 Zeilen à 74 px.

## Nachrechnung (Python, 5.11.2026)

- Privatanteil 2023: 57.900 ÷ 360.300 = 16,07 % → 16,1 % (im Hook gerundet „16 %“); 2011: 54.700 ÷ 274.600 = 19,92 % → 19,9 %.
- Kasse (GKV) je Inhaber 2011 → 2023: 285.100 ÷ 204.300 − 1 = 39,55 % → **39,6 %**.
- Privateinnahmen je Inhaber 2011 → 2023: 57.900 ÷ 54.700 − 1 = 5,85 % → **5,9 %**.
- Gesamteinnahmen: 360.300 ÷ 274.600 − 1 = 31,21 % (nur in der Caption-Logik, nicht im Bild).
Quelle: Paar 26, Steckbrief Feld 2 und 3, Datentabelle und Abschnitt Rechenwege (Zi-Praxis-Panel, Vorabinformation 2020–2023, vorläufig; Jahresbericht 2015, Tabelle 3), Stand 20.10.2026.

## Musik (vorgegeben, auf dem Mac zu mischen)

micro-house-1, 124,7 BPM, beat 0,4812 s, Takt 1,9248 s, T = 5 Takte = 9,62 s, Downbeats bei 1,92 / 3,85 / 5,77 / 7,70 s. Startpunkt auf dem Mac mit beat.py bestimmen, dann `mix.sh privatanteil-broll-stumm.mp4 Musik/micro-house-1.wav <start> privatanteil-broll-reel.mp4` und `beat-privatanteil-broll.json` anlegen.

## Prüfungen (5.11.2026)

1. **Textregeln:** jede Zeile ein Satz mit Verb (kommen, zahlt, stiegen, steht, nennt); Kette Hook (16 % Privatanteil) → Kasse +39,6 % seit 2011 → Privat nur +5,9 % → Schluss (Warum in der Caption) läuft ohne Sprung; Lauttest bestanden.
2. **Verständlichkeit:** Hook nennt Begriff (Privatpatienten, Umsatz) und Alltagsgröße (16 % vom Umsatz), keine Abkürzungen im Bild außer „Zi“ in der Fußzeile; drei Zahlen insgesamt, eine je Zeile.
3. **Eindeutigkeit:** „nur noch“ im Hook ist der Trend, den Zeile 1 und 2 belegen (2011: 19,9 %); „mehr“ in Zeile 1 heißt „mehr als 2011“ („Seit 2011“ steht in der Zeile), Zeile 2 nennt denselben Zeitraum („in der Zeit“); beide Zahlen sind nominale Einnahmen je Inhaber (Fußzeile „nominal“, „Mittelwerte je Inhaber“). Regelfall (Mittelwert) als Hauptaussage, Corona-Delle nur in der Caption.
4. **Fakten:** 16,1 %, 39,6 %, 5,9 % aus Paar 26, mit Python nachgerechnet (oben). Prüfhinweis aus dem Paar-Doc: die Reihe 2011 → 2023 verbindet zwei verschiedene Zi-Praxisauswahlen (Jahresbericht 2015 und Vorabinformation 2020–23); in Kommentaren so erklären.
5. **safezone.js:** clean (bei 80 px und 70 px Hook; die 80-px-Fassung hatte nur den Umbruch in eine vierte Zeile, keine Zonenverletzung).
6. **Kontaktbogen, Frame 0, Endframe:** angesehen; Frame 0 zeigt Kopfzeile und Hook komplett in drei Zeilen, Endframe zwei Zahlenkästen plus Schlusskasten und Fußzeile im Kasten, nichts in der Icon-Spalte.

## Dateien

`mo-abend-broll-privatanteil/`: `overlay.html`, `privatanteil-broll-stumm.mp4` (h264 1080×1920, ohne Ton, 9,625 s), `privatanteil-broll-stumm-check.jpg`, `privatanteil-broll-captions.md`, `check-00.jpg`, `check-end.jpg`, `check-pair.jpg`.
