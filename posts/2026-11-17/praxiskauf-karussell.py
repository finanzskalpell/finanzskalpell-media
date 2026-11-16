# Paar 10 · Praxiskauf · Karussell (Nachbau Website-Design 2026, 16.11.2026; Texte, Zahlen und Quellen aus dem Quelle-Doc „Quelle Paar 10“ (karussell.html, Fassung 19.10.2026), Fußzeilen gekürzt auf „Quelle: … · keine Anlage-/Steuerberatung“)
TAG = 'Praxiskauf'
DISC = 'Unsere Inhalte dienen ausschließlich der allgemeinen Information und stellen keine Anlageberatung, Steuerberatung oder sonstige individuelle Finanzberatung dar. Kapitalanlagen sind mit Risiken verbunden.'
HI = '<span style="color:#CDB6FF">%s</span>'
CSS = '''
.display .mk{margin-left:0}
.bars{margin-top:26px;display:flex;flex-direction:column;gap:16px}
.brow .h{display:flex;justify-content:space-between;align-items:baseline;font:600 32px/1.1 Inter;color:var(--body);margin-bottom:10px}
.brow .h b{font:800 48px/1 Inter;color:#fff;letter-spacing:-.03em;font-variant-numeric:tabular-nums;white-space:nowrap}
.brow.main .h b{color:#CDB6FF}
.trk{height:64px;border-radius:20px;background:rgba(255,255,255,.08);overflow:hidden;display:flex;gap:4px}
.trk span{display:block;height:100%}
.lgd{margin-top:16px;display:flex;gap:40px;font:600 30px/1.2 Inter;color:#fff}
.lgd span{display:flex;align-items:center;gap:12px}
.lgd i{display:block;width:30px;height:18px;border-radius:5px}
'''
# Balkenbreiten: Wert ÷ 200.000 € × 100 % (wie im Quelle-Doc: ÷ 200.000 × Spurbreite)
# 2013/14: 76.900 € = 38,45 % · 38.400 € = 19,2 % · 2023/24: 112.300 € = 56,15 % · 78.000 € = 39,0 %
BARS = '''<div class="bars">
      <div class="brow"><div class="h"><span>2013/2014</span><b>115.300&nbsp;€</b></div><div class="trk"><span style="width:38.45%;background:rgba(255,255,255,.55)"></span><span style="width:19.2%;background:rgba(255,255,255,.22)"></span></div></div>
      <div class="brow main"><div class="h"><span>2023/2024</span><b>190.300&nbsp;€</b></div><div class="trk"><span style="width:56.15%;background:#fff"></span><span style="width:39%;background:rgba(255,255,255,.38)"></span></div></div>
    </div>
    <div class="lgd"><span><i style="background:#fff"></i>Kaufpreis</span><span><i style="background:rgba(255,255,255,.38)"></i>Ausstattung und Umbau</span></div>'''
