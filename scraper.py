"""Main module for scraping. Here is the logic of preparation for the Bot
"""

def run():
    import pathconstructor
    import scrapingbot

    def menu():
        period_min = 10
        period_max = 3600
        period_default = 0
        period_cancel = -1
        enter_text = "Please enter a period in sec from {} till {}\n\t- for default 5 min put: {}\n\t- for cancel put: {}\n> "\
                        .format(period_min, period_max, period_default, period_cancel)
        wrong_text = "Invalid period, try again..."
        cancel_text = "Canceled"

        while True:
            try:
                nmbr = int(raw_input(enter_text))
                if nmbr == period_cancel:
                    print cancel_text
                    return False
                elif nmbr == period_default:
                    return 60 * 5
                elif nmbr >= period_min and nmbr <= period_max:
                    return nmbr
                else:
                    print wrong_text
            except ValueError:
                print wrong_text

    getperiod = menu()
    if getperiod is not False:
        source = pathconstructor.Pathconstructor().get_links()
        bot = scrapingbot.Scrapingbot(getperiod, source)
        bot.launch()

    raw_input("\nPress Enter for close...")

if __name__ == '__main__':
    try:
        run()
    except:
        import traceback
        print "\nUnexpected error:\n"
        traceback.print_exc()
        raw_input("\nProcess canceled. Press Enter for close...")
