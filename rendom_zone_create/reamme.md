# YAML  Generator Tool 🛠️

This is a simple Python script built with Tkinter that generates sample YAML blocks for testing purposes. Each block contains randomized device names, MAC-like addresses, and zone definitions — useful for prototyping or populating test data in YAML format.

## 🔧 Features

- Generates random device entries with:
  - Unique device names (e.g., `Device A`, `Device B`)
  - Unique MAC address suffixes (e.g., `AA:BB:CC:DD:EE:01`)
  - Random zone areas
- Ensures no duplicate last digits between MAC address and zone IDs
- GUI-based tool using `tkinter`
- "Generate YAML" button regenerates a new set
- "Copy to Clipboard" button to easily copy generated YAML
- Displays the number of YAML blocks generated



