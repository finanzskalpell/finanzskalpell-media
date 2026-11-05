# Steckbrief · B-Roll-Reel Paar 12 Steuerklasse III/V (Finanzen), So 8.11.2026, Abend-Videostrom

- **Variante:** C „POV mit Wendung“ (Vorlage `overlay-c-pov-wendung.html`, Fassung 2 mit Schutzzonen 260/1440/780), Hook im dunklen Kasten (`hook box`), weil der Clip sehr hell ist (weißer Glasflur).
- **Clip:** `incoming/broll/broll-korridor-02.mp4` (720×1280, 24 fps, 10,005 s, eine Einstellung, Arzt im weißen Kittel von hinten in einem hellen Glasflur; kein Namensschild, kein Logo). **Auffälligkeit:** zwischen etwa 1,7 und 6,7 s zieht am rechten Bildrand ein Stationsschild „Station 4 / Kardiologie“ vorbei (klein, leicht unscharf, generisch, ohne Klinikname); die Alternative `broll-chefaerztin-korridor.mp4` hat ein größeres, zentral stehendes Schild „Station 3 / Röntgen“ und ist deshalb nicht genommen worden; `broll-arzt-von-hinten-moderne-praxis.mp4` ist mit 6,0 s zu kurz. Christoph entscheidet beim Lesen, ob das Schild stört.
- **Länge:** T = 5 Takte lofi-house-2 = 10,172 s; der Clip ist mit 10,005 s um 0,17 s kürzer als T, deshalb hält `broll.sh` in diesem Ordner das letzte Bild per `tpad=stop_mode=clone` (Mechanik aus Variante D) für die fehlenden 4 Frames, die in den Musik-Fade-out fallen. Datei 10,208 s (245 Frames).
- **Themen-Chip:** Steuerklasse.
- **Hook (ab Frame 0, 84 px, 3 Zeilen):** „POV: Du hast Steuerklasse III und mehr Netto im Monat.“ (10 Wörter, Begriff Steuerklasse genannt.)
- **Situationssatz (Takt 1, 2,034 s; blendet bei 4,069 s aus):** „Dein Arbeitgeber zieht dir jeden Monat weniger Lohnsteuer ab.“
- **Frage (Takt 1 + 2 Schläge, 3,052 s; blendet bei 8,138 s aus):** „Wie viel Steuer spart ihr damit im Jahr?“
- **Zahl 1 (Takt 2, 4,069 s):** „Mit III/V statt IV/IV spart ihr im Jahr **0 €**.“
- **Zahl 2 (Takt 3, 6,103 s):** „Das Splitting bringt euch **169 €**, mit jeder Steuerklasse.“
- **Wendung (Takt 4, 8,138 s, violetter Kasten):** „III und V verschieben eure Steuer nur.“ Erklärsatz: „Im Bescheid gleicht das Finanzamt die Lohnsteuer aus, mit III/V oft als Nachzahlung.“
- **Fußzeile (Takt 1, 2,034 s):** „Das Beispiel rechnet mit 100.000 € und 60.000 € zu versteuerndem Einkommen, Tarif 2026, § 32a Abs. 5 EStG · keine Anlage‑/Steuerberatung“ (Fußzeilen-Vorgabe 31.10.2026, weil Steuerthema).
- **Feste Elemente (Frame 0):** Kopfzeile, KI-Schild rechts oben, Hook. Kein Logo.
- **Layout-Anpassungen gegenüber der Vorlage:** `.st.a` 46 px statt 50 px, `small` 29 px statt 31 px, `em` mit `white-space:nowrap` und geschütztem Leerzeichen vor „€“ (in der ersten Fassung brach „169 €“ um); Frage wie in der Vorlage auf Schlag 3 von Takt 1 (nicht Downbeat), weil fünf Takte nur vier Downbeats für fünf Schritte haben.

## Nachrechnung (Python, 5.11.2026; Tarif 2026 nach § 32a EStG, Beträge abgerundet)

