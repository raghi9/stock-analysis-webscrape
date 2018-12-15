

# returns wrong xpath bcz of weird <div>s just after <body>.
# page source in file test_output. search siblings and then the text starting with <body>
# compare this with page source in webpage using inspect_element.
# find a way so elements can be highlighted correctly
# ############################################################################
# body/div[4] is the problem, change it to body/div[2]
# ############################################################################
 
def xpath_from_soup(element):
    # return "/html/body/div[2]/div[3]/div[2]/div[3]/div[2]/div[2]/div[2]/div/table[2]/tbody/tr[8]/td[2]"
    """
    Generate xpath of soup element
    :param element: bs4 text or node
    :return: xpath as string
    """
    components = []
    child = element if element.name else element.parent
    for parent in child.parents:
        """
        @type parent: bs4.element.Tag
        """
        siblings = parent.find_all(child.name, recursive=False)
        # print("siblings list : \n")
        # for s in siblings:
        #     print(s)
        # print("child element : \n")
        # print(child)
        components.append(
            child.name
            if siblings == child or siblings.index(child) == 0
            else
                '%s[%d]' % (child.name, 1 + siblings.index(child))
            )
        child = parent
    components.reverse()
    xpath_string = '/%s' % '/'.join(components)
    return xpath_string.replace("[4]","[2]",1)
