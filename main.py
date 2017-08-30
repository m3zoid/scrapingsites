"""Use it only for launch scraper module
"""

try:
    import scraper
    scraper.run()
except:
    import traceback
    print "\nUnexpected error:\n"
    traceback.print_exc()
    raw_input("\nProcess canceled. Press Enter for close...")
