"""
Chemistry Knowledge Module

Contains basic chemistry concepts
for the UNITER AI Science Tutor.
"""

from __future__ import annotations


CHEMISTRY_KNOWLEDGE = {

    "electrolysis": {
        "topic": "Electrolysis",

        "explanation": (
            "Electrolysis is the chemical decomposition of an "
            "electrolyte by passing an electric current through it."
        ),

        "example": (
            "In copper(II) sulphate solution using copper electrodes, "
            "copper ions move to the cathode and gain electrons."
        ),

        "equations": {
            "cathode": "Cu²⁺ + 2e⁻ → Cu",
            "anode": "Cu → Cu²⁺ + 2e⁻"
        }
    },


    "acid_base": {
        "topic": "Acids and Bases",

        "explanation": (
            "An acid produces hydrogen ions (H⁺) in aqueous solution, "
            "while a base produces hydroxide ions (OH⁻)."
        ),

        "example": (
            "Hydrochloric acid reacts with sodium hydroxide "
            "to produce salt and water."
        ),

        "equation": (
            "HCl + NaOH → NaCl + H₂O"
        )
    },


    "rate_of_reaction": {
        "topic": "Rate of Reaction",

        "explanation": (
            "Rate of reaction is the speed at which reactants "
            "are converted into products."
        ),

        "factors": [
            "Temperature",
            "Concentration",
            "Surface area",
            "Catalyst"
        ]
    }

}


def get_topic(topic: str):
    """
    Retrieve chemistry information.
    """

    return CHEMISTRY_KNOWLEDGE.get(
        topic.lower()
    )