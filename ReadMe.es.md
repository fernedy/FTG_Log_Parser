<div align="center">

[🇬🇧 English](ReadMe.md) · [🇪🇸 Español](ReadMe.es.md)

</div>

<div align="center">

# 🛡️ FTG Log Parser

**Logs del firewall FortiGate → CSV limpio, en segundos.**

![Python](https://img.shields.io/badge/python-3.6%2B-blue?style=flat-square&logo=python&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-yellow?style=flat-square)
![Use case](https://img.shields.io/badge/use--case-Network_Security-00A884?style=flat-square)

</div>

---

Los equipos de red ahogados en logs de FortiGate necesitan respuestas, no texto crudo. **FTG Log Parser** convierte archivos de log de FortiGate en CSV estructurado para abrirlos en Excel, cargarlos en un SIEM o analizarlos con pandas.

## ⚡ Inicio rápido

```bash
git clone https://github.com/fernedy/FTG_Log_Parser.git
cd FTG_Log_Parser
python main.py
```

1. Copia tu archivo de log a la carpeta `Log/`.
2. Ejecuta `python main.py` e ingresa el nombre del archivo.
3. Obtén tu CSV. Listo.

## 📸 Capturas

| Aplicación | CSV resultante |
|---|---|
| ![App view](./Screenshoot/ScreenNo1.png) | ![CSV result](./Screenshoot/ScreenNo2.png) |

## 🗂️ Estructura del proyecto

```text
├── main.py         # Punto de entrada CLI
├── Log2CSV.py      # Parser: registros FortiGate → CSV
├── ColorText.py    # Salida en color en consola
└── Log/            # Coloca aquí tus archivos .log
```

## 📚 Referencias

- [Logs de ejemplo oficiales de Fortinet](https://docs.fortinet.com/document/fortigate/6.2.15/cookbook/986892/sample-logs-by-log-type)

## 🤝 Contribuir

PRs bienvenidos — las reglas de parsing para nuevos tipos de log de FortiGate son la contribución más útil.

## 📜 Licencia

MIT — ver [LICENSE](LICENSE).

---

<div align="center">

Construido por [Fernedy Arias](https://github.com/fernedy) · AI First · Tech Explorer

</div>
