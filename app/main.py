def determine_entity_type(employees, revenue, sector):
    high_criticality_sectors = [
        "Energie", "Verkehr", "Bankwesen", "Finanzmarktinfrastrukturen", "Gesundheitswesen",
        "Trinkwasser", "Abwasser", "Verwaltung von IKT-Diensten B2B", "öffentliche Verwaltung",
        "Weltraum", "Digitale Infrastruktur"
    ]
    other_critical_sectors = [
        "Post- und Kurierdienste", "Abfallbewirtschaftung", "Chemie", "Lebensmittel",
        "Verarbeitendes/herstellendes Gewerbe", "Anbieter digitaler Dienste", "Forschung"
    ]

    if employees <= 50 and revenue <= 10:
        company_size = "Kleines Unternehmen"
    elif employees < 250 and revenue <= 50:
        company_size = "Mittleres Unternehmen"
    elif employees >= 250 or revenue > 50:
        company_size = "Großes Unternehmen"
    else:
        company_size = "Unbekannt"

    if sector in high_criticality_sectors:
        if company_size in ["Mittleres Unternehmen", "Großes Unternehmen"]:
            entity_type = "Wesentliche Einrichtung"
        else:
            entity_type = "Nicht betroffen"
    elif sector in other_critical_sectors:
        if company_size in ["Mittleres Unternehmen", "Großes Unternehmen"]:
            entity_type = "Wichtige Einrichtung"
        else:
            entity_type = "Nicht betroffen"
    else:
        entity_type = "Nicht betroffen"

    return entity_type, company_size

def main():
    print("\n\n\n*** NISG2024 (Entwurf) Checker ***")
    print("Dieses Programm überprüft, ob Ihr Unternehmen von der NIS2-Richtlinie betroffen ist")
    print("und zeigt die entsprechenden Pflichten und Risikomanagementmaßnahmen\n")

    sectors = [
        "Energie", "Verkehr", "Bankwesen", "Finanzmarktinfrastrukturen", "Gesundheitswesen",
        "Trinkwasser", "Abwasser", "Verwaltung von IKT-Diensten B2B", "öffentliche Verwaltung",
        "Weltraum", "Digitale Infrastruktur",
        "Post- und Kurierdienste", "Abfallbewirtschaftung", "Chemie", "Lebensmittel",
        "Verarbeitendes/herstellendes Gewerbe", "Anbieter digitaler Dienste", "Forschung"
    ]

    print("\nBitte wählen Sie einen Sektor aus der folgenden Liste aus:")
    for i, sector in enumerate(sectors, start=1):
        print(f"{i}. {sector}")

    sector_index = int(input("\nGeben Sie die Nummer des gewählten Sektors ein: "))
    selected_sector = sectors[sector_index - 1]

    company = str(input("Name des Unternehmens: "))
    employees = int(input("Anzahl der Mitarbeiter: "))
    revenue = float(input("Jahresumsatz in Millionen Euro: "))

    entity_type, company_size = determine_entity_type(employees, revenue, selected_sector)

    print("\n---------------------------------------")
    print("            Ergebnisse")
    print("---------------------------------------")
    print(f"Unternehmen: {company}")
    print(f"Sektor: {selected_sector}")
    print(f"Unternehmensgröße: {company_size}")
    print(f"Einrichtungsart: {entity_type}")

    if entity_type == "Wesentliche Einrichtung" or entity_type == "Wichtige Einrichtung":
        print("\nPflichten für wesentliche und wichtige Einrichtungen:")
        print("§29 Registrierungspflicht")
        print("§31 Verantwortung der Leitungsorgane für die Einhaltung der Risikomanagementmaßnahmen")
        print("    Teilnahme an Cybersicherheitsschulungen")
        print("§32 Implementierung technischer, operativer und organisatorischer Maßnahmen zur Beherrschung der Risiken")
        print("§33 Nachweis über die Wirksamkeit der Risikomaßnahmen")
        print("§34 Verpflichtung zur Meldung erheblicher Cybersicherheitsvorfälle und regelmäßige Berichterstattung über die umgesetzten Sicherheitsmaßnahmen")
        print("§35 Beurteilung erheblicher Cybersicherheitsvorfall")
        print("§42 Definition der Arten personenbezogener Daten, die bei Sicherheitsvorfällen gemeldet werden müssen")
        
        print("\nErfüllung von 10 Risikomanagementmaßnahmen gemäß Artikel 21 der NIS2-Richtlinie:")
        print("1. Risikoanalyse und Sicherheitskonzepte für Informationssysteme")
        print("2. Bewältigung von Sicherheitsvorfällen")
        print("3. Aufrechterhaltung des Betriebs (Backup-Management und Wiederherstellung nach einem Notfall, Krisenmanagement)")
        print("4. Sicherheit der Lieferkette")
        print("5. Sicherheitsmaßnahmen bei Erwerb, Entwicklung und Wartung von Netz- und Informationssystemen")
        print("6. Bewertung der Wirksamkeit von Risikomanagementmaßnahmen")
        print("7. Cyberhygiene und Schulungen im Bereich Cybersicherheit")
        print("8. Einsatz von Kryptografie und Verschlüsselung")
        print("9. Sicherheit des Personals, Zugriffskontrollen, Management von Anlagen")
        print("10. Multi-Faktor-Authentifizierung und gesicherte Kommunikation")
        print("\nWeitere Informationen finden Sie im Anlage 3 zu NISG 2024 Entwurf")
    else:
        print("\nIhr Unternehmen ist nicht von der NIS2-Richtlinie betroffen.")
    
    print("\nDisclaimer: Bitte beachten Sie, dass diese Information keine Rechtsberatung zur NIS2 darstellt.")
    print("            Für rechtliche Beratung wenden Sie sich bitte an Ihren Rechtsberater")
    print("            oder Ihre Wirtschaftsvertretung, beispielsweise die WKÖ.\n")

if __name__ == "__main__":
    main()
