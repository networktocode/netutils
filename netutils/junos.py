"""Functions for working with junos lists."""


def junos_list(item_list: list):
    """Given a list of items it will output a Junos formatted list.

    Args:
        item_list (list): List of strings.

    Returns:
        str: Sorted string list of items in the junos format.

    Example:
        >>> from netutils.junos import junos_list
        >>> junos_list(["VLAN1", "VLAN2", "VLAN3", "VLAN4"])
        '[ VLAN1 VLAN2 VLAN3 VLAN4 ]'
        >>>
    """

    if isinstance(item_list, list):
        # De-dup list
        clean_item_list = list(dict.fromkeys(item_list))

        # If more than one item format with spaces and square brackets at either end
        if len(clean_item_list) > 1:
            string = ""
            for i in clean_item_list:
                string = string + str(i) + " "
            output = f"[ {string}]"
        else:
            output = clean_item_list[0]
        return output
    else:
        return item_list
