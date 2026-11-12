# Steckbrief · B-Roll-Reel Paar 36 — Krankenkasse 2027 (Variante A „Eine Aussage“)

- **Posttag:** Fr 13.11.2026, Abend-Videostrom (Entwurf, Christoph liest vor dem Einplanen)
- **Clip:** `broll-haende-desinfizieren-02.mp4` (720×1280, 24 fps, 10,0 s, eine Einstellung, keine Schilder, Logos oder Bildschirme; heller Clip, deshalb Hook im Kasten `hook box`). Clip ist damit verbraucht.
- **Themen-Chip:** Krankenkasse
- **Hook (ab Frame 0, 76 px, Marker auf „teurer“):** „Die Krankenkasse soll ab Januar für viele von uns teurer werden.“
- **Zeile 1 (Takt 1, 2,380 s):** „Voll trifft es dich, wenn du gesetzlich versichert bist und mindestens 6.375 € brutto im Monat verdienst.“
- **Zeile 2 (Takt 2, 4,759 s):** „Dein Beitrag soll dann im Monat um 49,22 € steigen.“
- **Schluss (Takt 3, 7,139 s, weißer Kasten):** „Warum, steht in der Caption.“
- **Fußzeile (Takt 1):** „Beispiel: dein Anteil am Höchstbeitrag 508,59 € → 557,81 € (BMG 30.10.2026). Rechengrößen 2027: vom Kabinett beschlossen, Bundesrat offen. Deine Kasse kann abweichen · keine Anlage-/Steuerberatung“
- **Länge:** 4 Takte = 9,518 s (bei 100,86 BPM wären 5 Takte 11,9 s und länger als der Clip); Video 9,54 s, 24 fps wie im Skill (broll.sh).
- **Musik:** bed-under-voiceover-1, 100,86 BPM, Takt 2,3795 s, Start 44,207 s (Downbeat), −14,5 LUFS.

## Nachrechnung (Python)

- 5.812,50 € × 8,75 % = 508,59 € · 6.375 € × 8,75 % = 557,81 € · Differenz 49,22 € (562,50 € × 8,75 % = 49,22 €) · 6.375 − 5.812,50 = 562,50 €. 8,75 % = Hälfte von 14,6 % + 2,9 %. Stimmt mit dem Paar-Doc überein.

## Prüfungen (12.11.2026)

- **Textregeln:** jede Zeile ein ganzer Satz mit Verb, jede prüfbar; zwei Zahlen im Inhaltsblock (6.375 €, 49,22 €), je Zeile eine; Kette Hook (für viele teurer) → wen es voll trifft → um wie viel → Grund in der Caption.
- **Hook-Test:** 11 Wörter, nennt „Krankenkasse“, ohne Vorwissen lesbar, verrät weder die 49,22 € noch den Grund. Abweichung von der Vorlage A: Hook ohne Zahl, weil die Zahl die Antwort wäre.
- **Eindeutigkeit:** Was steigt, ist dein monatlicher Anteil am Beitrag zur gesetzlichen Krankenversicherung. „soll“ und „geplant“/„Bundesrat offen“ statt endgültigem Beschluss. Die 49,22 € stehen nie ohne Bedingung im Bild (Zeile 1 mit der Bedingung bleibt stehen). „für viele von uns“: laut Paar-Doc gilt es für viele Fachärztinnen und Fachärzte; wer zwischen 5.812,50 € und 6.375 € verdient, zahlt weniger als 49,22 € mehr (Caption).
- **Fakten:** alle Zahlen aus dem Paar-Doc (BMG 30.10.2026, Kabinett 7.10.2026, BR-Drs. 576/26), nachgerechnet.
- **safezone.js:** clean (Frame 0, jede Einblendung, Ende).
- **Prüfbilder angesehen:** 0 s, 2,2 s (Vorschaubild: nur Kopfzeile und Hook, Marker fertig), 2,85 s, 5,25 s, 7,6 s, 9,4 s.

## Offen

- Bundesrat (voraussichtlich 20.11.2026) nicht neu geprüft; nach der Sitzung „soll“, Fußzeile und Caption anpassen.
- Schriftgröße der Inhaltszeilen 40 statt 42 px, damit die fünfzeilige Fußzeile nicht berührt wird.
