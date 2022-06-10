from xsd_validator import XsdValidator

validator = XsdValidator('UBL/maindoc/UBL-invoice-2.1.xsd')
validator.assert_valid('UBL/Examples/MainExample.xml')