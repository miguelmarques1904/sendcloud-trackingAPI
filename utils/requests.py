import requests

api_endpoint = "http://localhost:5000/email"


ticket_list = [
  {
    "id": 1,
    "created_at": "2021-06-14T08:53:30Z",
    "subject": "Berichtgeving Support Case: 99999",
    "body": "Beste klant,\n\n\nBedankt voor uw bericht over pakketnummer: 05222885917440.\n\n\nIk heb uw bericht doorgestuurd naar het juiste depot en verwacht u binnen 2 dagen een terugkoppeling te geven.\n\nAlvast bedankt voor uw geduld en een fijne dag toegewenst!\n\n\nMet vriendelijke groet,\n"
  },
  {
    "id": 2,
    "created_at": "2021-06-14T05:33:54Z",
    "subject": "DPD Paketklärungsinformation zu: 06215115546675",
    "body": "Guten Morgen DPD-Team,\n\nwir hatten wiederholende Anfragen zu Paketklärungen zu den Sendungsnummern: 06215115546675\nWir haben Sie schriftlich (Ticket #) und auch telefonisch darüber informiert, dass die Empfängeradresse schon mehrfach angefahren wurde und auch die restlichen Details haben wir Ihnen schon weitergeleitet. Die angegebene Adresse ist korrekt!\n\nNun haben wir einen sehr verärgerten Kunden, da die Lieferung bis Freitag, 18 Uhr hätte stattfinden sollen und es bisher drei missglückte Zustellversuche gab.\nWir würden Sie bitten, den Fahrer doch bitte genau zu informieren, dass an der schon von Anfang an angegebenen Adresse immer jemand bis 18 Uhr da ist.\n\n\nEbenso hat er uns eine Telefonnummer des Empfängers hinterlassen:\n\n> Empfänger auch gerne telefonisch kontaktieren.\n>\n> Hier nochmal die Telefonnummer: +\n\nEbenso den Vermerk:\n\n> Der Kunde (Empfänger) ist im Sprachstudio (kein Nachbarhaus notwendig). Zur Not darf der Wein auch im Sprachstudio abgestellt werden.\n>\n> Kundin sitzt den ganzen im Haus!! (Auch zur Mittagspause ist die Tür zum öffnen!  Sie wartet immer noch… Es war ganzen Tag kein Zustellversuch! Ich glaube der Fahrer ist ein Betrüger…\n\n\nWir bitten Sie daher um einen erneuten Zustellversuch beim Kunden, mit der Bitte den Fahrer ganz genau zu briefen.\n\nVielen Dank im Voraus.",
    "status": "open"
  },
  {
    "id": 3,
    "created_at": "2021-06-14T07:23:32Z",
    "subject": "Beschwerde Paket nicht zugestellt obwohl Adresse korrekt ist 094467...",
    "body": "Sehr geehrte Damen und Herren,\r\n\r\nvielen Dank für Ihre E-Mail zur Sendung 09446786365989.\r\n\r\nNach  Einsicht und Prüfung der zuständigen Kollegen sehen wir  von einer Gutschrift ab. \r\n\r\nDas Zustellhindernis wurde zur Bearbeitung in MYDPD freigegeben, allerdings nicht bearbeitet.\r\n\r\nViele Grüße"
  },
  {
    "id": 4,
    "created_at": "2021-06-14T09:59:10Z",
    "subject": "Support JVGL0613644400017892",
    "body": "Hi Sendcloud,\n\nBedankt voor je bericht.\n\nIk zie dat de mail van 02/06 niet bij ons binnengekomen is. Hoe dit kan, weet ik helaas niet.\n\nDe zending gaat binnen 2 werkdagen aangeboden worden op het adres in je bericht.\n\nMocht je verdere vragen hebben, verneem ik dit graag.\n\nMijn excuses voor het ongemak.\n\nMet vriendelijke groet / Kind regards,"
  },
  {
    "id": 5,
    "created_at": "2021-06-14T09:59:10Z",
    "subject": "JVGL0599564200004620-  Bedankt voor je bericht...",
    "body": "Hoi Sendcloud,\n\n\n\nBedankt voor je bericht.\n\n\n\nDeze zending stond op het depot in Duitsland om afgehaald te worden door de ontvanger. Tijdens de bezorgpoging was er namelijk niemand aanwezig.\n\n\n\nEchter is de zending gisteren, 09-06, geretourneerd, omdat de zending niet binnen de aangegeven tijd was opgehaald. Je kunt de zending JVGL0599564200004620 spoedig retour verwachten.\n\n\n\nIndien er nog vragen zijn, hoor ik het graag.\n\n\n\n \nMet vriendelijke groet / Kind regards,\n\n"
  },
  {
    "id": 6,
    "created_at": "2021-06-14T09:59:10Z",
    "subject": "DHL Vraag",
    "body": "Hi Sendcloud,\n\n\n\nDank voor je bericht.\n\n\n\nDe zending JVGL06062129045490459072 wordt binnen 2 werkdagen aangeboden op huisnummer 21.\n\n\n\nMocht je nog vragen hebben verneem ik dat graag.\n\n\n\nMet vriendelijke groet / Kind regards,\n\n\n\n"
  },
  {
    "id": 7,
    "created_at": "2021-06-15T01:19:19Z",
    "subject": "Vertraagd: PostNL Service",
    "body": "Beste Sendcloud Team, \n\n We hebben uw bericht in goede orde ontvangen. Het is natuurlijk erg vervelend dat de zending 3STXYC1996186 retour is gestuurd. Echter mocht dit niet het geval zijn geweest dan hadden we ook geen herstelactie uit mogen zetten. We mogen geen volledig adres aanpassen. Dus wanneer de zending naar een alternatief adres moet, is dit niet mogelijk. \n\n Heeft u nog vragen? \n\n Neem dan contact op met uw Service Team op telefoonnummer 088-2255682. We zijn bereikbaar op maandag tot en met vrijdag van 08:00 tot 19:00 uur en op zaterdag van 09:00 tot 17:00 uur. U kunt ook contact opnemen door deze e-mail te beantwoorden. \n\n Met vriendelijke groet, \n\n"
  },
  {
    "id": 8,
    "created_at": "2021-06-15T03:22:43Z",
    "subject": "Retoure: PostNL Service",
    "body": "&nbsp;\n\t\t\n\t\t\n\t\t\t\n\t\t\t\n\t\t\t\t\n\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t Beste Sendcloud, \n\n\t\t\t\t\t\t\t\t\t &nbsp; \n\n\t\t\t\t\t\t\t\t\t Wat vervelend dat de zending retour is gestuurd. Ik heb voor u een onderzoek geopend onder casenummer 13927. \n\n\t\t\t\t\t\t\t\t\t &nbsp; \n\n\t\t\t\t\t\t\t\t\t Zodra ik meer informatie heb, neem ik contact met u op. \n\n\t\t\t\t\t\t\t\t\t &nbsp; \n\n\t\t\t\t\t\t\t\t\t Gegevens van uw zending: \n\n\t\t\t\t\t\t\t\t\t &nbsp; \n\n\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t\t Verzenddatum: \n\t\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t\t 9 juni 2021 \n\t\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t\t Barcode: \n\t\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t\t 3STXWW1346350 \n\t\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t\t Geadresseerde: \n\t\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t\t &nbsp; \n\t\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t\t Nederland \n\t\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\n\n\t\t\t\t\t\t\t\t\t &nbsp; \n\n\t\t\t\t\t\t\t\t\t Heeft u nog vragen? \n\n\t\t\t\t\t\t\t\t\t &nbsp; \n\n\t\t\t\t\t\t\t\t\t Neem dan contact op met uw Service Team op&nbsp;telefoonnummer 088-2255682. We zijn bereikbaar op&nbsp;maandag tot en met vrijdag van 08:00 tot 19:00 uur en op zaterdag van 09:00 tot 17:00 uur. U kunt ook contact opnemen door deze e-mail te beantwoorden.&nbsp; \n\n\t\t\t\t\t\t\t\t\t &nbsp; \n\n\t\t\t\t\t\t\t\t\t Met vriendelijke groet,&nbsp;\n\n\t\t\t\t\t\t\t\t\t\n\n\t\t\t\t\t\t\t\t\tMarieke Piek\n\n\t\t\t\t\t\t\t\t\tServiceteam Amber&nbsp; \n\n\t\t\t\t\t\t\t\t\t PostNL Pakketten Benelux B.V. \n\n\t\t\t\t\t\t\t\t\t &nbsp; \n\n\t\t\t\t\t\t\t\t\t &nbsp; \n\n\t\t\t\t\t\t\t\t\t Als zakelijke klant van PostNL kunt u gebruik maken van de zakelijke track &amp; trace-module in Mijn PostNL. Hier vindt u meer informatie over uw zendingen, zodat u uw klanten sneller en beter kunt helpen. Zet zakelijke track &amp; trace eenvoudig aan: Ga naar postnl.nl/meerinzicht voor meer informatie. \n\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\t&nbsp;\n\t\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t Serviceteam Amber&nbsp; \n\n\t\t\t\t\t\t\t\t\t Postbus 99180\n\n\t\t\t\t\t\t\t\t\tLeeuwarden 8900 NA \n\n\t\t\t\t\t\t\t\t\t &nbsp;\n\t\t\t\t\t\t\t\t\t &nbsp; \n\n\t\t\t\t\t\t\t\t\t &nbsp; \n\n\t\t\t\t\t\t\t\t\t www.postnl.nl \n\t\t\t\t\t\t\t\t\t \n\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\n\t\t\t\t\n\t\t\t\n\t\t\t\n\t\t\n\t\t\n\t\t\t&nbsp;\n\t\t\n\t\t\n\t\t\t\n\t\t\n\t\t\n\t\t\t&nbsp;\n\t\t\n\t\n\n\n \n\n\n--------------- Oorspronkelijk bericht ---------------\n\nVan: Sendcloud Support [contact@sendcloud.sc]\n\nVerzonden: 11-6-2021 14:37\n\nAan: serviceteamamber@postnl.nl\n\nOnderwerp: [Sendcloud] 3STXWW1346350\n\n\n\n\n\n\n\n\nref:_00Dw0CncL._5006M1pqDJg:ref"
  },
  {
    "id": 9,
    "created_at": "2021-06-15T03:22:43Z",
    "subject": "3SNZYV5258200",
    "body": "Beste Sendcloud Team, \n\n Ik hou jullie op de hoogte. Inderdaad leuk je een keer gesproken te hebben. Fijne dag en werkse. \n\n Heeft u nog vragen? \n\n Neem dan contact op met uw Service Team op telefoonnummer 088-225. We zijn bereikbaar op maandag tot en met vrijdag van 08:00 tot 19:00 uur en op zaterdag van 09:00 tot 17:00 uur. U kunt ook contact opnemen door deze e-mail te beantwoorden. \n\n Met vriendelijke groet, \n\nServiceteam Amber\n\nPostNL Pakketten Benelux B.V."
  }
]


for ticket in ticket_list:
  r = requests.post(url = api_endpoint, json = ticket)
  print("Response:", r.json())
  print("Status Code:", r.status_code)
  print("Time Taken:", str(r.elapsed.total_seconds()) + "s")