CARDS = [
 dict(pillintro='Für Ärztinnen und Ärzte',
      display='Eigene Praxis: <span class="mk">112.300&nbsp;€</span> sind nur der Anfang?', display_size=118,
      sub='Kaufpreis, Geräte, Umbau: was eine Hausarztpraxis im Schnitt wirklich kostet.', sub_size=44, sub_margin=56),
 dict(eyebrow='Die eine Zahl', display='Hausarztpraxis übernehmen, alles drin:', display_size=80,
      big='190.000&nbsp;€', big_size=178,
      split=[('Kaufpreis der Praxis','112.300&nbsp;€',True),('Ausstattung und Umbau','78.000&nbsp;€',False)],
      foot='Quelle: apoBank/Zi, Existenzgründungsanalyse 2023/2024 (Nov. 2025) · Einzelpraxis, Durchschnitt · 112.300 + 78.000 = 190.300 € · keine&nbsp;Anlage&#8209;/Steuerberatung'),
 dict(eyebrow='Schritt 1 · Der Kaufpreis', display='Die meisten zahlen unter 100.000&nbsp;€ Kaufpreis', display_size=80,
      calc=[('bis 100.000 €','','61&nbsp;%',False),('100.000 bis 200.000 €','','31&nbsp;%',False),('über 200.000 €','','8&nbsp;%',False),('Im Schnitt','','112.300&nbsp;€',True)], calc_small=True,
      sub='Im Kaufpreis steckt beides: Geräte und Möbel (Substanzwert) und der Patientenstamm mit Lage und Zulassung (ideeller Wert).', sub_size=34, sub_margin=30,
      foot='Quelle: apoBank/Zi 2023/2024, hausärztliche Einzelpraxis · Kaufpreis ohne Ausstattung, Durchschnitt · keine&nbsp;Anlage&#8209;/Steuerberatung'),
 dict(eyebrow='Schritt 2 · Dazu kommt die Ausstattung', display='Geräte und Umbau: doppelt so teuer wie vor zehn Jahren', display_size=64,
      raw=BARS,
      sub='Umbau, Geräte, IT und Startkapital: 78.000&nbsp;€ heute, 38.400&nbsp;€ vor zehn Jahren. Zwei Fünftel der ganzen Investition.', sub_size=33, sub_margin=26,
      foot='Quelle: apoBank/Zi, hausärztliche Einzelpraxis-Übernahme · 2013/14: 76.900 + 38.400 € · 2023/24: 112.300 + 78.000 € · keine&nbsp;Anlage&#8209;/Steuerberatung'),
 dict(eyebrow='Schritt 3 · Was andere Fächer zahlen', display='Je nach Fach: 62.400 bis&nbsp;529.100&nbsp;€', display_size=76,
      calc=[('Psychiatrie, Psychotherapie','','62.400&nbsp;€',False),('Hausarztpraxis','',HI%'190.300&nbsp;€',False),('Kinderheilkunde','','237.400&nbsp;€',False),('Gynäkologie','','290.400&nbsp;€',False),('Orthopädie','','529.100&nbsp;€',True)], calc_small=True,
      sub='Übernahme einer Einzelpraxis, Kaufpreis plus Ausstattung. Je mehr Geräte ein Fach braucht, desto teurer.', sub_size=33, sub_margin=26,
      foot='Quelle: apoBank/Zi, Existenzgründungsanalyse 2023/2024 · Orthopädie: Kaufpreis allein 397.700&nbsp;€ · keine&nbsp;Anlage&#8209;/Steuerberatung'),
 dict(eyebrow='Vergleich · 2014 gegen 2024', display='Die Hausarztpraxis kostet heute 65&nbsp;% mehr', display_size=80,
      calc=[('Kaufpreis','','76.900 → 112.300&nbsp;€',False),('Ausstattung und Umbau','','38.400 → 78.000&nbsp;€',False),('Gesamt damals','','115.300&nbsp;€',False),('Gesamt heute','','190.300&nbsp;€',True)], calc_small=True,
      sub='Der Kaufpreis stieg um 46&nbsp;%, die Ausstattung um 103&nbsp;%. Auf dem Land kostet die Übernahme 151.700&nbsp;€, in der Großstadt 205.000&nbsp;€.', sub_size=34, sub_margin=28,
      foot='Quelle: apoBank/Zi, hausärztliche Einzelpraxis-Übernahme · Prozentwerte berechnet · Neugründung: 227.500 € · keine&nbsp;Anlage&#8209;/Steuerberatung'),
 dict(eyebrow='Merkzettel · vor dem ersten Gespräch', display='Drei Dinge, die du <span class="vi" style="white-space:nowrap">vorher nachsiehst.</span>',
      items=[('Kaufpreis im Exposé:','Ist er aufgeteilt in Geräte und Möbel (Substanzwert) und Patientenstamm (ideeller Wert)?'),('Anlageverzeichnis des Abgebers:','Wie alt sind Geräte und IT, was muss in zwei Jahren neu?'),('Niederlassungsberatung deiner KV:','Übernahme, BAG-Eintritt oder Neugründung, und welche Förderung es in der Region gibt.')],
      foot='Keine&nbsp;Anlage&#8209;/Steuerberatung · Zahlen bekommst du vom Abgeber, deiner KV und deiner Steuerberatung'),
 dict(eyebrow='Schick es weiter', display='<span class="vi">Teile das</span> mit Kolleginnen und Kollegen, die sagen: „Der Kaufpreis geht ja noch.“', display_size=80,
      sub='<b>Übernahme oder Neugründung: Was wäre deins?</b> Schreib es in die Kommentare.', sub_size=42, sub_margin=44, disc=DISC),
]
