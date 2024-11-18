from os import remove


def main():
    """testing the funktion "remove_used_url"

    """
    list = ["test1", "test2", "test3"]
    url = "test2"
    global used_urls
    used_urls = {}
    print(remove_used_url(0, list, url))




def remove_used_url(num_round:int=0, url_list:list=None, used_url:str=None):
    """get list of url(url_list) and an url(used_url) as arg.
    removes the url from the list and saves the removed url dict with key(round(int)) and val(current url)
    also gives back the current round

    Args:
        url_list(list): list of all possible landmarks
        used_url(str): the current used url
        num_round(int): counts the rounds played

    """
    num_round += 1
    try:
        index_of_removed_url = url_list.index(used_url)
        url = url_list.pop(index_of_removed_url)
        if url not in url_list:
            used_urls[num_round] = url
        return used_urls
    except ValueError:
        exit()






if __name__ == "__main__":
    main()