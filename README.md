# Dobot Controller

Basisproject om de Dobot Magician aan te sturen met Python. Je leert hoe je via code de robotarm kunt laten bewegen, objecten kunt oppakken en weer neerzetten.

## Vereisten

- Python 3.12
- Dobot Magician aangesloten via USB
- Windows (COM-poort)

## Installatie

1. Clone de repository:
```bash
git clone git@github.com:RTMA/dobotController.git
cd dobotController
```

2. Maak een virtuele omgeving aan en activeer deze:
```bash
python -m venv venv
venv\Scripts\activate
```

3. Installeer de benodigde packages:
```bash
pip install -r requirements.txt
```

## COM-poort instellen

De scripts gebruiken standaard `COM13`. Check in Apparaatbeheer (Device Manager) welke COM-poort jouw Dobot gebruikt en pas dit aan in het script als dat afwijkt:

```python
port = "COM13"  # Pas aan naar jouw COM-poort
```

## Bestanden

| Bestand | Omschrijving |
|---|---|
| `dobot_control.py` | Hoofdscript: homing, naar positie bewegen, oppakken en plaatsen van een object met de gripper |
| `pose_dobot.py` | Leest de huidige positie (x, y, z) van de Dobot uit en print deze |
| `serial_test.py` | Test of de seriële verbinding met de Dobot werkt |
| `requirements.txt` | Lijst met Python packages |

## Gebruik

Zorg dat de Dobot is aangesloten en de juiste COM-poort is ingesteld.

```bash
python dobot_control.py
```

Het script doorloopt de volgende stappen:
1. Verbinding maken met de Dobot
2. Homing uitvoeren (nulpositie bepalen)
3. Naar de oppakpositie bewegen
4. Object oppakken met de gripper
5. Naar de plaatspositie bewegen
6. Object neerzetten

Wil je eerst alleen de huidige positie uitlezen:
```bash
python pose_dobot.py
```

## Posities aanpassen

In `dobot_control.py` kun je de x, y, z en r waarden aanpassen in de functies `positie_een()` en `positie_twee()`. Gebruik `pose_dobot.py` om de huidige positie uit te lezen en als startpunt te gebruiken.