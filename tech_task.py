# -*- encoding: utf-8 -*-
import json
import re


# This function
def splitStreetGermanAddress(address):
    """
    Call "splitStreetWorldAddress" with provided default value for "country".
    To be used when working with german addresses only, when providing address each time is not needed.

    :param address: str - address in format street + house number
    :return: dictionary of street and house number values in a form of json message
    """
    return splitStreetWorldAddress(address, country="Germany")


def splitStreetWorldAddress(address, country):
    """
    This function parses given address based on provided country.
    Supported countries: Germany, USA, Spain, Argentina, France

    :param address: str - address in format street + house number
    :param country: str - country of the address
    :return: dictionary of street and house number values in a form of json message
    """
    addressDictionary = {}
    if country.lower() == "germany":
        regexPattern = "([\x7f-\xff\-A-Za-z ]+)\s+([0-9]+\s{0,1}[A-Za-z]{0,1})"
        # German address contains street first with name with a-z, A-Z, can contain special german letters like umlauts, dash(-), space( ).
        # House number starts with a numeric, can contain letter.
        # Can be divided by space.
        try:
            #try to parse address with regex
            regexSplit = re.split(regexPattern, address)
            addressDictionary.update({
                "street": regexSplit[1],
                "housenumber": regexSplit[2]
            })
        except:
            # raise exception if parsing failed (no matches found)
            raise Exception("Address '" + address + "' is a not valid German address")
    elif country.lower() == "usa":
        regexPattern = "([0-9\-]*)[\W\s+]([a-zA-Z \.]*)"
        # American address contains numeric house number first, it can be complex number like 2-3.
        # Then street address with name with a-z, A-Z, can contain dash(-), space( ).
        # Can be divided by space or comma.
        try:
            addressSplit = re.split(regexPattern, address)
            addressDictionary.update({
                "street": addressSplit[2],
                "housenumber": addressSplit[1]
            })
        except:
            raise Exception("Address '" + address + "' is a not valid American address")
    elif country.lower() == "france":
        regexPattern = "([0-9\-]*)[\W\s]*([\x7f-\xffa-zA-Z \.\-]*)"
        # French address contains numeric house number first, it can be complex number like 2-3.
        # Then street address with name with a-z, A-Z, can contain dash(-), space( ).
        # Can be divided by space or comma.
        try:
            addressSplit = re.split(regexPattern, address)
            addressDictionary.update({
                "street": addressSplit[2],
                "housenumber": addressSplit[1]
            })
        except:
            raise Exception("Address '" + address + "' is a not valid French address")
    elif country.lower() == "spain":
        regexPattern = "([\x7f-\xffa-zA-Z \.\-]*)[\W\s]*([0-9\-]*)"
        # Spanish address contains street address first with name with a-z, A-Z, can contain dash(-), space( ), dot(.).
        # Then numeric house number, it can be complex number like 2-3.
        # Can be divided by space or comma.
        try:
            addressSplit = re.split(regexPattern, address)
            addressDictionary.update({
                "street": addressSplit[1],
                "housenumber": addressSplit[2]
            })
        except:
            raise Exception("Address '" + address + "' is a not valid Spanish address")
    elif country.lower() == "argentina":
        regexPattern = "([a-zA-Z \-\.]*[0-9]*)[\s\W]*(No\s[0-9]*)"
        # Argentina address contains street address first with name with a-z, A-Z, can contain dash(-), space( ), dot(.).
        # Then numeric house number. It should start with "No".
        # Can be divided by space or comma.
        try:
            regexSplit = re.split(regexPattern, address)
            addressDictionary.update({
                "street": regexSplit[1],
                "housenumber": regexSplit[2]
            })
        except:
            raise Exception("Address '" + address + "' is a not valid Argentine address")

    else:
        raise Exception("This country is not supported for address parcing.") # if the country is not one of the list
    assert (addressDictionary["street"] and addressDictionary["housenumber"]), \
        'Parsing error: one of the dict. values is empty.' #asserts that both values return True (not empty)
    return json.dumps(addressDictionary, ensure_ascii=False)
