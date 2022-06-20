from xsd_validator import XsdValidator

validator = XsdValidator('Thales_Activation/Thales_Activation.xsd')
validator.assert_valid('Thales_Activation/Examples/ThalesActivation.xml')