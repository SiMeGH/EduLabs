import os
import pickle
from menus import MainMenu
from bus_company import BusCompany


if __name__ == '__main__':
    if not os.path.exists('bus_company.pickle'):
        bus_company = BusCompany("Best Bus Ever")
    else:
        with open('bus_company.pickle', 'rb') as fh:
            bus_company = pickle.load(fh)

    main_menu: MainMenu = MainMenu(bus_company)
    main_menu.run()

    with open('bus_company.pickle', 'wb') as fh:
        pickle.dump(bus_company, fh)
