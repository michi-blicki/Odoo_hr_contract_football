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
`contract_runtime` | Float | Contract Runtime (years) | Vertragslaufzeit (Jahre) | Die vorgesehene Laufzeit des Vertrags in Jahren. Wird zur Berechnung des Enddatums des Vertrags verwendet, basierend auf dem Startdatum.
`contract_optional_extension` | Float | Contract Optional Extension (years) | Optionale Vertragsverlängerung (Jahre) | Die optionale Verlängerungszeit des Vertrags in Jahren, die über die ursprüngliche Laufzeit hinausgeht. Ermöglicht es, eine mögliche Verlängerung des Vertrags zu berücksichtigen.
`signing_fee` | Monetary | Signing Fee | Ablösesumme | Einmalige Zahlung, die bei Vertragsunterzeichnung fällig wird, oft bei Spielern, die von einem anderen Verein wechseln.`
`signing_fee_pay_date` | Date | Signing Fee Pay Date | Datum der Ablösesumme | Das Datum, an dem die Ablösesumme fällig wird.
`transfer_type` | Selection | Transfer Type | Transferart | Art des Transfers, z.B. Leihe, Kauf, Free Transfer.
`termination_clause_type` | Selection | Termination Clause Type | Kündigungsklauseltyp | Art der Kündigungsklausel, z.B. fest, variabel, etc.
`termination_amount` | Monetary | Termination Amount | Kündigungsbetrag | Betrag, der im Falle einer Vertragskündigung fällig wird.
`termination_variable_condition` | Text | Termination Variable Condition | Bedingung für variable Kündigungsklausel | Bedingungen, die erfüllt sein müssen, damit die variable Kündigungsklausel greift, z.B. bestimmte Leistungen des Spielers oder des Teams.
`loyalty_bonus` | Monetary | Loyalty Bonus | Loyalitätsbonus | Bonus, der an Spieler oder Trainer gezahlt wird, die über einen bestimmten Zeitraum im Verein bleiben, um ihre Treue zu belohnen.
`loyalty_bonus_pay_date` | Date | Loyalty Bonus Pay Date | Datum des Loyalitätsbonus | Das Datum, an dem der Loyalitätsbonus fällig wird.
`game_appearance_bonus` | Monetary | Game Appearance Bonus | Bonus für Spieleinsätze | Bonus, der an Spieler gezahlt wird, basierend auf der Anzahl der Spieleinsätze.
`goal_bonus` | Monetary | Goal Bonus | Bonus für Tore | Bonus, der an Spieler gezahlt wird, basierend auf der Anzahl der erzielten Tore.
`clean_sheet_bonus` | Monetary | Clean Sheet Bonus | Bonus für zu Null Spiele | Bonus, der an Torhüter gezahlt wird, basierend auf der Anzahl der Spiele, in denen kein Gegentor kassiert wurde.
`team_success_bonus` | Monetary | Team Success Bonus | Bonus für Teamerfolge | Bonus, der an Spieler und Trainer gezahlt wird, basierend auf den Erfolgen des Teams, z.B. Gewinn von Meisterschaften oder Pokalen.
`release_clause_amount` | Monetary | Release Clause Amount | Ablösesumme bei Ausstiegsklausel | Betrag, der fällig wird, wenn eine im Vertrag festgelegte Ausstiegsklausel aktiviert wird.
`buyout_clause_amount` | Monetary | Buyout Clause Amount | Ablösesumme bei Kaufklausel | Betrag, der fällig wird, wenn eine im Vertrag festgelegte Kaufklausel aktiviert wird.
`loan_conditions` | Text | Loan Conditions | Leihbedingungen | Bedingungen, die für einen Spieler gelten, der auf Leihbasis zu einem anderen Verein wechselt, z.B. Dauer der Leihe, Gehaltsübernahme, etc.
`loan_return_conditions` | Text | Loan Return Conditions | Rückkehrbedingungen bei Leihe | Bedingungen, die für die Rückkehr eines Spielers gelten, der auf Leihbasis zu einem anderen Verein gewechselt ist, z.B. Rückkehrzeitpunkt, Zustand des Spielers, etc.
`sponsorship_conditions` | Text | Sponsorship Conditions | Sponsoringbedingungen | Bedingungen, die für Spieler oder Trainer gelten, die bestimmte Sponsoringverpflichtungen haben, z.B. Teilnahme an Werbeveranstaltungen, Tragen von Markenbekleidung, etc.
`sponsorship_bonus` | Monetary | Sponsorship Bonus | Bonus für Sponsoringverpflichtungen | Bonus, der an Spieler oder Trainer gezahlt wird, die bestimmte Sponsoringverpflichtungen erfüllen.
`trainer_title_bonus` | Monetary | Trainer Title Bonus | Bonus für Trainer Titel | Bonus, der an Trainer gezahlt wird, basierend auf den Titeln, die sie mit dem Team gewinnen, z.B. Gewinn der Meisterschaft, Pokal, etc.
`trainer_title_condition` | Text | Trainer Title Condition | Bedingung für Trainer Titel Bonus | Bedingungen, die erfüllt sein müssen, damit der Trainer den Titelbonus erhält, z.B. Mindestanzahl von Spielen, bestimmte Leistungen des Teams, etc.
`trainer_position_bonus` | Monetary | Trainer Position Bonus | Bonus für Trainerposition | Bonus, der an Trainer gezahlt wird, basierend auf der Position, die das Team am Ende der Saison erreicht, z.B. Gewinn der Meisterschaft, Qualifikation für internationale Wettbewerbe, etc.
`trainer_position_condition` | Text | Trainer Position Condition | Bedingung für Trainer Position Bonus | Bedingungen, die erfüllt sein müssen, damit der Trainer den Positionsbonus erhält, z.B. Mindestanzahl von Spielen, bestimmte Leistungen des Teams, etc.
`trainer_retention_bonus` | Monetary | Trainer Retention Bonus | Bonus für Trainerbindung | Bonus, der an Trainer gezahlt wird, die über einen bestimmten Zeitraum im Verein bleiben, um ihre Bindung zu belohnen.
`trainer_retention_condition` | Text | Trainer Retention Condition | Bedingung für Trainer Retention Bonus | Bedingungen, die erfüllt sein müssen, damit der Trainer den Retention Bonus erhält, z.B. Mindestanzahl von Jahren im Verein, bestimmte Leistungen des Teams, etc.
`trainer_side_jobs_conditions` | Text | Trainer Side Jobs Conditions | Bedingungen für Nebentätigkeiten von Trainern | Bedingungen, die für Trainer gelten, die Nebentätigkeiten ausüben, z.B. Einschränkungen bei der Art der Nebentätigkeit, Genehmigungspflicht durch den Verein, etc.

## Geklärte Entscheidungen (umsetzungsrelevant)
1. Modellstrategie
   Primär Erweiterung von `hr.contract` via `_inherit`. Zusätzliche Hilfsmodelle sind nur erlaubt, wenn eine Anforderung nicht sinnvoll direkt auf `hr.contract` abbildbar ist; solche Modelle müssen von `hr.contract` referenziert werden.

2. Selection-Werte
   * `transfer_type`: `purchase` (Purchase), `free_transfer` (Free Transfer), `loan` (Loan)
   * `termination_clause_type`: `fixed` (Fixed), `variable` (Variable)

3. Laufzeitlogik
   * `contract_runtime` berechnet `date_end` automatisch aus `date_start`.
   * Die Berechnung muss im UI (`@api.onchange`) und serverseitig (`create`/`write`) erfolgen.
   * Umrechnung Jahre -> Monate: `months = contract_runtime * 12` (z.B. 0.25=3, 0.5=6, 0.75=9 Monate).

4. Optionale Verlängerung
   `contract_optional_extension` ist reine Planungsinformation und wird nicht automatisch in `date_end` eingerechnet.

5. Feldbenennung
   Die Schreibweise `loyality_*` wird nicht verwendet. Korrekt ist `loyalty_*`.

6. Währung
   Monetary-Felder nutzen die bestehende Vertragswährung von `hr.contract`; kein zusätzliches Währungsfeld.

7. Fachliche Validierungen
   * Alle Monetary-Felder: Wert muss >= 0 sein.
   * `signing_fee_pay_date` ist Pflicht, wenn `signing_fee` > 0.
   * `loyalty_bonus_pay_date` ist Pflicht, wenn `loyalty_bonus` > 0.
   * Keine globalen Pflichtfelder nach Rolle (Spieler/Trainer); dies bleibt vertragsspezifisch.

8. Views
   Neue Felder werden direkt in bestehenden `hr_contract`-Formviews über separate Tabs angezeigt:
   * Monetary-Felder gruppiert in einem eigenen Tab.
   * Text-/Condition-Felder gruppiert in einem eigenen Tab.

9. Security
   Vorerst keine neuen Zugriffsregeln; bestehende Rechte von `hr.contract` werden geerbt.

10. Migration
    Keine zusätzliche Migrationsstrategie nur für Feldumbenennung notwendig, da das Add-on neu ist und direkt mit korrekter Benennung startet.