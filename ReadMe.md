<div align="center">

# 🛡️ FTG Log Parser

**FortiGate firewall logs → clean CSV, in seconds.**
*Logs del firewall FortiGate → CSV limpio, en segundos.*

![Python](https://img.shields.io/badge/python-3.6%2B-blue?style=flat-square&logo=python&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-yellow?style=flat-square)
![Use case](https://img.shields.io/badge/use--case-Network_Security-00A884?style=flat-square)

</div>

---

Network teams drowning in FortiGate logs need answers, not raw text. **FTG Log Parser** converts FortiGate log files into structured CSV so you can open them in Excel, load them into a SIEM, or feed them to pandas for analysis.

Los equipos de red ahogados en logs de FortiGate necesitan respuestas, no texto crudo. **FTG Log Parser** convierte archivos de log de FortiGate en CSV estructurado para abrirlos en Excel, cargarlos en un SIEM o analizarlos con pandas.

## ⚡ Quickstart / Inicio rápido

```bash
git clone https://github.com/fernedy/FTG_Log_Parser.git
cd FTG_Log_Parser
python main.py
```

1. Drop your log file into the `Log/` folder.
   *Copia tu archivo de log a la carpeta `Log/`.*
2. Run `python main.py` and type the file name.
   *Ejecuta `python main.py` e ingresa el nombre del archivo.*
3. Get your CSV. Done.
   *Obtén tu CSV. Listo.*

## 📸 Screenshots / Capturas

| Application | Resulting CSV |
|---|---|
| ![App view](./Screenshoot/ScreenNo1.png) | ![CSV result](./Screenshoot/ScreenNo2.png) |

## 🗂️ Project structure / Estructura

```text
├── main.py         # CLI entry point / punto de entrada
├── Log2CSV.py      # Parser: FortiGate records → CSV / registros → CSV
├── ColorText.py    # Colored console output / salida en color
└── Log/            # Drop your .log files here / coloca aquí tus logs
```

## 📚 References / Referencias

- [Fortinet official sample logs / logs de ejemplo oficiales](https://docs.fortinet.com/document/fortigate/6.2.15/cookbook/986892/sample-logs-by-log-type)

## 🤝 Contributing / Contribuir

PRs welcome — parsing rules for new FortiGate log types are the most useful contribution.

## 📜 License / Licencia

MIT — see [LICENSE](LICENSE).

---

<div align="center">

Built by [Fernedy Arias](https://github.com/fernedy) · AI First · Tech Explorer

</div>
