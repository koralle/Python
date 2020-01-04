Lipps = ['Kanade', 'Mika', 'Shiki', 'Frederica', 'Shuko']

class Not346IdolError(Exception):
    pass

def LippsList(name:str):
    """
    例外処理の練習
    """

    try:
        if name == 'Tsubasa':
            raise Not346IdolError(name)
        elif type(name) != str:
            raise TypeError(name)
        else:
            pos = Lipps.index(name)
            print(Lipps[pos])
    except Not346IdolError as e:
        print(name + ": She is not 346 idol.")
    # except IndexError as e:
        # print("NG: {}".format(e))
    except NameError as e:
        print("NG: {}".format(e))
    except TypeError as e:
        print("NG: {}".format(e))
    except ValueError as e:
        print("NG: {}".format(e))
    else:
        print("Lipps Saiko!")
    finally:
        print("Tulip.")
        return False


def main():
    # -------------------------------
    LippsList('Mika')
    # -------------------------------

    # きっとValueErrorをcatchするはず。
    LippsList('Mio')
    # -------------------------------

    # きっとTypeErrorをcatchするはず。
    LippsList(346)
    # -------------------------------

    # きっとNot346IdolErrorをcatchするはず。
    LippsList('Tsubasa')
    # -------------------------------

    LippsList('Kanade')



if __name__ == "__main__":
    main()