- T(100.000) = 0,42 × 100.000 − 11.135,63 = 30.864 €; T(60.000): z = 4,2201, (173,10 × z + 2.397) × z + 1.034,87 = 14.233 €; einzeln 45.097 €.
- Splitting: T(80.000) = 22.464 €, × 2 = 44.928 €; Vorteil 45.097 − 44.928 = **169 €**.
- Unterschied III/V gegen IV/IV in der festgesetzten Jahressteuer bei Zusammenveranlagung: **0 €** (die Steuerklasse steuert nur den Lohnsteuerabzug, § 38b, § 39b EStG; Pflichtveranlagung bei III/V § 46 Abs. 2 Nr. 3a EStG).
- Zur Caption: 160.000 + 0 €: T(160.000) = 56.064 €, Vorteil 56.064 − 44.928 = 11.136 €.
Quelle: Paar 12, Steckbrief Feld 2 bis 4 und Abschnitt Rechenwege (Stand 3.10.2026).

## Musik

lofi-house-2.wav, 117,97 BPM, beat 0,5086 s, Takt 2,0344 s, Start 17,507 s (beat.py, `--dauer 12 --min-start 15`, abschnitt_rel_db +0,05), T = 5 Takte = 10,172 s, Downbeats bei 2,034 / 4,069 / 6,103 / 8,138 s. Mix −14,63 LUFS (mix.sh, linearer Durchlauf).

## Prüfungen (5.11.2026)

1. **Textregeln:** jede Zeile ein Satz mit Verb (hast, zieht ab, spart, bringt, verschieben, gleicht aus); Kette Hook (III, mehr Netto) → Situation (weniger Lohnsteuer im Monat) → Frage (wie viel im Jahr?) → 0 € → Splittingvorteil unabhängig von der Steuerklasse → Wendung (verschieben, nicht sparen) läuft ohne Sprung; Lauttest bestanden.
2. **Verständlichkeit:** Hook ohne Vorwissen lesbar, „Steuerklasse III“ ist Alltagsbegriff; „Splitting“ wird im Erklärsatz der Wendung in der Sache erklärt (Finanzamt gleicht im Bescheid aus) und in der Caption ausführlich; Paragraf nur in der Fußzeile; drei Zahlen insgesamt (0 €, 169 €, Beispielbeträge nur in der Fußzeile).
3. **Eindeutigkeit:** Vergleich nennt beide Seiten (III/V statt IV/IV), Zeitraum „im Jahr“ steht bei beiden Zahlen; „0 €“ bezieht sich laut Paar-Doc auf die festgesetzte Einkommensteuer bei Zusammenveranlagung (nicht auf Elterngeld oder andere Lohnersatzleistungen, die am Netto hängen); „169 €“ ist der Splittingvorteil des Beispiels, Beispiel in der Fußzeile; „oft eine Nachzahlung“ bewusst weich wie im Paar-Doc („meist zu wenig abgezogen“ ist Erfahrung, kein Gesetz).
4. **Fakten:** 0 €, 169 € und die Beispielbeträge aus Paar 12, mit Python nachgerechnet (oben).
5. **safezone.js:** clean (zwei Vorfassungen mit FOOT-OVERLAP/BOTTOM, Texte und Schriftgrößen angepasst, Zonen unverändert).
6. **Kontaktbogen, Frame 0, Frame 6,8 s, Endframe:** angesehen; Frame 0 zeigt Kopfzeile und Hook komplett, höchstens drei Kästen zugleich, Fußzeile im Kasten, nichts in der Icon-Spalte. Schild rechts am Bildrand siehe Auffälligkeit oben.

## Dateien

`so-abend-broll-steuerklasse/`: `overlay.html`, `broll.sh` (mit tpad-Zeile), `steuerklasse-broll-stumm.mp4`, `steuerklasse-broll-stumm-check.jpg`, `steuerklasse-broll-reel.mp4` (h264 1080×1920, aac, 10,208 s), `beat-steuerklasse-broll.json`, `steuerklasse-broll-captions.md`, `check-00.jpg`, `check-68.jpg`, `check-end.jpg`, `check-pair.jpg`, `check-trio.jpg`.
