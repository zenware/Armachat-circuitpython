# Models
As a Doomsday Communicator, the ARMACHAT software should be designed to run on
various platforms and models. Some ambitious users may extend the ARMACHAT
project with new schematics and designs based on CircuitPython-capable chips. To
give these users the best chance of success, the ARMACHAT software should use an
extensible "Model" schema that defines the available hardware and its pins.

As a start, the following model attributes should be defined:
* LoRa Module Pins
* Display Type and Pins
* Keyboard Mapping and Backlight Pins
* Speaker Pins

The Model schema should be used for the following:
**Boot Process** - Initialize the hardware based on pin definitions. Enable or
disable ARMACHAT features based on available hardware.
**Hardware Information Screen** - Model and hardware information as well as
supported features.  
**Bytecode Compilation** - Only compiles the code that's needed for the model.
CircuitPython based devices are limited in both RAM and Flash, so the footprint
needs to be as small as possible.
