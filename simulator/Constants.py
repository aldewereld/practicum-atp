
"""Constants for physical simulation"""
flowRate = 1            # the amount of water flowing (in ml) from the mixture vessel per second when tap is open
heatRate = 1            # the amount of heat increase (in degrees celsius) in mixture vessel when heater is on
temperatureDecay = 0.1    # amount of temperature loss (in degrees celsius) in mixture vessel when heater is off

pressureRampUp = 3      # amount of seconds to build up enough pressure to make liquid flow from storage vessels
pressureRampDown = 20   # amount of time before liquid stops flowing after the air pump has been switched off

liquidMax = 2000        # amount (in ml) of liquid that can maximally go into the containers (pi * 10 * 10 * 6.5; diameter 10cm, height ~6.5cm)
environmentTemp = 20    # environmentalTemperature

tempConversion = 0.05   # 0.00V = 0.0 degrees celsius; steps of 0.05V per degree celsius above 0
levelConversion = 0.5       # V/cm; 0V is empty
colourConversion = 0.033 # 0.00V = value 0 (pitch black) - 3.3 V = value 100 (bright white); value/lightness score (HSV)

"""Set Points: these indicate the desired values for the dimensions of the resulting mixture"""
levelSetPoint = 1.6 # cm liquid (0.8 = 500ml)
colourSetPoint = 1.65 # % value
tempSetPoint = 2.0 # degrees celsius

"""Reaction difference: the amount of points of divergence allowed before the controller reacts"""
tempReaction = 0.05
levelReaction = 0.07
colourReaction = 0.05