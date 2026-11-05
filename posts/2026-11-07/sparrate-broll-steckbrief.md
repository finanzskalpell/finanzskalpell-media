# Steckbrief · B-Roll-Reel Paar 13 Sparrate (Geldanlage), Sa 7.11.2026, Abend-Videostrom

- **Variante:** B „Ansprache + Liste“ (Vorlage `overlay-b-ansprache-liste.html`, Fassung 2 mit Schutzzonen 260/1440/780), Hook im dunklen Kasten (`hook box`), weil der Clip oben hell ist (Fenster, Deckenlicht).
- **Clip:** `incoming/broll/broll-zwei-aerztinnen-gehen-durch-korridor.mp4` (720×1280, 24 fps, 10,03 s, eine Einstellung, zwei Personen von hinten im Klinikflur; kein Namensschild, kein Logo; in der Tiefe ein kleines grünes Hinweisschild, nicht lesbar). Gebaut am 5.11.2026, Länge 9,676 s (5 Takte micro-house-2); Datei 9,708 s (233 Frames).
- **Themen-Chip:** Sparrate.
- **Hook (ab Frame 0, 66 px, 3 Zeilen):** „Wenn du mit 60 aufhören willst: Dein Startalter bestimmt deine Sparrate.“ (11 Wörter; Begriff Sparrate genannt, Alltagsgröße 60.)
- **Punkt 1 (Takt 1, 1,935 s):** „Fängst du mit 30 an, reichen **498 €** im Monat.“
- **Punkt 2 (Takt 2, 3,870 s):** „Fängst du mit 40 an, brauchst du schon **1.082 €**.“
- **Punkt 3 (Takt 3, 5,806 s):** „Fängst du mit 50 an, sind es **3.051 €** im Monat.“
- **Schluss (Takt 4, 7,741 s, violetter Kasten):** „Speichern für den Tag, an dem du deine eigene Rate rechnest.“
- **Fußzeile (Takt 1, 1,935 s):** „Das Beispiel rechnet mit 500.000 € mit 60 und 6 % p. a. vor Steuern und Kosten · keine Anlageberatung“
- **Feste Elemente (Frame 0):** Kopfzeile (Chip + Label „Finanzen von und für Ärztinnen und Ärzte“), KI-Schild „KI-generiert“ rechts oben, Hook. Kein Logo.

## Nachrechnung (Python, 5.11.2026)

Rate = Ziel × i ÷ ((1 + i)^n − 1), i = 0,06 ÷ 12, n = Jahre × 12, Ziel 500.000 €:
- Start 30 (30 Jahre): 497,75 € → 498 €
- Start 40 (20 Jahre): 1.082,16 € → 1.082 €
- Start 50 (10 Jahre): 3.051,03 € → 3.051 €
- Verhältnisse: 1.082 ÷ 498 = 2,17; 3.051 ÷ 498 = 6,13 (Paar-Doc: „mehr als die doppelte Rate“, „das Sechsfache“).
Quelle: Paar 13, Steckbrief Feld 2 und 3 sowie Abschnitt Rechenwege (eigene Rechnung, Stand 4.10.2026).

## Musik

micro-house-2.wav, 124,02 BPM, beat 0,4838 s, Takt 1,9352 s, Start 22,277 s (beat.py, `--dauer 12 --min-start 15`, abschnitt_rel_db −0,44), T = 5 Takte = 9,676 s, Downbeats bei 1,935 / 3,870 / 5,806 / 7,741 s. Mix −14,94 LUFS (mix.sh, linearer Durchlauf).

## Prüfungen (5.11.2026)

1. **Textregeln:** jede Zeile ein Satz mit Verb (reichen, brauchst, sind, rechnest, rechnet), keine Etiketten; die Kette Hook (Startalter bestimmt die Rate) → drei Zahlen nach Startalter → Schluss (eigene Rate rechnen) läuft ohne Sprung; Lauttest bestanden („Fängst du mit 40 an, brauchst du schon 1.082 €“ sagt eine Kollegin so im Flur).
2. **Verständlichkeit:** Hook nennt den Begriff (Sparrate) und die Alltagsgröße (60), keine Abkürzungen, keine Fachwörter; drei Zahlen insgesamt, eine je Zeile.
3. **Eindeutigkeit:** „bestimmt“ bezieht sich auf das feste Beispiel (Ziel und Rendite in der Fußzeile), die Zahlen nennen jeweils das Startalter als Vergleichsseite; „reichen“, „brauchst“, „sind es“ beziehen sich auf dasselbe Ziel 500.000 € mit 60; „im Monat“ steht in Punkt 1 und 3, Punkt 2 folgt in derselben Reihe. Beispiel in der Fußzeile als Beispiel gekennzeichnet, 6 % p. a. vor Steuern und Kosten.
4. **Fakten:** alle drei Beträge aus Paar 13, mit Python nachgerechnet (oben).
5. **safezone.js:** clean (erste Fassung hatte FOOT-OVERLAP bei t = 8,19 / 9,63, weil Fußzeile und Schluss je drei Zeilen hatten; beide gekürzt, danach clean).
6. **Kontaktbogen, Frame 0, Endframe:** angesehen; Frame 0 zeigt Kopfzeile und Hook komplett, Endframe drei Kästen plus Schlusskasten und Fußzeile im Kasten, nichts abgeschnitten, nichts in der Icon-Spalte.

## Dateien

`sa-abend-broll-sparrate/`: `overlay.html`, `sparrate-broll-stumm.mp4`, `sparrate-broll-stumm-check.jpg`, `sparrate-broll-reel.mp4` (h264 1080×1920, aac, 9,708 s), `beat-sparrate-broll.json`, `sparrate-broll-captions.md`, `check-00.jpg`, `check-end.jpg`, `check-pair.jpg`.
