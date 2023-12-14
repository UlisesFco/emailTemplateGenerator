# emailTemplateGenerator
App que genera un formato de correos en un archivo HTML (msg.html)
y una versión en texto simple que se copia al portapapeles.

Se pueden guardar direcciones de destino en el archivo appAdd.csv, el cual
se crea automáticamente al correr la aplicación por primera vez.

Si hay multiples encargos (appointments), los datos se separan con comas.
Como en la siguiente imagen:
![imagen](https://github.com/UlisesFco/emailTemplateGenerator/assets/23128764/7fc738ff-0a15-44fa-bb00-deef086722d9)

El texto sin formato tendría una apariencia como la siguiente

```
Delivery Order: 123456789

Pickup address: 1420 N RENAISSANCE BLVD NE ALBUQUERQUE NM 87107 USA
Details: COSTCO, 456-784-9634


-------------------------------------------------------
Pickup Appointment: 12-23-2023 05:00 am
Carrier: Carrier
Driver: NAME SURNAME, Phone: 456-785-9641
Rate: 2500
Notes: notes
-------------------------------------------------------

=======================================================
Appointment: 12-30-2023 01:00 am
Number:123
SO:7899, PO:456

-------------------------------------------------------
SAMS CLUB

300 ENTERPRISE RD JOHNSTOWN NY 12095 USA
=======================================================
=======================================================
Appointment: 12-31-23 09:am
Number:458
SO:6352, PO:785

-------------------------------------------------------
TARGET

2300 W BEN WHITE BLVD AUSTIN TX 78704 USA
=======================================================
<>

Lbs: 78
Qty: 500
Temp: 75 °F
Palets: 12
```
En msg.html se muestra un ejemplo con formato que se puede copiar
a su servicio de correo electrónico preferido. Un ejemplo a continuación:
![imagen](https://github.com/UlisesFco/emailTemplateGenerator/assets/23128764/23bbc18e-a1ac-4fe1-a1f8-866d30f5bf21)


