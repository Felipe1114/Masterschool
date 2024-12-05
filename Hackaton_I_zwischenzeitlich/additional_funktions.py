import random as r

def main():
    """testing the funktion "remove_used_url"
    """
    #test für url enetferunung
    """urls = [
        "https://example.com",
        "https://bit.ly",
        "https://tinyurl.com",
        "https://goo.gl",
        "https://t.co",
        "https://ow.ly",
        "https://buff.ly",
        "https://is.gd",
        "https://v.gd",
        "https://shrtco.de"
    ]
    global used_urls
    used_urls = {}
    length = len(urls)
    i = r.randrange(len(urls))
    runde = 0
    print(i)
    while length > 0:
        try:
            runde += 1
            i = r.randrange(len(urls))
            print(f"list bevor reome: {urls}")
            url = urls[i]
            print(remove_used_url(runde, urls, url))
        except ValueError:
            exit()"""

    #testing für dict erstellung
    liste_2 = [
        [1, 34, 22, 343, "url1"],
        [2, 45, 52, 452, "url2"],
        [3, 55, 11, 5511, "url3"]
    ]
    global all_results
    all_results = {}
    for liste in liste_2:
        runde, entferung, zeit, punkte, url = liste
        all_results = get_all_informations(liste)
    print(all_results)


def remove_used_url(count_round:int=0, url_list:list=None, used_url:str=None):
    """get list of urls(url_list) and an url(used_url) as argument.
    removes the url from the list and saves the removed url dict with key(round(int)) and val(current url)
    also gives back the current round

    Args:
        url_list(list): list of all possible landmarks
        used_url(str): the current used url
        count_round(int): counts the rounds played

    """
    index_of_removed_url = url_list.index(used_url)
    url = url_list.pop(index_of_removed_url)
    print(f"list after reove: {url_list}")

    if url not in url_list:
        used_urls[count_round] = url
    return used_urls


def get_all_informations(lst) -> dict:
    round, distance, time, points, url = lst
    if all_results["distance"][round] not in all_results:
        all_results["distance"][round] = distance
    else:
        all_results["distance"][round] = distance
    if all_results["time"][round] not in all_results:
        all_results["time"][round] = time
    else:
        all_results["time"][round] = time
    if all_results["points"][round] not in all_results:
        all_results["points"][round] = points
    else:
        all_results["points"][round] = points
    if all_results["url"][round] not in all_results:
        all_results["url"][round] = url
    else:
        all_results["url"][round] = url

    return all_results




if __name__ == "__main__":
    main()