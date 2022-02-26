# ARMACHAT CircuitPython
New ARMACHAT based on CircuitPython

**Supported Models**
- ARMACHAT Compact

**Upcoming Models**
- ARMACHAT Watch

**Working Features**
- Send message with header and store to memory
- Receive message and parse header, store to memory
- Display message memory with message details like SNR and RSSI
- Count messages in memory by type
- Hardware details like free memory and power supply voltage
- Terminal display with messages from background systems
- AES256 encryption
- Message confirmation and status change in memory
- Boot safe mode


**TODO**
- Better LoRa Libray
  - CAD
  - Status Detection
  - Interrupts
- Contact List
- Setup and Save Configuration
- Save Messages

**Development**
To install the required dependencies, run the following command to install
Pipenv and then install the dependencies:
```shell
pip install --user pipenv
pipenv install --dev
```
