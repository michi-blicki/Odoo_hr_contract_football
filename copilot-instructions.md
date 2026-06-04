# Copilot Instructions – hr_contract_football (Odoo 18 CE)

## Zweck dieser Datei
Diese Datei ist der operative Wiedereinstieg für dieses Add-on.
Sie ist bewusst **kritisch, hinterfragend und faktenbasiert** aufgebaut.

## Arbeitsmodus (verbindlich)
1. **Keine Annahmen treffen.** Nur auf Basis von Code, Manifest, Security-Regeln und dokumentierten Anforderungen arbeiten.
2. **Bei Unklarheit immer Rückfragen stellen**, bevor Code geändert wird.
3. **Enterprise-Level Qualität** einhalten: Sicherheit, Nachvollziehbarkeit, saubere Migration, keine Quick-Fixes.
4. **Scope diszipliniert halten**: nur Standard-Odoo + OCA, keine zusätzlichen Fremdabhängigkeiten ohne explizite Freigabe.
5. Add-on ist **in Entwicklung / Pre-Alpha**: Änderungen immer mit Regression-Risiko einschätzen.
6. **Sprache Textbausteine**: Textelemente werden im Sourcode immer in Englisch formulert. Texte werden erst in der Übersetzungsphase in andere Sprachen übersetzt. Es gibt ausschliesslich englische Textelemente im Code.

## Faktenlage (Stand Codebasis)
* Modul: `hr_contract_football`
* Odoo-Version: 18
* Edition-Ziel: Community Edition
* Manifest-Version: `18.0.0.0.0`
* Lizenz im Manifest: `AGPL-3`
* README-Status: „under heavy development / do not use yet"
* Zielgruppe: grosse, enterprise-ähnliche Vereine

## Beschreibung des Addons
Dieses Addon erweitert den Funktionsumfang von `hr_contract` um spezifische Features in Verträgen von Fussballspielern, Trainern und weiteren fussballnahen Rollen. Es soll dabei helfen, die komplexen Anforderungen von mittelgrossen und grossen Fussballvereinen abzudecken und die entsprechenden Variablen in den Verträgen zentral zu verwalten.

## Business Anforderungen
* Arbeitsverträge mit Trainern, Spielern und anderen Rollen in Fussballvereinen erfordern spezifische Vertragsvariablen, die nicht im Standard von `hr_contract` abgebildet sind. Diese Variablen sind von Vertrag zu Vertrag unterschiedlich und müssen den individuellen Anforderungen der Vertragspartner angepasst werden können.
* Das Addon stellt die Variablen zur Verfügung und dokumentiert diese, so dass Vertragsmanager und HR-Verantwortliche die Variablen in den Verträgen sowie für die Abrechnung nutzen können.

## Technische Anforderungen
* so wenig wie möglich mit eigenen Datenmodellen arbeiten, sondern die bestehenden Modelle vom Odoo Addon `hr_contract`.
* Wenn zusätzliche Datenmodelle notwendig werden, müssen diese so gestaltet sein, dass von `hr_contract` darauf zugegriffen werden kann.
* Neue Datenmodelle müssen so gestaltet sein, dass sie in der Community Edition von Odoo 18 lauffähig sind, ohne dass Enterprise-spezifische Funktionen oder Module erforderlich sind.
* Alle neuen Funktionen müssen so implementiert werden, dass sie in der Community Edition von Odoo 18 lauffähig sind, ohne dass Enterprise-spezifische Funktionen oder Module erforderlich sind.
* Existiert bereits ein Datenmodell oder eine Funktionalität in `hr_contract`, die für die Anforderung genutzt werden kann, muss diese genutzt werden, anstatt ein neues Datenmodell oder eine neue Funktionalität zu erstellen.

## Neue Felder für `hr_contract`
Feld | Typ | Description (en_US) | Bezeichnung (de_CH) | Beschreibung
-----|-----|---------------------|---------------------|-------------
`signing_fee` | Monetary | Signing Fee | Ablösesumme | Einmalige Zahlung, die bei Vertragsunterzeichnung fällig wird, oft bei Spielern, die von einem anderen Verein wechseln.`
`signing_fee_pay_date` | Date | Signing Fee Pay Date | Datum der Ablösesumme | Das Datum, an dem die Ablösesumme fällig wird.
`transfer_type` | Selection | Transfer Type | Transferart | Art des Transfers, z.B. Leihe, Kauf, Free Transfer.
`termination_clause_type` | Selection | Termination Clause Type | Kündigungsklauseltyp | Art der Kündigungsklausel, z.B. fest, variabel, etc.
`termination_amount` | Monetary | Termination Amount | Kündigungsbetrag | Betrag, der im Falle einer Vertragskündigung fällig wird.
`loyality_bonus` | Monetary | Loyalty Bonus | Loyalitätsbonus | Bonus, der an Spieler oder Trainer gezahlt wird, die über einen bestimmten Zeitraum im Verein bleiben, um ihre Treue zu belohnen.
`loyality_bonus_pay_date` | Date | Loyalty Bonus Pay Date | Datum des Loyalitätsbonus | Das Datum, an dem der Loyalitätsbonus fällig wird.
