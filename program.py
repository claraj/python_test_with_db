from models import Flower 


def add_flower(flower_name):
    """ Save flower to DB. 
    Return flower object if saved, return None if duplicate """

    flower = Flower(name=flower_name)
    try:
        flower.save()
        return flower
    except Exception as e:
        print(e)
        return None 


def main():
    Flower.delete().execute()
    rose = add_flower('Rose')
    poppy = add_flower('Poppy')
    poppy2 = add_flower('Poppy')
    print(rose, poppy, poppy2)  # Rose Poppy None 


if __name__ == '__main__':
    main()