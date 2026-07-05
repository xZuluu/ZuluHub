<div align="center">

![](https://capsule-render.vercel.app/api?type=rect&color=0:141E30,100:243B55&height=130&section=header&text=%E2%97%A2%E2%97%A4%20%20ZULU%20HUB%20%20%E2%97%A2%E2%97%A4&fontSize=38&fontColor=ffffff&fontAlignY=56)

`Email Tooling`&nbsp;&nbsp;·&nbsp;&nbsp;`Search`&nbsp;&nbsp;·&nbsp;&nbsp;`Automation`&nbsp;&nbsp;·&nbsp;&nbsp;`Desktop`

[![Status](https://img.shields.io/badge/STATUS-AKTIV-1ed760?style=for-the-badge&labelColor=0D1117)](.)
&nbsp;
[![Electron](https://img.shields.io/badge/Electron-21262D?style=for-the-badge&logo=electron&logoColor=white&labelColor=0D1117)](.)
&nbsp;
[![Python](https://img.shields.io/badge/Python-21262D?style=for-the-badge&logo=python&logoColor=white&labelColor=0D1117)](.)
&nbsp;
[![Node.js](https://img.shields.io/badge/Node.js-21262D?style=for-the-badge&logo=nodedotjs&logoColor=white&labelColor=0D1117)](.)
&nbsp;
[![SQLite](https://img.shields.io/badge/SQLite-21262D?style=for-the-badge&logo=sqlite&logoColor=white&labelColor=0D1117)](.)

</div>

<div align="center">

**Ein schlankes Desktop-Toolkit: E-Mail-Adressen erzeugen und bereinigen, plus eine kriterienbasierte Suche — unter einer Hülle.**

</div>

<br>

### &nbsp;◇&nbsp;&nbsp;Überblick

ZuluHub bündelt drei Werkzeuge in einer schlanken Desktop-Oberfläche: einen **Generator** und einen
**Cleaner** für E-Mail-Adressen sowie **Seeker**, eine kriterienbasierte Suche. Eine Shell, ein
lokaler Datastore, ein Interface. Enterprise-Look, flach, high-contrast, dark-only.

### &nbsp;◇&nbsp;&nbsp;Module

| Modul | Rolle |
|-------|-------|
| **Email Generator** | E-Mail-Adressen generieren und lokal verwalten |
| **Email Cleaner** | Listen validieren, deduplizieren, tote Adressen entfernen |
| **Seeker** | Kriterienbasierte Suche — Datensätze auffinden, prüfen, anreichern |

### &nbsp;◇&nbsp;&nbsp;Stack

<div align="center">

`Electron` · `Node.js` · `Python` · `SQLite` · `Vanilla JS UI`

</div>

### &nbsp;◇&nbsp;&nbsp;Architektur

Eine Electron-Shell orchestriert Python-Worker. Die Worker streamen strukturierte NDJSON-Events auf
stdout, die Shell rendert sie live (Progress · Results · Logs). Die Module teilen sich lokal einen
SQLite-Datastore. Zugang läuft über eine getrennte, aktivierungsbasierte Lizenz-Schicht.

### &nbsp;◇&nbsp;&nbsp;Setup

```bash
npm install
pip install -r requirements.txt
npm start
```

Konfiguration über `config.json` (Vorlage: `config.example.json`).

---

<div align="center">

© 2026 Zulu · Proprietär — alle Rechte vorbehalten.

</div>
